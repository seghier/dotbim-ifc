
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os
from dotbimifc import Ifc2Dotbim, Dotbim2Ifc
import ifcopenshell
import dotbimpy

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.foldername = ""
        icon_path = "bakebim.png"
        self.icon = QtGui.QIcon(icon_path)
        MainWindow.setWindowIcon(self.icon)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(592, 232)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(592, 232))
        MainWindow.setMaximumSize(QtCore.QSize(592, 232))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 551, 211))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ifcradioButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ifcradioButton.setFont(font)
        self.ifcradioButton.setChecked(True)
        self.ifcradioButton.setObjectName("ifcradioButton")
        self.horizontalLayout.addWidget(self.ifcradioButton)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.bimradioButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bimradioButton.setFont(font)
        self.bimradioButton.setObjectName("bimradioButton")
        self.horizontalLayout.addWidget(self.bimradioButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.inputButton = QtWidgets.QPushButton(self.widget)
        self.inputButton.setMinimumSize(QtCore.QSize(135, 30))
        self.inputButton.setMaximumSize(QtCore.QSize(135, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.inputButton.setFont(font)
        self.inputButton.setObjectName("inputButton")
        self.horizontalLayout_2.addWidget(self.inputButton)
        self.inputlabel = QtWidgets.QLabel(self.widget)
        self.inputlabel.setMinimumSize(QtCore.QSize(0, 30))
        self.inputlabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.inputlabel.setFont(font)
        self.inputlabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.inputlabel.setText("")
        self.inputlabel.setObjectName("inputlabel")
        self.horizontalLayout_2.addWidget(self.inputlabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.outputButton = QtWidgets.QPushButton(self.widget)
        self.outputButton.setMinimumSize(QtCore.QSize(135, 30))
        self.outputButton.setMaximumSize(QtCore.QSize(135, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.outputButton.setFont(font)
        self.outputButton.setObjectName("outputButton")
        self.horizontalLayout_3.addWidget(self.outputButton)
        self.outputlabel = QtWidgets.QLabel(self.widget)
        self.outputlabel.setMinimumSize(QtCore.QSize(0, 30))
        self.outputlabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.outputlabel.setFont(font)
        self.outputlabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.outputlabel.setText("")
        self.outputlabel.setObjectName("outputlabel")
        self.horizontalLayout_3.addWidget(self.outputlabel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.convertButton = QtWidgets.QPushButton(self.widget)
        self.convertButton.setMinimumSize(QtCore.QSize(0, 50))
        self.convertButton.setMaximumSize(QtCore.QSize(16666666, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.convertButton.setFont(font)
        self.convertButton.setObjectName("convertButton")
        self.verticalLayout.addWidget(self.convertButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to functions
        self.inputButton.clicked.connect(self.chooseInputFile)
        self.outputButton.clicked.connect(self.chooseOutputFolder)
        self.convertButton.clicked.connect(self.convert)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IFC to BIM and BIM to IFC Converter"))
        self.ifcradioButton.setText(_translate("MainWindow", "IFC to BIM"))
        self.bimradioButton.setText(_translate("MainWindow", "BIM to IFC"))
        self.inputButton.setText(_translate("MainWindow", "Select Input File"))
        self.outputButton.setText(_translate("MainWindow", "Select Output Folder"))
        self.convertButton.setText(_translate("MainWindow", "Convert"))

    def chooseInputFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        if self.ifcradioButton.isChecked():
            file, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select IFC File", "", "IFC Files (*.ifc);;All Files (*)", options=options)
        else:
            file, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select BIM File", "", "BIM Files (*.bim);;All Files (*)", options=options)

        if file:
            self.inputlabel.setText(file)

    def chooseOutputFolder(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        folder = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Output Folder", "", options=options)
        if self.ifcradioButton.isChecked():
            output_file_name = os.path.splitext(os.path.basename(self.inputlabel.text()))[0] + ".bim"
        else:
            output_file_name = os.path.splitext(os.path.basename(self.inputlabel.text()))[0] + ".ifc"
        outfile = os.path.join(folder, output_file_name)
        self.foldername = folder
        if folder:
            self.outputlabel.setText(outfile)

    def convert(self):
        input_file = self.inputlabel.text()
        output_folder = self.foldername

        if self.ifcradioButton.isChecked():
            self.IFC2BIM(input_file, output_folder)
        elif self.bimradioButton.isChecked():
            self.BIM2IFC(input_file, output_folder)

    def IFC2BIM(self, ifcfile, output_folder):
        ifc = ifcopenshell.open(ifcfile)
        ifc2dotbim = Ifc2Dotbim(ifc)
        ifc2dotbim.execute()
        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(ifcfile))[0] + ".bim")
        ifc2dotbim.write(output_file)
        self.showMessageBox("Conversion Complete", "IFC to BIM conversion is complete!")

    def BIM2IFC(self, bimfile, output_folder):
        dotbim = dotbimpy.File.read(bimfile)
        dotbim2ifc = Dotbim2Ifc(dotbim)
        dotbim2ifc.execute()
        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(bimfile))[0] + ".ifc")
        dotbim2ifc.write(output_file)
        self.showMessageBox("Conversion Complete", "BIM to IFC conversion is complete!")

    def showMessageBox(self, title, message, icon=QtWidgets.QMessageBox.Information):
        msgBox = QMessageBox()
        msgBox.setWindowIcon(self.icon)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
