# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ryu/util/Eigene Dateien/Subversion/urh/ui/proto_sniff.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SniffProtocol(object):
    def setupUi(self, SniffProtocol):
        SniffProtocol.setObjectName("SniffProtocol")
        SniffProtocol.resize(882, 786)
        self.gridLayout_3 = QtWidgets.QGridLayout(SniffProtocol)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.spinboxErrorTolerance = QtWidgets.QSpinBox(SniffProtocol)
        self.spinboxErrorTolerance.setMaximum(999999999)
        self.spinboxErrorTolerance.setObjectName("spinboxErrorTolerance")
        self.gridLayout.addWidget(self.spinboxErrorTolerance, 9, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(SniffProtocol)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)
        self.comboxModulation = QtWidgets.QComboBox(SniffProtocol)
        self.comboxModulation.setObjectName("comboxModulation")
        self.comboxModulation.addItem("")
        self.comboxModulation.addItem("")
        self.comboxModulation.addItem("")
        self.gridLayout.addWidget(self.comboxModulation, 10, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(SniffProtocol)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(SniffProtocol)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(SniffProtocol)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(SniffProtocol)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.labelIP = QtWidgets.QLabel(SniffProtocol)
        self.labelIP.setObjectName("labelIP")
        self.gridLayout.addWidget(self.labelIP, 1, 0, 1, 1)
        self.cbDevice = QtWidgets.QComboBox(SniffProtocol)
        self.cbDevice.setObjectName("cbDevice")
        self.cbDevice.addItem("")
        self.cbDevice.addItem("")
        self.gridLayout.addWidget(self.cbDevice, 0, 1, 1, 2)
        self.spinboxCenter = QtWidgets.QDoubleSpinBox(SniffProtocol)
        self.spinboxCenter.setDecimals(4)
        self.spinboxCenter.setMinimum(-3.14)
        self.spinboxCenter.setMaximum(3.14)
        self.spinboxCenter.setObjectName("spinboxCenter")
        self.gridLayout.addWidget(self.spinboxCenter, 7, 1, 1, 2)
        self.lineEditIP = QtWidgets.QLineEdit(SniffProtocol)
        self.lineEditIP.setObjectName("lineEditIP")
        self.gridLayout.addWidget(self.lineEditIP, 1, 1, 1, 2)
        self.spinBoxGain = QtWidgets.QSpinBox(SniffProtocol)
        self.spinBoxGain.setMinimum(1)
        self.spinBoxGain.setProperty("value", 40)
        self.spinBoxGain.setObjectName("spinBoxGain")
        self.gridLayout.addWidget(self.spinBoxGain, 5, 1, 1, 2)
        self.label = QtWidgets.QLabel(SniffProtocol)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.spinboxBitLen = QtWidgets.QSpinBox(SniffProtocol)
        self.spinboxBitLen.setMinimum(1)
        self.spinboxBitLen.setMaximum(999999999)
        self.spinboxBitLen.setObjectName("spinboxBitLen")
        self.gridLayout.addWidget(self.spinboxBitLen, 8, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(SniffProtocol)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(SniffProtocol)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(SniffProtocol)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.spinboxNoise = QtWidgets.QDoubleSpinBox(SniffProtocol)
        self.spinboxNoise.setDecimals(4)
        self.spinboxNoise.setMaximum(1.0)
        self.spinboxNoise.setObjectName("spinboxNoise")
        self.gridLayout.addWidget(self.spinboxNoise, 6, 1, 1, 2)
        self.label_9 = QtWidgets.QLabel(SniffProtocol)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(SniffProtocol)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 11, 0, 1, 1)
        self.comboBoxViewType = QtWidgets.QComboBox(SniffProtocol)
        self.comboBoxViewType.setObjectName("comboBoxViewType")
        self.comboBoxViewType.addItem("")
        self.comboBoxViewType.addItem("")
        self.comboBoxViewType.addItem("")
        self.gridLayout.addWidget(self.comboBoxViewType, 11, 1, 1, 2)
        self.label_12 = QtWidgets.QLabel(SniffProtocol)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 12, 0, 1, 1)
        self.lineEditOutputFile = QtWidgets.QLineEdit(SniffProtocol)
        self.lineEditOutputFile.setReadOnly(False)
        self.lineEditOutputFile.setClearButtonEnabled(True)
        self.lineEditOutputFile.setObjectName("lineEditOutputFile")
        self.gridLayout.addWidget(self.lineEditOutputFile, 12, 1, 1, 1)
        self.spinBoxFreq = KillerDoubleSpinBox(SniffProtocol)
        self.spinBoxFreq.setMinimum(0.01)
        self.spinBoxFreq.setMaximum(1000000000000.0)
        self.spinBoxFreq.setObjectName("spinBoxFreq")
        self.gridLayout.addWidget(self.spinBoxFreq, 2, 1, 1, 1)
        self.spinBoxSampleRate = KillerDoubleSpinBox(SniffProtocol)
        self.spinBoxSampleRate.setMinimum(0.01)
        self.spinBoxSampleRate.setMaximum(1000000000000.0)
        self.spinBoxSampleRate.setObjectName("spinBoxSampleRate")
        self.gridLayout.addWidget(self.spinBoxSampleRate, 3, 1, 1, 1)
        self.spinBoxBandwidth = KillerDoubleSpinBox(SniffProtocol)
        self.spinBoxBandwidth.setMinimum(0.01)
        self.spinBoxBandwidth.setMaximum(1000000000000.0)
        self.spinBoxBandwidth.setObjectName("spinBoxBandwidth")
        self.gridLayout.addWidget(self.spinBoxBandwidth, 4, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnStart = QtWidgets.QToolButton(SniffProtocol)
        self.btnStart.setMinimumSize(QtCore.QSize(42, 42))
        self.btnStart.setMaximumSize(QtCore.QSize(42, 42))
        self.btnStart.setText("")
        icon = QtGui.QIcon.fromTheme("media-record")
        self.btnStart.setIcon(icon)
        self.btnStart.setIconSize(QtCore.QSize(32, 32))
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout.addWidget(self.btnStart)
        self.btnStop = QtWidgets.QToolButton(SniffProtocol)
        self.btnStop.setMinimumSize(QtCore.QSize(42, 42))
        self.btnStop.setMaximumSize(QtCore.QSize(42, 42))
        self.btnStop.setText("")
        icon = QtGui.QIcon.fromTheme("media-playback-stop")
        self.btnStop.setIcon(icon)
        self.btnStop.setIconSize(QtCore.QSize(32, 32))
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout.addWidget(self.btnStop)
        self.btnClear = QtWidgets.QToolButton(SniffProtocol)
        self.btnClear.setMinimumSize(QtCore.QSize(42, 42))
        self.btnClear.setMaximumSize(QtCore.QSize(42, 42))
        self.btnClear.setText("")
        icon = QtGui.QIcon.fromTheme("view-refresh")
        self.btnClear.setIcon(icon)
        self.btnClear.setIconSize(QtCore.QSize(32, 32))
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout.addWidget(self.btnClear)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.txtEditErrors = QtWidgets.QTextEdit(SniffProtocol)
        self.txtEditErrors.setReadOnly(True)
        self.txtEditErrors.setObjectName("txtEditErrors")
        self.gridLayout_3.addWidget(self.txtEditErrors, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnClose = QtWidgets.QPushButton(SniffProtocol)
        self.btnClose.setObjectName("btnClose")
        self.gridLayout_2.addWidget(self.btnClose, 1, 1, 1, 1)
        self.btnAccept = QtWidgets.QPushButton(SniffProtocol)
        self.btnAccept.setObjectName("btnAccept")
        self.gridLayout_2.addWidget(self.btnAccept, 1, 0, 1, 1)
        self.txtEdPreview = QtWidgets.QPlainTextEdit(SniffProtocol)
        self.txtEdPreview.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.txtEdPreview.setReadOnly(True)
        self.txtEdPreview.setMaximumBlockCount(100)
        self.txtEdPreview.setObjectName("txtEdPreview")
        self.gridLayout_2.addWidget(self.txtEdPreview, 0, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 3, 1)
        self.gridLayout_3.setColumnStretch(1, 1)

        self.retranslateUi(SniffProtocol)
        QtCore.QMetaObject.connectSlotsByName(SniffProtocol)

    def retranslateUi(self, SniffProtocol):
        _translate = QtCore.QCoreApplication.translate
        SniffProtocol.setWindowTitle(_translate("SniffProtocol", "Sniff Protocol"))
        self.label_6.setText(_translate("SniffProtocol", "Modulation:"))
        self.comboxModulation.setItemText(0, _translate("SniffProtocol", "ASK"))
        self.comboxModulation.setItemText(1, _translate("SniffProtocol", "FSK"))
        self.comboxModulation.setItemText(2, _translate("SniffProtocol", "PSK"))
        self.label_10.setText(_translate("SniffProtocol", "Error Tolerance:"))
        self.label_8.setText(_translate("SniffProtocol", "Center:"))
        self.label_3.setText(_translate("SniffProtocol", "Device:"))
        self.label_4.setText(_translate("SniffProtocol", "Gain:"))
        self.labelIP.setText(_translate("SniffProtocol", "IP address:"))
        self.cbDevice.setItemText(0, _translate("SniffProtocol", "USRP"))
        self.cbDevice.setItemText(1, _translate("SniffProtocol", "HackRF"))
        self.lineEditIP.setText(_translate("SniffProtocol", "192.168.10.2"))
        self.label.setText(_translate("SniffProtocol", "Frequency (Hz):"))
        self.label_2.setText(_translate("SniffProtocol", "Sample rate (Sps):"))
        self.label_5.setText(_translate("SniffProtocol", "Bandwidth (Hz):"))
        self.label_7.setText(_translate("SniffProtocol", "Noise:"))
        self.label_9.setText(_translate("SniffProtocol", "Bit Length:"))
        self.label_11.setText(_translate("SniffProtocol", "View Type:"))
        self.comboBoxViewType.setItemText(0, _translate("SniffProtocol", "Bit"))
        self.comboBoxViewType.setItemText(1, _translate("SniffProtocol", "Hex"))
        self.comboBoxViewType.setItemText(2, _translate("SniffProtocol", "ASCII"))
        self.label_12.setText(_translate("SniffProtocol", "Output file:"))
        self.lineEditOutputFile.setPlaceholderText(_translate("SniffProtocol", "None"))
        self.btnStart.setToolTip(_translate("SniffProtocol", "Record signal"))
        self.btnStop.setToolTip(_translate("SniffProtocol", "Stop recording"))
        self.btnClear.setToolTip(_translate("SniffProtocol", "Clear"))
        self.btnClose.setText(_translate("SniffProtocol", "Close"))
        self.btnAccept.setText(_translate("SniffProtocol", "Accept data"))

from urh.ui.KillerDoubleSpinBox import KillerDoubleSpinBox
