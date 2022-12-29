# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parsing_parameters.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import configs.config


class ParsingParametersUi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(688, 520)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 651, 642))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.suppliers_combobox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.suppliers_combobox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(23)
        sizePolicy.setHeightForWidth(self.suppliers_combobox.sizePolicy().hasHeightForWidth())
        self.suppliers_combobox.setSizePolicy(sizePolicy)
        self.suppliers_combobox.setObjectName("suppliers_combobox")
        self.horizontalLayout_2.addWidget(self.suppliers_combobox, 0, QtCore.Qt.AlignTop)
        self.choose_supplier_push_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.choose_supplier_push_button.setObjectName("choose_supplier_push_button")
        self.horizontalLayout_2.addWidget(self.choose_supplier_push_button, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.article_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.article_line_edit.setObjectName("article_line_edit")
        self.verticalLayout.addWidget(self.article_line_edit)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.name_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.name_line_edit.setObjectName("name_line_edit")
        self.verticalLayout.addWidget(self.name_line_edit)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.unit_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.unit_line_edit.setObjectName("unit_line_edit")
        self.verticalLayout.addWidget(self.unit_line_edit)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.purchace_price_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.purchace_price_line_edit.setObjectName("purchace_price_line_edit")
        self.verticalLayout.addWidget(self.purchace_price_line_edit)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.quantity_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.quantity_line_edit.setObjectName("quantity_line_edit")
        self.verticalLayout.addWidget(self.quantity_line_edit)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.rrc_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.rrc_line_edit.setObjectName("rrc_line_edit")
        self.verticalLayout.addWidget(self.rrc_line_edit)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.roc_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.roc_line_edit.setObjectName("roc_line_edit")
        self.verticalLayout.addWidget(self.roc_line_edit)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.brand_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.brand_line_edit.setObjectName("brand_line_edit")
        self.verticalLayout.addWidget(self.brand_line_edit)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.selling_price_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.selling_price_line_edit.setObjectName("selling_price_line_edit")
        self.verticalLayout.addWidget(self.selling_price_line_edit)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.group_key_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.group_key_line_edit.setObjectName("group_key_line_edit")
        self.verticalLayout.addWidget(self.group_key_line_edit)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.site_name_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.site_name_line_edit.setObjectName("site_name_line_edit")
        self.verticalLayout.addWidget(self.site_name_line_edit)

        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.multiplicity_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.multiplicity_line_edit.setObjectName("multiplicity_line_edit")
        self.verticalLayout.addWidget(self.multiplicity_line_edit)

        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_push_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_push_button.sizePolicy().hasHeightForWidth())
        self.save_push_button.setSizePolicy(sizePolicy)
        self.save_push_button.setObjectName("save_push_button")
        self.horizontalLayout.addWidget(self.save_push_button, 0, QtCore.Qt.AlignRight)
        self.cancel_push_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_push_button.sizePolicy().hasHeightForWidth())
        self.cancel_push_button.setSizePolicy(sizePolicy)
        self.cancel_push_button.setObjectName("cancel_push_button")
        self.horizontalLayout.addWidget(self.cancel_push_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Параметры поставщиков"))
        self.label_2.setText(_translate("Form", "Выберите поставщика:"))
        self.choose_supplier_push_button.setText(_translate("Form", "Выбрать"))
        self.label_3.setText(_translate("Form", "Артикул"))
        self.label_4.setText(_translate("Form", "Наименование"))
        self.label_5.setText(_translate("Form", "Еденица измерения"))
        self.label_6.setText(_translate("Form", "Цена прихода"))
        self.label_13.setText(_translate("Form", "Количество (остатки)"))
        self.label_7.setText(_translate("Form", "РРЦ"))
        self.label_8.setText(_translate("Form", "РОЦ"))
        self.label_9.setText(_translate("Form", "Бренд"))
        self.label_10.setText(_translate("Form", "Цена продажи"))
        self.label_11.setText(_translate("Form", "Код группы (cheescake group_id)"))
        self.label_12.setText(_translate("Form", "Наименование для сайта"))
        self.label_14.setText(_translate("Form", "Кратность поставки"))
        self.save_push_button.setText(_translate("Form", "Сохранить"))
        self.cancel_push_button.setText(_translate("Form", "Отмена"))
