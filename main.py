import sys
import pickle

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

        dumpData = self.loadDump()
        print(dumpData)
        for data in dumpData:
            if data['type'] == 'sphere':
                self.addSphere()
            else:
                self.addBox()
            idx = len(self.objects) - 1
            self.objects[idx].transform.setMatrix(data['matrix'])
            self.objects[idx].material.setAmbient(data['ambient'])
            if data['type'] == 'sphere':
                self.objects[idx].figure.setRadius(data['size'])
            else:
                self.objects[idx].figure.setXExtent(data['size1'])
                self.objects[idx].figure.setYExtent(data['size2'])
                self.objects[idx].figure.setZExtent(data['size3'])


        self.dump()

    def showInfo(self):
        row = self.par_ui.currentObjectsView.currentIndex().row()
        if row >= 0:
            self.lastInfoRow = row
            object = self.objects[self.lastInfoRow]

            # show matrix
            data = object.transform.matrix().data()
            self.par_ui.objectInfoWidget.setRowCount(4)
            self.par_ui.objectInfoWidget.setColumnCount(4)
            for i in range(4):
                for j in range(4):
                    self.par_ui.objectInfoWidget.setItem(i, j, QTableWidgetItem(str(data[i * 4 + j])))

            # show color
            ambient = object.material.ambient()
            self.par_ui.rColor.setText(str(ambient.red()))
            self.par_ui.gColor.setText(str(ambient.green()))
            self.par_ui.bColor.setText(str(ambient.blue()))
            self.par_ui.aColor.setText(str(ambient.alpha()))

            # show size
            if object.type == 'sphere':
                self.par_ui.size1.show()
                self.par_ui.size2.hide()
                self.par_ui.size3.hide()
                self.par_ui.size1.setText(str(object.figure.radius()))
            else:
                self.par_ui.size1.show()
                self.par_ui.size2.show()
                self.par_ui.size3.show()
                self.par_ui.size1.setText(str(object.figure.xExtent()))
                self.par_ui.size2.setText(str(object.figure.yExtent()))
                self.par_ui.size3.setText(str(object.figure.zExtent()))



    def updateInfo(self):
        if self.lastInfoRow >= 0:
            # get matrix
            matrix = QMatrix4x4()
            for i in range(4):
                newRow = []
                for j in range(4):
                    val = self.par_ui.objectInfoWidget.item(i,j)
                    newRow.append(float(val.text()))
                print(newRow, i, j)

                matrix.setRow(i, QVector4D(newRow[0], newRow[1], newRow[2], newRow[3]))

            object = self.objects[self.lastInfoRow]

            # update matrix
            transform = object.transform
            transform.setMatrix(matrix)

            # update color
            color = QColor()
            color.setRed(int(self.par_ui.rColor.toPlainText()))
            color.setGreen(int(self.par_ui.gColor.toPlainText()))
            color.setBlue(int(self.par_ui.bColor.toPlainText()))
            color.setAlpha(int(self.par_ui.aColor.toPlainText()))
            material = object.material
            material.setAmbient(color)

            # update size
            if object.type == 'sphere':
                object.figure.setRadius(float(self.par_ui.size1.toPlainText()))
            else:
                object.figure.setXExtent(float(self.par_ui.size1.toPlainText()))
                object.figure.setYExtent(float(self.par_ui.size2.toPlainText()))
                object.figure.setZExtent(float(self.par_ui.size3.toPlainText()))
            self.dump()


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
        self.dump()

    def deleteObject(self):
        row = self.par_ui.currentObjectsView.currentIndex().row()
        if row >= 0:
            self.objectsModel.removeRow(row)

            # for reference count
            self.garbage.append(self.objects[row])
            self.objects[row].figure.setEnabled(False)
            self.objects[row].entity.setEnabled(False)

            del self.objects[row]
            self.dump()

    def loadDump(self):
        try:
            with open('editorDump.pkl', 'rb') as input:
                return pickle.load(input)
        except:
            return []

    def dump(self):
        dumpData = []
        for obj in self.objects:
            data = {'matrix': obj.transform.matrix(), 'type': obj.type, 'ambient': obj.material.ambient()}
            if obj.type == 'sphere':
                data['size'] = obj.figure.radius()
            else:
                data['size1'] = obj.figure.xExtent()
                data['size2'] = obj.figure.yExtent()
                data['size3'] = obj.figure.zExtent()
            dumpData.append(data)
        with open('editorDump.pkl', 'wb') as output:
            pickle.dump(dumpData, output, pickle.HIGHEST_PROTOCOL)
        print(dumpData)

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
