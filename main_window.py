# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 646)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("work_files/blue-cherry-268x268.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.prepare_passport_tab = QtWidgets.QWidget()
        self.prepare_passport_tab.setObjectName("prepare_passport_tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.prepare_passport_tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.prepare_passport_label = QtWidgets.QLabel(self.prepare_passport_tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.prepare_passport_label.setFont(font)
        self.prepare_passport_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prepare_passport_label.setObjectName("prepare_passport_label")
        self.verticalLayout.addWidget(self.prepare_passport_label)
        self.passport_tree_widget = QtWidgets.QTreeWidget(self.prepare_passport_tab)
        self.passport_tree_widget.setObjectName("passport_tree_widget")
        self.passport_tree_widget.header().setDefaultSectionSize(300)
        self.verticalLayout.addWidget(self.passport_tree_widget)
        self.result_path_label = QtWidgets.QLabel(self.prepare_passport_tab)
        self.result_path_label.setObjectName("result_path_label")
        self.verticalLayout.addWidget(self.result_path_label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.result_path_line_edit = QtWidgets.QLineEdit(self.prepare_passport_tab)
        self.result_path_line_edit.setReadOnly(True)
        self.result_path_line_edit.setObjectName("result_path_line_edit")
        self.horizontalLayout_4.addWidget(self.result_path_line_edit)
        self.set_result_path_push_button = QtWidgets.QPushButton(self.prepare_passport_tab)
        self.set_result_path_push_button.setObjectName("set_result_path_push_button")
        self.horizontalLayout_4.addWidget(self.set_result_path_push_button)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_passport_files_push_button = QtWidgets.QPushButton(self.prepare_passport_tab)
        self.add_passport_files_push_button.setObjectName("add_passport_files_push_button")
        self.horizontalLayout_3.addWidget(self.add_passport_files_push_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.delete_selected_passport_file_push_button = QtWidgets.QPushButton(self.prepare_passport_tab)
        self.delete_selected_passport_file_push_button.setObjectName("delete_selected_passport_file_push_button")
        self.horizontalLayout_3.addWidget(self.delete_selected_passport_file_push_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.start_passport_protection_push_button = QtWidgets.QPushButton(self.prepare_passport_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.start_passport_protection_push_button.setFont(font)
        self.start_passport_protection_push_button.setObjectName("start_passport_protection_push_button")
        self.horizontalLayout_3.addWidget(self.start_passport_protection_push_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.prepare_passport_tab, "")
        self.cheescake_parser_tab = QtWidgets.QWidget()
        self.cheescake_parser_tab.setObjectName("cheescake_parser_tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.cheescake_parser_tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.manual_parser_label = QtWidgets.QLabel(self.cheescake_parser_tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.manual_parser_label.setFont(font)
        self.manual_parser_label.setAlignment(QtCore.Qt.AlignCenter)
        self.manual_parser_label.setObjectName("manual_parser_label")
        self.verticalLayout_2.addWidget(self.manual_parser_label)
        self.test_push_button = QtWidgets.QPushButton(self.cheescake_parser_tab)
        self.test_push_button.setObjectName("test_push_button")
        self.verticalLayout_2.addWidget(self.test_push_button)
        self.manual_parser_tree_widget = QtWidgets.QTreeWidget(self.cheescake_parser_tab)
        self.manual_parser_tree_widget.setObjectName("manual_parser_tree_widget")
        self.manual_parser_tree_widget.header().setDefaultSectionSize(200)
        self.verticalLayout_2.addWidget(self.manual_parser_tree_widget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.add_price_push_button = QtWidgets.QPushButton(self.cheescake_parser_tab)
        self.add_price_push_button.setObjectName("add_price_push_button")
        self.horizontalLayout_6.addWidget(self.add_price_push_button)
        self.add_multiple_price_push_button = QtWidgets.QPushButton(self.cheescake_parser_tab)
        self.add_multiple_price_push_button.setObjectName("add_multiple_price_push_button")
        self.horizontalLayout_6.addWidget(self.add_multiple_price_push_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.delete_price_push_button = QtWidgets.QPushButton(self.cheescake_parser_tab)
        self.delete_price_push_button.setObjectName("delete_price_push_button")
        self.horizontalLayout_6.addWidget(self.delete_price_push_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.line_4 = QtWidgets.QFrame(self.cheescake_parser_tab)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.start_parsing_push_button = QtWidgets.QPushButton(self.cheescake_parser_tab)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.start_parsing_push_button.setPalette(palette)
        self.start_parsing_push_button.setObjectName("start_parsing_push_button")
        self.verticalLayout_2.addWidget(self.start_parsing_push_button)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(self.cheescake_parser_tab)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_9.addWidget(self.line)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.auto_parser_label = QtWidgets.QLabel(self.cheescake_parser_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auto_parser_label.sizePolicy().hasHeightForWidth())
        self.auto_parser_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.auto_parser_label.setFont(font)
        self.auto_parser_label.setAlignment(QtCore.Qt.AlignCenter)
        self.auto_parser_label.setObjectName("auto_parser_label")
        self.verticalLayout_3.addWidget(self.auto_parser_label)
        self.line_2 = QtWidgets.QFrame(self.cheescake_parser_tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.kvt_label = QtWidgets.QLabel(self.cheescake_parser_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kvt_label.sizePolicy().hasHeightForWidth())
        self.kvt_label.setSizePolicy(sizePolicy)
        self.kvt_label.setObjectName("kvt_label")
        self.verticalLayout_5.addWidget(self.kvt_label, 0, QtCore.Qt.AlignHCenter)
        self.link_kvt_line_edit = QtWidgets.QLineEdit(self.cheescake_parser_tab)
        self.link_kvt_line_edit.setObjectName("link_kvt_line_edit")
        self.verticalLayout_5.addWidget(self.link_kvt_line_edit)
        self.parse_kvt_push_button = QtWidgets.QPushButton(self.cheescake_parser_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parse_kvt_push_button.sizePolicy().hasHeightForWidth())
        self.parse_kvt_push_button.setSizePolicy(sizePolicy)
        self.parse_kvt_push_button.setObjectName("parse_kvt_push_button")
        self.verticalLayout_5.addWidget(self.parse_kvt_push_button, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.torg7_label = QtWidgets.QLabel(self.cheescake_parser_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.torg7_label.sizePolicy().hasHeightForWidth())
        self.torg7_label.setSizePolicy(sizePolicy)
        self.torg7_label.setObjectName("torg7_label")
        self.verticalLayout_4.addWidget(self.torg7_label, 0, QtCore.Qt.AlignHCenter)
        self.link_torg7_line_edit = QtWidgets.QLineEdit(self.cheescake_parser_tab)
        self.link_torg7_line_edit.setObjectName("link_torg7_line_edit")
        self.verticalLayout_4.addWidget(self.link_torg7_line_edit)
        self.parse_torg7_push_button = QtWidgets.QPushButton(self.cheescake_parser_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parse_torg7_push_button.sizePolicy().hasHeightForWidth())
        self.parse_torg7_push_button.setSizePolicy(sizePolicy)
        self.parse_torg7_push_button.setObjectName("parse_torg7_push_button")
        self.verticalLayout_4.addWidget(self.parse_torg7_push_button, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.a4_label = QtWidgets.QLabel(self.cheescake_parser_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a4_label.sizePolicy().hasHeightForWidth())
        self.a4_label.setSizePolicy(sizePolicy)
        self.a4_label.setObjectName("a4_label")
        self.verticalLayout_9.addWidget(self.a4_label, 0, QtCore.Qt.AlignHCenter)
        self.link_a4_line_edit = QtWidgets.QLineEdit(self.cheescake_parser_tab)
        self.link_a4_line_edit.setObjectName("link_a4_line_edit")
        self.verticalLayout_9.addWidget(self.link_a4_line_edit)
        self.parse_a4_push_button = QtWidgets.QPushButton(self.cheescake_parser_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parse_a4_push_button.sizePolicy().hasHeightForWidth())
        self.parse_a4_push_button.setSizePolicy(sizePolicy)
        self.parse_a4_push_button.setObjectName("parse_a4_push_button")
        self.verticalLayout_9.addWidget(self.parse_a4_push_button, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.verticalLayout_9)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.line_3 = QtWidgets.QFrame(self.cheescake_parser_tab)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        self.horizontalLayout_9.setStretch(0, 500)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.label = QtWidgets.QLabel(self.cheescake_parser_tab)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.result_path_parser_line_edit = QtWidgets.QLineEdit(self.cheescake_parser_tab)
        self.result_path_parser_line_edit.setReadOnly(True)
        self.result_path_parser_line_edit.setObjectName("result_path_parser_line_edit")
        self.horizontalLayout_5.addWidget(self.result_path_parser_line_edit)
        self.add_result_path_parser_push_button = QtWidgets.QPushButton(self.cheescake_parser_tab)
        self.add_result_path_parser_push_button.setObjectName("add_result_path_parser_push_button")
        self.horizontalLayout_5.addWidget(self.add_result_path_parser_push_button)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.cheescake_parser_tab, "")
        self.prepare_photo_archive_tab = QtWidgets.QWidget()
        self.prepare_photo_archive_tab.setObjectName("prepare_photo_archive_tab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.prepare_photo_archive_tab)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.articles_without_photo_table_widget = QtWidgets.QTableWidget(self.prepare_photo_archive_tab)
        self.articles_without_photo_table_widget.setMinimumSize(QtCore.QSize(1001, 0))
        self.articles_without_photo_table_widget.setObjectName("articles_without_photo_table_widget")
        self.articles_without_photo_table_widget.setColumnCount(0)
        self.articles_without_photo_table_widget.setRowCount(0)
        self.articles_without_photo_table_widget.horizontalHeader().setDefaultSectionSize(200)
        self.articles_without_photo_table_widget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_10.addWidget(self.articles_without_photo_table_widget)
        self.add_prepare_list_photo_push_button = QtWidgets.QPushButton(self.prepare_photo_archive_tab)
        self.add_prepare_list_photo_push_button.setObjectName("add_prepare_list_photo_push_button")
        self.verticalLayout_10.addWidget(self.add_prepare_list_photo_push_button)
        self.label_2 = QtWidgets.QLabel(self.prepare_photo_archive_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_10.addWidget(self.label_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.result_path_line_edit_2 = QtWidgets.QLineEdit(self.prepare_photo_archive_tab)
        self.result_path_line_edit_2.setObjectName("result_path_line_edit_2")
        self.horizontalLayout_7.addWidget(self.result_path_line_edit_2)
        self.add_photo_archive_path_push_button = QtWidgets.QPushButton(self.prepare_photo_archive_tab)
        self.add_photo_archive_path_push_button.setObjectName("add_photo_archive_path_push_button")
        self.horizontalLayout_7.addWidget(self.add_photo_archive_path_push_button)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.label_3 = QtWidgets.QLabel(self.prepare_photo_archive_tab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_10.addWidget(self.label_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.result_path_archive_line_edit = QtWidgets.QLineEdit(self.prepare_photo_archive_tab)
        self.result_path_archive_line_edit.setObjectName("result_path_archive_line_edit")
        self.horizontalLayout_8.addWidget(self.result_path_archive_line_edit)
        self.add_result_path_archive_push_button = QtWidgets.QPushButton(self.prepare_photo_archive_tab)
        self.add_result_path_archive_push_button.setObjectName("add_result_path_archive_push_button")
        self.horizontalLayout_8.addWidget(self.add_result_path_archive_push_button)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.start_prepare_result_archive_push_button = QtWidgets.QPushButton(self.prepare_photo_archive_tab)
        self.start_prepare_result_archive_push_button.setObjectName("start_prepare_result_archive_push_button")
        self.verticalLayout_10.addWidget(self.start_prepare_result_archive_push_button)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.tabWidget.addTab(self.prepare_photo_archive_tab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1027, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.parsing_parameters_action = QtWidgets.QAction(MainWindow)
        self.parsing_parameters_action.setObjectName("parsing_parameters_action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menuSettings.addAction(self.parsing_parameters_action)
        self.menuAbout.addAction(self.action_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Blue Cherry"))
        self.prepare_passport_label.setText(_translate("MainWindow", "Защита паспортов"))
        self.passport_tree_widget.headerItem().setText(0, _translate("MainWindow", "Расположение"))
        self.passport_tree_widget.headerItem().setText(1, _translate("MainWindow", "Файл"))
        self.passport_tree_widget.headerItem().setText(2, _translate("MainWindow", "Статус"))
        self.result_path_label.setText(_translate("MainWindow", "Путь, где будет создана папка с результатом"))
        self.set_result_path_push_button.setText(_translate("MainWindow", "Выбрать"))
        self.add_passport_files_push_button.setText(_translate("MainWindow", "Добавить файлы"))
        self.delete_selected_passport_file_push_button.setText(_translate("MainWindow", "Удалить выбранный"))
        self.start_passport_protection_push_button.setText(_translate("MainWindow", "Создать защищенные файлы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.prepare_passport_tab), _translate("MainWindow", "Защита паспортов"))
        self.manual_parser_label.setText(_translate("MainWindow", "Ручной парсинг прайсов"))
        self.test_push_button.setText(_translate("MainWindow", "test"))
        self.manual_parser_tree_widget.headerItem().setText(0, _translate("MainWindow", "Расположение"))
        self.manual_parser_tree_widget.headerItem().setText(1, _translate("MainWindow", "Файл"))
        self.manual_parser_tree_widget.headerItem().setText(2, _translate("MainWindow", "Поставщик"))
        self.add_price_push_button.setToolTip(_translate("MainWindow", "Для парсинга 1 файла"))
        self.add_price_push_button.setText(_translate("MainWindow", "Добавить"))
        self.add_multiple_price_push_button.setToolTip(_translate("MainWindow", "Для поставщиков из нескольких прайсов"))
        self.add_multiple_price_push_button.setText(_translate("MainWindow", "Добавить несколько файлов"))
        self.delete_price_push_button.setText(_translate("MainWindow", "Удалить"))
        self.start_parsing_push_button.setText(_translate("MainWindow", "Запустить"))
        self.auto_parser_label.setText(_translate("MainWindow", "Автоматический парсинг прайсов"))
        self.kvt_label.setText(_translate("MainWindow", "КВТ_СИТ - ссылка на xls файл"))
        self.parse_kvt_push_button.setText(_translate("MainWindow", "Спарсить КВТ_СИТ "))
        self.torg7_label.setText(_translate("MainWindow", "Торг7 - ссылка на xml файл"))
        self.parse_torg7_push_button.setText(_translate("MainWindow", "Спарсить Торг7_ЧК"))
        self.a4_label.setText(_translate("MainWindow", "А4_ИД - ссылка на xml файл"))
        self.parse_a4_push_button.setText(_translate("MainWindow", "Спарсить А4_ИД     "))
        self.label.setText(_translate("MainWindow", "Путь, где будут файлы  с результатом"))
        self.add_result_path_parser_push_button.setText(_translate("MainWindow", "Указать папку"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cheescake_parser_tab), _translate("MainWindow", "Парсинг для Cheescake"))
        self.add_prepare_list_photo_push_button.setText(_translate("MainWindow", "Добавить файл со списком артикулов без фото"))
        self.label_2.setText(_translate("MainWindow", "Укажите путь к архиву с фотографиями, где название папки = артикул"))
        self.add_photo_archive_path_push_button.setText(_translate("MainWindow", "Указать"))
        self.label_3.setText(_translate("MainWindow", "Укажите путь, где будет храниться архив с результатом"))
        self.add_result_path_archive_push_button.setText(_translate("MainWindow", "Указать"))
        self.start_prepare_result_archive_push_button.setText(_translate("MainWindow", "Подготовить архив"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.prepare_photo_archive_tab), _translate("MainWindow", "Подготовка фотоархива"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.parsing_parameters_action.setText(_translate("MainWindow", "Параметры парсинга"))
        self.action_2.setText(_translate("MainWindow", "О программе"))
