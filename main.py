import sys
from PySide2.QtCore import(Property, QObject, QPropertyAnimation, Signal)
from PySide2.QtGui import (QGuiApplication, QMatrix4x4, QQuaternion, QVector3D, QVector4D, QColor)
from PySide2.Qt3DCore import (Qt3DCore)
from PySide2.Qt3DExtras import (Qt3DExtras)

from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QTableWidgetItem
from PySide2.QtCore import QFile, QObject, SIGNAL, QStringListModel
from ui_mainwindow import Ui_MainWindow


class Object(QObject):
    def __init__(self, type, entity, figure, transform, material):
        super().__init__()
        self.type = type
        self.name = "new_" + self.type
        self.entity = entity
        self.figure = figure
        self.transform = transform
        self.material = material
        self.history = []


class Sphere(Qt3DExtras.QSphereMesh):
    def __init__(self):
        super().__init__()
        self.setRadius(3)

class Box(Qt3DExtras.QCuboidMesh):
    def __init__(self):
        super().__init__()
        self.setXExtent(4)
        self.setYExtent(4)
        self.setZExtent(4)

class ObjectsWindow(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.par_ui = ui

        # Construct Layout
        layout = QVBoxLayout(self)
        self.view = Qt3DExtras.Qt3DWindow()
        container = QWidget.createWindowContainer(self.view)
        layout.addWidget(container)
        self.objects = []
        self.garbage = []
        self.lastInfoRow = -1

        # Camera
        self.camera = self.view.camera()
        self.camera.lens().setPerspectiveProjection(45, 16 / 9, 0.1, 1000)
        self.camera.setPosition(QVector3D(0, 0, 40))
        self.camera.setViewCenter(QVector3D(0, 0, 0))

        # Root entity & Material
        self.rootEntity = Qt3DCore.QEntity()

        # First-person controller
        self.firstPersonController = Qt3DExtras.QFirstPersonCameraController(self.rootEntity)
        self.firstPersonController.setCamera(self.camera)

        QObject.connect(self.par_ui.addSphere, SIGNAL('clicked()'), self.addSphere)
        QObject.connect(self.par_ui.addBox, SIGNAL('clicked()'), self.addBox)
        QObject.connect(self.par_ui.deleteObject, SIGNAL('clicked()'), self.deleteObject)
        QObject.connect(self.par_ui.showInfo, SIGNAL('clicked()'), self.showInfo)
        QObject.connect(self.par_ui.updateInfo, SIGNAL('clicked()'), self.updateInfo)

        self.view.setRootEntity(self.rootEntity)

        self.objectsModel = QStringListModel()
        self.par_ui.currentObjectsView.setModel(self.objectsModel)

    def showInfo(self):
        row = self.par_ui.currentObjectsView.currentIndex().row()
        if row >= 0:
            self.lastInfoRow = row
            object = self.objects[self.lastInfoRow]

            data = object.transform.matrix().data()
            self.par_ui.objectInfoWidget.setRowCount(4)
            self.par_ui.objectInfoWidget.setColumnCount(4)
            for i in range(4):
                for j in range(4):
                    self.par_ui.objectInfoWidget.setItem(i,j,QTableWidgetItem(str(data[i * 4 + j])))
            print(object.material.ambient().red())

            ambient = object.material.ambient()
            self.par_ui.rColor.setText(str(ambient.red()))
            self.par_ui.gColor.setText(str(ambient.green()))
            self.par_ui.bColor.setText(str(ambient.blue()))
            self.par_ui.aColor.setText(str(ambient.alpha()))


    def updateInfo(self):
        if self.lastInfoRow >= 0:
            newData = []
            matrix = QMatrix4x4()
            for i in range(4):
                newRow = []
                for j in range(4):
                    val = self.par_ui.objectInfoWidget.item(i,j)
                    newRow.append(float(val.text()))
                print(newRow, i, j)

                matrix.setRow(i, QVector4D(newRow[0], newRow[1], newRow[2], newRow[3]))

            transform = self.objects[self.lastInfoRow].transform
            transform.setMatrix(matrix)

            color = QColor()
            color.setRed(int(self.par_ui.rColor.toPlainText()))
            color.setGreen(int(self.par_ui.gColor.toPlainText()))
            color.setBlue(int(self.par_ui.bColor.toPlainText()))
            color.setAlpha(int(self.par_ui.aColor.toPlainText()))

            material = self.objects[self.lastInfoRow].material
            material.setAmbient(color)

    def addSphere(self):
        self.addObject("sphere")

    def addBox(self):
        self.addObject("box")

    def addCustom(self):
        pass

    def addObject(self, type):
        entity = Qt3DCore.QEntity(self.rootEntity)
        material = Qt3DExtras.QPhongMaterial(self.rootEntity)

        if type == "sphere":
            figure = Sphere()
        else:
            figure = Box()
        transform = Qt3DCore.QTransform()

        entity.addComponent(figure)
        entity.addComponent(material)
        entity.addComponent(transform)

        object = Object(type, entity, figure, transform, material)
        self.objects.append(object)

        idx = self.objectsModel.rowCount()
        self.objectsModel.insertRow(idx)
        self.objectsModel.setData(self.objectsModel.index(idx), "new_" + type)

    def deleteObject(self):
        row = self.par_ui.currentObjectsView.currentIndex().row()
        if row >= 0:
            self.objectsModel.removeRow(row)

            # for reference count
            self.garbage.append(self.objects[row])
            self.objects[row].figure.setEnabled(False)
            self.objects[row].entity.setEnabled(False)

            del self.objects[row]



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        objectsWindow = ObjectsWindow(self.ui)
        self.ui.objectsLayout.addWidget(objectsWindow)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
