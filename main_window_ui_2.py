# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/main_window_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 776)
        MainWindow.setWindowTitle("TRGB - Color Estimate")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.main_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.main_tabs.setEnabled(True)
        self.main_tabs.setAutoFillBackground(False)
        self.main_tabs.setTabPosition(QtWidgets.QTabWidget.West)
        self.main_tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.main_tabs.setElideMode(QtCore.Qt.ElideNone)
        self.main_tabs.setUsesScrollButtons(True)
        self.main_tabs.setDocumentMode(False)
        self.main_tabs.setTabsClosable(False)
        self.main_tabs.setMovable(False)
        self.main_tabs.setTabBarAutoHide(True)
        self.main_tabs.setObjectName("main_tabs")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.group_chosing_file = QtWidgets.QGroupBox(self.tab_1)
        self.group_chosing_file.setObjectName("group_chosing_file")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.group_chosing_file)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_descr_chosing_file = QtWidgets.QLabel(self.group_chosing_file)
        self.label_descr_chosing_file.setObjectName("label_descr_chosing_file")
        self.verticalLayout.addWidget(self.label_descr_chosing_file)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_chose_file = QtWidgets.QPushButton(self.group_chosing_file)
        self.button_chose_file.setObjectName("button_chose_file")
        self.horizontalLayout.addWidget(self.button_chose_file)
        self.label_filename = QtWidgets.QLabel(self.group_chosing_file)
        self.label_filename.setObjectName("label_filename")
        self.horizontalLayout.addWidget(self.label_filename)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.button_view_chosen = QtWidgets.QPushButton(self.group_chosing_file)
        self.button_view_chosen.setEnabled(False)
        self.button_view_chosen.setObjectName("button_view_chosen")
        self.verticalLayout.addWidget(self.button_view_chosen)
        self.verticalLayout_2.addWidget(self.group_chosing_file)
        self.group_clearing = QtWidgets.QGroupBox(self.tab_1)
        self.group_clearing.setEnabled(False)
        self.group_clearing.setObjectName("group_clearing")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.group_clearing)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.button_clearing = QtWidgets.QPushButton(self.group_clearing)
        self.button_clearing.setCheckable(False)
        self.button_clearing.setChecked(False)
        self.button_clearing.setObjectName("button_clearing")
        self.horizontalLayout_7.addWidget(self.button_clearing)
        self.button_view_clearing = QtWidgets.QPushButton(self.group_clearing)
        self.button_view_clearing.setEnabled(False)
        self.button_view_clearing.setObjectName("button_view_clearing")
        self.horizontalLayout_7.addWidget(self.button_view_clearing)
        self.verticalLayout_2.addWidget(self.group_clearing)
        self.group_masking = QtWidgets.QGroupBox(self.tab_1)
        self.group_masking.setEnabled(False)
        self.group_masking.setObjectName("group_masking")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.group_masking)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_masking = QtWidgets.QPushButton(self.group_masking)
        self.button_masking.setObjectName("button_masking")
        self.horizontalLayout_3.addWidget(self.button_masking)
        self.button_view_masking = QtWidgets.QPushButton(self.group_masking)
        self.button_view_masking.setEnabled(False)
        self.button_view_masking.setCheckable(False)
        self.button_view_masking.setObjectName("button_view_masking")
        self.horizontalLayout_3.addWidget(self.button_view_masking)
        self.verticalLayout_2.addWidget(self.group_masking)
        self.group_distance = QtWidgets.QGroupBox(self.tab_1)
        self.group_distance.setEnabled(False)
        self.group_distance.setObjectName("group_distance")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.group_distance)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.group_distance)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_mags = QtWidgets.QWidget()
        self.tab_mags.setObjectName("tab_mags")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_mags)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.tab_mags)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.enter_mags = QtWidgets.QDoubleSpinBox(self.tab_mags)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_mags.setFont(font)
        self.enter_mags.setDecimals(3)
        self.enter_mags.setSingleStep(1.0)
        self.enter_mags.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.enter_mags.setObjectName("enter_mags")
        self.horizontalLayout_6.addWidget(self.enter_mags, 0, QtCore.Qt.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.tabWidget_3.addTab(self.tab_mags, "")
        self.tab_mpcs = QtWidgets.QWidget()
        self.tab_mpcs.setObjectName("tab_mpcs")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_mpcs)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.label_9 = QtWidgets.QLabel(self.tab_mpcs)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.enter_mpcs = QtWidgets.QDoubleSpinBox(self.tab_mpcs)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_mpcs.setFont(font)
        self.enter_mpcs.setPrefix("")
        self.enter_mpcs.setDecimals(3)
        self.enter_mpcs.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.enter_mpcs.setObjectName("enter_mpcs")
        self.horizontalLayout_8.addWidget(self.enter_mpcs)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.tabWidget_3.addTab(self.tab_mpcs, "")
        self.verticalLayout_4.addWidget(self.tabWidget_3)
        self.buttons_distance = QtWidgets.QDialogButtonBox(self.group_distance)
        self.buttons_distance.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttons_distance.setObjectName("buttons_distance")
        self.verticalLayout_4.addWidget(self.buttons_distance)
        self.verticalLayout_2.addWidget(self.group_distance)
        self.group_reddening = QtWidgets.QGroupBox(self.tab_1)
        self.group_reddening.setEnabled(False)
        self.group_reddening.setCheckable(False)
        self.group_reddening.setChecked(False)
        self.group_reddening.setObjectName("group_reddening")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.group_reddening)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.group_reddening)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_auto = QtWidgets.QWidget()
        self.tab_auto.setObjectName("tab_auto")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_auto)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_absorbtion = QtWidgets.QLabel(self.tab_auto)
        self.label_absorbtion.setObjectName("label_absorbtion")
        self.gridLayout_3.addWidget(self.label_absorbtion, 3, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label_11 = QtWidgets.QLabel(self.tab_auto)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.enter_coef_1 = QtWidgets.QDoubleSpinBox(self.tab_auto)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_coef_1.setFont(font)
        self.enter_coef_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.enter_coef_1.setDecimals(3)
        self.enter_coef_1.setSingleStep(1.0)
        self.enter_coef_1.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.enter_coef_1.setProperty("value", 2.742)
        self.enter_coef_1.setObjectName("enter_coef_1")
        self.horizontalLayout_4.addWidget(self.enter_coef_1)
        self.label_10 = QtWidgets.QLabel(self.tab_auto)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.label_redshift = QtWidgets.QLabel(self.tab_auto)
        self.label_redshift.setObjectName("label_redshift")
        self.gridLayout_3.addWidget(self.label_redshift, 2, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.label_13 = QtWidgets.QLabel(self.tab_auto)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.enter_coef_2 = QtWidgets.QDoubleSpinBox(self.tab_auto)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_coef_2.setFont(font)
        self.enter_coef_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.enter_coef_2.setDecimals(3)
        self.enter_coef_2.setSingleStep(1.0)
        self.enter_coef_2.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.enter_coef_2.setProperty("value", 1.505)
        self.enter_coef_2.setObjectName("enter_coef_2")
        self.horizontalLayout_5.addWidget(self.enter_coef_2)
        self.label_8 = QtWidgets.QLabel(self.tab_auto)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.label_7 = QtWidgets.QLabel(self.tab_auto)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.enter_b_minus_v = QtWidgets.QDoubleSpinBox(self.tab_auto)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_b_minus_v.setFont(font)
        self.enter_b_minus_v.setDecimals(3)
        self.enter_b_minus_v.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.enter_b_minus_v.setObjectName("enter_b_minus_v")
        self.horizontalLayout_10.addWidget(self.enter_b_minus_v)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 0, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_auto, "")
        self.tab_manual = QtWidgets.QWidget()
        self.tab_manual.setObjectName("tab_manual")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_manual)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.tab_manual)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_manual)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        self.enter_redshift = QtWidgets.QDoubleSpinBox(self.tab_manual)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_redshift.setFont(font)
        self.enter_redshift.setDecimals(3)
        self.enter_redshift.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.enter_redshift.setObjectName("enter_redshift")
        self.gridLayout_2.addWidget(self.enter_redshift, 0, 2, 1, 1)
        self.enter_absorbtion = QtWidgets.QDoubleSpinBox(self.tab_manual)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_absorbtion.setFont(font)
        self.enter_absorbtion.setDecimals(3)
        self.enter_absorbtion.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.enter_absorbtion.setObjectName("enter_absorbtion")
        self.gridLayout_2.addWidget(self.enter_absorbtion, 1, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_manual, "Вручную")
        self.verticalLayout_3.addWidget(self.tabWidget_2)
        self.buttons_reddening = QtWidgets.QDialogButtonBox(self.group_reddening)
        self.buttons_reddening.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttons_reddening.setObjectName("buttons_reddening")
        self.verticalLayout_3.addWidget(self.buttons_reddening)
        self.verticalLayout_2.addWidget(self.group_reddening)
        self.bottom_tab_1 = QtWidgets.QHBoxLayout()
        self.bottom_tab_1.setObjectName("bottom_tab_1")
        self.button_final_view = QtWidgets.QPushButton(self.tab_1)
        self.button_final_view.setObjectName("button_final_view")
        self.bottom_tab_1.addWidget(self.button_final_view)
        self.button_next_tab = QtWidgets.QPushButton(self.tab_1)
        self.button_next_tab.setEnabled(False)
        self.button_next_tab.setObjectName("button_next_tab")
        self.bottom_tab_1.addWidget(self.button_next_tab)
        self.verticalLayout_2.addLayout(self.bottom_tab_1)
        self.main_tabs.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.group_spatial = QtWidgets.QGroupBox(self.tab_2)
        self.group_spatial.setObjectName("group_spatial")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.group_spatial)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_i = QtWidgets.QLabel(self.group_spatial)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_i.setFont(font)
        self.label_i.setObjectName("label_i")
        self.gridLayout_10.addWidget(self.label_i, 2, 2, 1, 1)
        self.enter_vi_left = QtWidgets.QDoubleSpinBox(self.group_spatial)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_vi_left.setFont(font)
        self.enter_vi_left.setDecimals(2)
        self.enter_vi_left.setMinimum(-3.0)
        self.enter_vi_left.setMaximum(10.0)
        self.enter_vi_left.setSingleStep(0.1)
        self.enter_vi_left.setProperty("value", 0.7)
        self.enter_vi_left.setObjectName("enter_vi_left")
        self.gridLayout_10.addWidget(self.enter_vi_left, 1, 1, 1, 1)
        self.enter_vi_right = QtWidgets.QDoubleSpinBox(self.group_spatial)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_vi_right.setFont(font)
        self.enter_vi_right.setDecimals(2)
        self.enter_vi_right.setMinimum(-3.0)
        self.enter_vi_right.setMaximum(10.0)
        self.enter_vi_right.setSingleStep(0.1)
        self.enter_vi_right.setProperty("value", 1.7)
        self.enter_vi_right.setObjectName("enter_vi_right")
        self.gridLayout_10.addWidget(self.enter_vi_right, 1, 3, 1, 1)
        self.enter_i_left = QtWidgets.QDoubleSpinBox(self.group_spatial)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_i_left.setFont(font)
        self.enter_i_left.setDecimals(2)
        self.enter_i_left.setMinimum(-3.0)
        self.enter_i_left.setMaximum(10.0)
        self.enter_i_left.setSingleStep(0.1)
        self.enter_i_left.setProperty("value", 2.0)
        self.enter_i_left.setObjectName("enter_i_left")
        self.gridLayout_10.addWidget(self.enter_i_left, 2, 1, 1, 1)
        self.label_vi = QtWidgets.QLabel(self.group_spatial)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_vi.setFont(font)
        self.label_vi.setObjectName("label_vi")
        self.gridLayout_10.addWidget(self.label_vi, 1, 2, 1, 1)
        self.enter_i_right = QtWidgets.QDoubleSpinBox(self.group_spatial)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_i_right.setFont(font)
        self.enter_i_right.setDecimals(2)
        self.enter_i_right.setMinimum(-3.0)
        self.enter_i_right.setMaximum(10.0)
        self.enter_i_right.setSingleStep(0.1)
        self.enter_i_right.setProperty("value", 4.2)
        self.enter_i_right.setObjectName("enter_i_right")
        self.gridLayout_10.addWidget(self.enter_i_right, 2, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem10, 1, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem11, 1, 4, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_10)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.enter_p = QtWidgets.QDoubleSpinBox(self.group_spatial)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_p.setFont(font)
        self.enter_p.setDecimals(1)
        self.enter_p.setMaximum(100.0)
        self.enter_p.setProperty("value", 100.0)
        self.enter_p.setObjectName("enter_p")
        self.gridLayout_11.addWidget(self.enter_p, 0, 2, 1, 1)
        self.label_p = QtWidgets.QLabel(self.group_spatial)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_p.setFont(font)
        self.label_p.setObjectName("label_p")
        self.gridLayout_11.addWidget(self.label_p, 0, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem12, 0, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem13, 0, 3, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_11)
        self.button_view_spatial = QtWidgets.QPushButton(self.group_spatial)
        self.button_view_spatial.setObjectName("button_view_spatial")
        self.verticalLayout_5.addWidget(self.button_view_spatial)
        self.gridLayout_4.addWidget(self.group_spatial, 2, 0, 1, 1)
        self.group_distance_2 = QtWidgets.QGroupBox(self.tab_2)
        self.group_distance_2.setObjectName("group_distance_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.group_distance_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem14, 0, 3, 1, 1)
        self.label_d_plus = QtWidgets.QLabel(self.group_distance_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_d_plus.setFont(font)
        self.label_d_plus.setObjectName("label_d_plus")
        self.gridLayout_5.addWidget(self.label_d_plus, 0, 1, 1, 1)
        self.enter_d_plus = QtWidgets.QDoubleSpinBox(self.group_distance_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_d_plus.setFont(font)
        self.enter_d_plus.setSuffix("")
        self.enter_d_plus.setDecimals(2)
        self.enter_d_plus.setSingleStep(0.01)
        self.enter_d_plus.setObjectName("enter_d_plus")
        self.gridLayout_5.addWidget(self.enter_d_plus, 0, 2, 1, 1)
        self.label_d_minus = QtWidgets.QLabel(self.group_distance_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_d_minus.setFont(font)
        self.label_d_minus.setObjectName("label_d_minus")
        self.gridLayout_5.addWidget(self.label_d_minus, 1, 1, 1, 1)
        self.enter_d_minus = QtWidgets.QDoubleSpinBox(self.group_distance_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_d_minus.setFont(font)
        self.enter_d_minus.setDecimals(2)
        self.enter_d_minus.setSingleStep(0.01)
        self.enter_d_minus.setObjectName("enter_d_minus")
        self.gridLayout_5.addWidget(self.enter_d_minus, 1, 2, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem15, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.group_distance_2, 1, 0, 1, 1)
        self.group_saving = QtWidgets.QGroupBox(self.tab_2)
        self.group_saving.setObjectName("group_saving")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.group_saving)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.button_save = QtWidgets.QPushButton(self.group_saving)
        self.button_save.setObjectName("button_save")
        self.gridLayout_12.addWidget(self.button_save, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.group_saving, 3, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem16, 4, 0, 1, 1)
        self.text_fewstars = QtWidgets.QTextBrowser(self.tab_2)
        self.text_fewstars.setObjectName("text_fewstars")
        self.gridLayout_4.addWidget(self.text_fewstars, 0, 0, 1, 1)
        self.main_tabs.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.main_tabs.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.main_tabs, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main_tabs.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.group_chosing_file.setTitle(_translate("MainWindow", "Выбор файла"))
        self.label_descr_chosing_file.setText(_translate("MainWindow", "<html><head/><body><p>Файл фотометрии должен представлять из себя<span style=\" font-weight:600;\"> .csv </span>файл с определёнными колонками.</p></body></html>"))
        self.button_chose_file.setText(_translate("MainWindow", "Выбор файла"))
        self.label_filename.setText(_translate("MainWindow", " na"))
        self.button_view_chosen.setText(_translate("MainWindow", "Предварительный просмотр"))
        self.group_clearing.setTitle(_translate("MainWindow", "Очистка фотометрии"))
        self.button_clearing.setText(_translate("MainWindow", "Критерии"))
        self.button_view_clearing.setText(_translate("MainWindow", "Просмотр"))
        self.group_masking.setTitle(_translate("MainWindow", "Добавление маски"))
        self.button_masking.setText(_translate("MainWindow", "Маска"))
        self.button_view_masking.setText(_translate("MainWindow", "Просмотр"))
        self.group_distance.setTitle(_translate("MainWindow", "Расстояние"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt;\">D </span><span style=\" font-size:14pt; vertical-align:super;\">[m]</span><span style=\" font-size:14pt;\"> = </span></p></body></html>"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_mags), _translate("MainWindow", "В звёздных величинах"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">D </span><span style=\" font-size:14pt; vertical-align:sub;\">[Mpc]</span><span style=\" font-size:14pt;\"> = </span></p></body></html>"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_mpcs), _translate("MainWindow", "В мегапарсеках"))
        self.group_reddening.setTitle(_translate("MainWindow", "Покраснение"))
        self.label_absorbtion.setText(_translate("MainWindow", "nan"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">redshift (V-I) = </p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">× ( B - V ) = </p></body></html>"))
        self.label_redshift.setText(_translate("MainWindow", "nan"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">absorbtion (I) = </p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">× ( B - V ) = </p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">( B - V ) = </p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_auto), _translate("MainWindow", "Через (B-V)"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">redshift (V-I) = </p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">absorbtion (I) =</p></body></html>"))
        self.button_final_view.setText(_translate("MainWindow", "Просмотр"))
        self.button_next_tab.setText(_translate("MainWindow", "Следующий этап"))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.tab_1), _translate("MainWindow", "Этап 1"))
        self.group_spatial.setTitle(_translate("MainWindow", "Выделение ветви"))
        self.label_i.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">≤ I <span style=\" vertical-align:super;\">m</span> ≤ </p></body></html>"))
        self.label_vi.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">≤ (V-I) <span style=\" vertical-align:super;\">m</span> ≤ </p></body></html>"))
        self.enter_p.setSuffix(_translate("MainWindow", "%"))
        self.label_p.setText(_translate("MainWindow", "P = "))
        self.button_view_spatial.setText(_translate("MainWindow", "Просмотр"))
        self.group_distance_2.setTitle(_translate("MainWindow", "Ошибка в определении расстояния (в звёздных величинах)"))
        self.label_d_plus.setText(_translate("MainWindow", "<html><head/><body><p> δ<span style=\" vertical-align:sub;\">+</span> D<span style=\" vertical-align:super;\">m</span> = </p></body></html>"))
        self.label_d_minus.setText(_translate("MainWindow", "<html><head/><body><p> δ<span style=\" vertical-align:sub;\">-</span> D<span style=\" vertical-align:super;\">m</span> = </p></body></html>"))
        self.group_saving.setTitle(_translate("MainWindow", "Сохранение результата"))
        self.button_save.setText(_translate("MainWindow", "Сохранить [pdf]"))
        self.text_fewstars.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Выделение ветви красных гигантов вручную и аппроксимация её кривой. Рекомендуется для слабонаселённых ветвей.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Ввод доверительного интервала для расстояния (в звёздных величинах):</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">D<span style=\" vertical-align:sub;\">real</span>∈(D <span style=\" font-family:\'Nimbus Roman No9 L\',\'Times New Roman\',\'Times\',\'serif\'; font-weight:704; color:#202122; background-color:#ffffff;\">−</span> δ<span style=\" vertical-align:sub;\">-</span> D; D + δ<span style=\" vertical-align:sub;\">+</span> D)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. Выбор границ ветви (в плоскости цвет-величина). Показатель цвета (V-I) и величина I.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. Доля звёзд, которые использовать в аппроксимации. (100 - P)% звёзд будут отброшены как выбросы. Для относительно чистых диаграмм разумное значение в диапазоне 95-100%, для засорённых может быть ниже. </p></body></html>"))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.tab_2), _translate("MainWindow", "Этап 2"))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.tab_3), _translate("MainWindow", "Этап 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
