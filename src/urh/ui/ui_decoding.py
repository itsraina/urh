# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ryu/util/Eigene Dateien/Subversion/urh/ui/decoding.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Decoder(object):
    def setupUi(self, Decoder):
        Decoder.setObjectName("Decoder")
        Decoder.setWindowModality(QtCore.Qt.WindowModal)
        Decoder.resize(923, 685)
        Decoder.setModal(True)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Decoder)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.combobox_decodings = QtWidgets.QComboBox(Decoder)
        self.combobox_decodings.setObjectName("combobox_decodings")
        self.combobox_decodings.addItem("")
        self.combobox_decodings.addItem("")
        self.horizontalLayout_2.addWidget(self.combobox_decodings)
        self.delete_decoding = QtWidgets.QPushButton(Decoder)
        self.delete_decoding.setObjectName("delete_decoding")
        self.horizontalLayout_2.addWidget(self.delete_decoding)
        self.saveas = QtWidgets.QPushButton(Decoder)
        self.saveas.setObjectName("saveas")
        self.horizontalLayout_2.addWidget(self.saveas)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(Decoder)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.basefunctions = QtWidgets.QListWidget(Decoder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.basefunctions.sizePolicy().hasHeightForWidth())
        self.basefunctions.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.basefunctions.setFont(font)
        self.basefunctions.setDragEnabled(True)
        self.basefunctions.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.basefunctions.setObjectName("basefunctions")
        self.verticalLayout_2.addWidget(self.basefunctions)
        self.label_9 = QtWidgets.QLabel(Decoder)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.additionalfunctions = QtWidgets.QListWidget(Decoder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.additionalfunctions.sizePolicy().hasHeightForWidth())
        self.additionalfunctions.setSizePolicy(sizePolicy)
        self.additionalfunctions.setDragEnabled(True)
        self.additionalfunctions.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.additionalfunctions.setObjectName("additionalfunctions")
        self.verticalLayout_2.addWidget(self.additionalfunctions)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Decoder)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(Decoder)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.decoderchain = ListWidget(Decoder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decoderchain.sizePolicy().hasHeightForWidth())
        self.decoderchain.setSizePolicy(sizePolicy)
        self.decoderchain.setAcceptDrops(True)
        self.decoderchain.setDragEnabled(True)
        self.decoderchain.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.decoderchain.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.decoderchain.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.decoderchain.setResizeMode(QtWidgets.QListView.Fixed)
        self.decoderchain.setViewMode(QtWidgets.QListView.ListMode)
        self.decoderchain.setObjectName("decoderchain")
        self.verticalLayout.addWidget(self.decoderchain)
        self.label_7 = QtWidgets.QLabel(Decoder)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gb_infoandoptions = QtWidgets.QGroupBox(Decoder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_infoandoptions.sizePolicy().hasHeightForWidth())
        self.gb_infoandoptions.setSizePolicy(sizePolicy)
        self.gb_infoandoptions.setObjectName("gb_infoandoptions")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.gb_infoandoptions)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.info = QtWidgets.QLabel(self.gb_infoandoptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(True)
        self.info.setFont(font)
        self.info.setTextFormat(QtCore.Qt.PlainText)
        self.info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.info.setWordWrap(True)
        self.info.setObjectName("info")
        self.verticalLayout_5.addWidget(self.info)
        self.optionWidget = QtWidgets.QStackedWidget(self.gb_infoandoptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionWidget.sizePolicy().hasHeightForWidth())
        self.optionWidget.setSizePolicy(sizePolicy)
        self.optionWidget.setObjectName("optionWidget")
        self.page_empty = QtWidgets.QWidget()
        self.page_empty.setObjectName("page_empty")
        self.optionWidget.addWidget(self.page_empty)
        self.page_redundancy = QtWidgets.QWidget()
        self.page_redundancy.setObjectName("page_redundancy")
        self.multiple = QtWidgets.QSpinBox(self.page_redundancy)
        self.multiple.setGeometry(QtCore.QRect(0, 0, 56, 23))
        self.multiple.setMinimum(2)
        self.multiple.setObjectName("multiple")
        self.label_5 = QtWidgets.QLabel(self.page_redundancy)
        self.label_5.setGeometry(QtCore.QRect(60, 0, 171, 21))
        self.label_5.setObjectName("label_5")
        self.optionWidget.addWidget(self.page_redundancy)
        self.page_carrier = QtWidgets.QWidget()
        self.page_carrier.setObjectName("page_carrier")
        self.carrier = QtWidgets.QLineEdit(self.page_carrier)
        self.carrier.setGeometry(QtCore.QRect(0, 0, 113, 23))
        self.carrier.setObjectName("carrier")
        self.label_6 = QtWidgets.QLabel(self.page_carrier)
        self.label_6.setGeometry(QtCore.QRect(120, 0, 171, 21))
        self.label_6.setObjectName("label_6")
        self.optionWidget.addWidget(self.page_carrier)
        self.page_substitution = QtWidgets.QWidget()
        self.page_substitution.setObjectName("page_substitution")
        self.gridLayout = QtWidgets.QGridLayout(self.page_substitution)
        self.gridLayout.setObjectName("gridLayout")
        self.substitution_rows = QtWidgets.QSpinBox(self.page_substitution)
        self.substitution_rows.setMinimum(1)
        self.substitution_rows.setMaximum(1000)
        self.substitution_rows.setProperty("value", 4)
        self.substitution_rows.setObjectName("substitution_rows")
        self.gridLayout.addWidget(self.substitution_rows, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.page_substitution)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 1, 1, 1)
        self.substitution = QtWidgets.QTableWidget(self.page_substitution)
        self.substitution.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.substitution.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.substitution.setObjectName("substitution")
        self.substitution.setColumnCount(0)
        self.substitution.setRowCount(0)
        self.gridLayout.addWidget(self.substitution, 1, 0, 1, 2)
        self.optionWidget.addWidget(self.page_substitution)
        self.page_external = QtWidgets.QWidget()
        self.page_external.setObjectName("page_external")
        self.external_decoder = QtWidgets.QLineEdit(self.page_external)
        self.external_decoder.setGeometry(QtCore.QRect(0, 0, 291, 23))
        self.external_decoder.setObjectName("external_decoder")
        self.external_encoder = QtWidgets.QLineEdit(self.page_external)
        self.external_encoder.setGeometry(QtCore.QRect(0, 30, 291, 23))
        self.external_encoder.setObjectName("external_encoder")
        self.label_11 = QtWidgets.QLabel(self.page_external)
        self.label_11.setGeometry(QtCore.QRect(300, 0, 71, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_external)
        self.label_12.setGeometry(QtCore.QRect(300, 30, 71, 21))
        self.label_12.setObjectName("label_12")
        self.optionWidget.addWidget(self.page_external)
        self.page_data_whitening = QtWidgets.QWidget()
        self.page_data_whitening.setObjectName("page_data_whitening")
        self.datawhitening_sync = QtWidgets.QLineEdit(self.page_data_whitening)
        self.datawhitening_sync.setGeometry(QtCore.QRect(0, 0, 171, 23))
        self.datawhitening_sync.setObjectName("datawhitening_sync")
        self.label_13 = QtWidgets.QLabel(self.page_data_whitening)
        self.label_13.setGeometry(QtCore.QRect(180, 0, 231, 20))
        self.label_13.setObjectName("label_13")
        self.datawhitening_polynomial = QtWidgets.QLineEdit(self.page_data_whitening)
        self.datawhitening_polynomial.setGeometry(QtCore.QRect(0, 30, 171, 23))
        self.datawhitening_polynomial.setObjectName("datawhitening_polynomial")
        self.label_14 = QtWidgets.QLabel(self.page_data_whitening)
        self.label_14.setGeometry(QtCore.QRect(180, 30, 291, 21))
        self.label_14.setObjectName("label_14")
        self.datawhitening_applycrc = QtWidgets.QCheckBox(self.page_data_whitening)
        self.datawhitening_applycrc.setGeometry(QtCore.QRect(0, 60, 261, 21))
        self.datawhitening_applycrc.setObjectName("datawhitening_applycrc")
        self.datawhitening_preamble_rm = QtWidgets.QCheckBox(self.page_data_whitening)
        self.datawhitening_preamble_rm.setGeometry(QtCore.QRect(0, 80, 221, 21))
        self.datawhitening_preamble_rm.setObjectName("datawhitening_preamble_rm")
        self.datawhitening_sync_rm = QtWidgets.QCheckBox(self.page_data_whitening)
        self.datawhitening_sync_rm.setGeometry(QtCore.QRect(0, 100, 261, 21))
        self.datawhitening_sync_rm.setObjectName("datawhitening_sync_rm")
        self.datawhitening_crc_rm = QtWidgets.QCheckBox(self.page_data_whitening)
        self.datawhitening_crc_rm.setGeometry(QtCore.QRect(0, 120, 131, 21))
        self.datawhitening_crc_rm.setObjectName("datawhitening_crc_rm")
        self.optionWidget.addWidget(self.page_data_whitening)
        self.verticalLayout_5.addWidget(self.optionWidget)
        self.optionWidget.raise_()
        self.info.raise_()
        self.verticalLayout_3.addWidget(self.gb_infoandoptions)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(Decoder)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.combobox_signals = QtWidgets.QComboBox(Decoder)
        self.combobox_signals.setObjectName("combobox_signals")
        self.combobox_signals.addItem("")
        self.gridLayout_2.addWidget(self.combobox_signals, 1, 0, 1, 1)
        self.output = QtWidgets.QLineEdit(Decoder)
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.gridLayout_2.addWidget(self.output, 5, 0, 1, 2)
        self.decoding_errors_label = QtWidgets.QLabel(Decoder)
        self.decoding_errors_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.decoding_errors_label.setObjectName("decoding_errors_label")
        self.gridLayout_2.addWidget(self.decoding_errors_label, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Decoder)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.inpt = QtWidgets.QLineEdit(Decoder)
        self.inpt.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.inpt.setObjectName("inpt")
        self.gridLayout_2.addWidget(self.inpt, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        self.graphicsView_signal = ZoomableGraphicView(Decoder)
        self.graphicsView_signal.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView_signal.setObjectName("graphicsView_signal")
        self.gridLayout_2.addWidget(self.graphicsView_signal, 2, 0, 1, 2)
        self.graphicsView_decoded = ZoomableGraphicView(Decoder)
        self.graphicsView_decoded.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView_decoded.setObjectName("graphicsView_decoded")
        self.gridLayout_2.addWidget(self.graphicsView_decoded, 3, 0, 1, 2)
        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.retranslateUi(Decoder)
        self.optionWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(Decoder)

    def retranslateUi(self, Decoder):
        _translate = QtCore.QCoreApplication.translate
        Decoder.setWindowTitle(_translate("Decoder", "Decoding"))
        self.combobox_decodings.setItemText(0, _translate("Decoder", "Non Return to Zero (NRZ)"))
        self.combobox_decodings.setItemText(1, _translate("Decoder", "Empty"))
        self.delete_decoding.setText(_translate("Decoder", "Delete"))
        self.saveas.setText(_translate("Decoder", "Save as..."))
        self.label_8.setText(_translate("Decoder", "Base Functions"))
        self.label_9.setText(_translate("Decoder", "Additional Functions"))
        self.label.setText(_translate("Decoder", "Decoder"))
        self.label_4.setText(_translate("Decoder", "Signal"))
        self.label_7.setText(_translate("Decoder", "Decoded Bits"))
        self.gb_infoandoptions.setTitle(_translate("Decoder", "Information and Options"))
        self.info.setText(_translate("Decoder", "Please drag functions from the categories base and additional to the decoding process (Decoder). You can reorder functions by drag and drop and remove functions by dropping them outside the Decoder box. Click on every function for detailed information."))
        self.label_5.setText(_translate("Decoder", "Number of redundant bits"))
        self.label_6.setText(_translate("Decoder", "Carrier (\'1\' -> 1_1_1_1...)"))
        self.label_10.setText(_translate("Decoder", "Rows"))
        self.label_11.setText(_translate("Decoder", "Decoder"))
        self.label_12.setText(_translate("Decoder", "Encoder"))
        self.label_13.setText(_translate("Decoder", "Synchronization bytes (hex coded)"))
        self.label_14.setText(_translate("Decoder", "Data whitening polynomial (LFSR, hex coded)"))
        self.datawhitening_applycrc.setText(_translate("Decoder", "Compute and apply CRC-16 via XOR"))
        self.datawhitening_preamble_rm.setText(_translate("Decoder", "Remove Preamble (1010...)"))
        self.datawhitening_sync_rm.setText(_translate("Decoder", "Remove Synchronization bytes"))
        self.datawhitening_crc_rm.setText(_translate("Decoder", "Remove CRC-16"))
        self.label_3.setText(_translate("Decoder", "Decoded Bits:"))
        self.combobox_signals.setItemText(0, _translate("Decoder", "Test"))
        self.decoding_errors_label.setText(_translate("Decoder", "[Decoding Errors = 0]"))
        self.label_2.setText(_translate("Decoder", "Signal {0,1}:"))

from urh.ui.ListWidget import ListWidget
from urh.ui.views.ZoomableGraphicView import ZoomableGraphicView
