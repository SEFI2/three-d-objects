import sys
from PySide2.QtCore import(Property, QObject, QPropertyAnimation, Signal)
from PySide2.QtGui import (QGuiApplication, QMatrix4x4, QQuaternion, QVector3D)
from PySide2.Qt3DCore import (Qt3DCore)
from PySide2.Qt3DExtras import (Qt3DExtras)

from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PySide2.QtCore import QFile, QObject, SIGNAL, QStringListModel
from ui_mainwindow import Ui_MainWindow


class Sphere(Qt3DExtras.QSphereMesh):
    def __init__(self):
        super().__init__()
        self.setRadius(3)
        history = []

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
        # Camera
        self.camera = self.view.camera()
        self.camera.lens().setPerspectiveProjection(45, 16 / 9, 0.1, 1000)
        self.camera.setPosition(QVector3D(0, 0, 40))
        self.camera.setViewCenter(QVector3D(0, 0, 0))

        # Root entity & Material
        self.rootEntity = Qt3DCore.QEntity()
        self.material = Qt3DExtras.QPhongMaterial(self.rootEntity)

        # First-person controller
        self.firstPersonController = Qt3DExtras.QFirstPersonCameraController(self.rootEntity)
        self.firstPersonController.setCamera(self.camera)

        self.view.setRootEntity(self.rootEntity)

        model = QStringListModel()

        QObject.connect(self.par_ui.addSphere, SIGNAL('clicked()'), self.addSphere)
        QObject.connect(self.par_ui.addBox, SIGNAL('clicked()'), self.addBox)



    def addSphere(self):
        sphereEntity = Qt3DCore.QEntity(self.rootEntity)
        sphere = Sphere()

        sphereEntity.addComponent(sphere)
        sphereEntity.addComponent(self.material)

        self.objects.append([sphere, sphereEntity])

    def addBox(self):
        boxEntity = Qt3DCore.QEntity(self.rootEntity)
        box = Box()

        boxEntity.addComponent(box)
        boxEntity.addComponent(self.material)

        self.objects.append([box, boxEntity])


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
