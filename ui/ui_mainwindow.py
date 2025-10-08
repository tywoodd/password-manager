# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTableView, QToolBar, QVBoxLayout, QWidget)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1117, 895)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.actionNew.setIcon(icon)
        self.actionNew.setMenuRole(QAction.MenuRole.NoRole)
        self.actionEdit = QAction(MainWindow)
        self.actionEdit.setObjectName(u"actionEdit")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditCopy))
        self.actionEdit.setIcon(icon1)
        self.actionEdit.setMenuRole(QAction.MenuRole.NoRole)
        self.actionLock = QAction(MainWindow)
        self.actionLock.setObjectName(u"actionLock")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemLockScreen))
        self.actionLock.setIcon(icon2)
        self.actionLock.setMenuRole(QAction.MenuRole.NoRole)
        self.action_Delete = QAction(MainWindow)
        self.action_Delete.setObjectName(u"action_Delete")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.action_Delete.setIcon(icon3)
        self.action_Delete.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageLocked = QWidget()
        self.pageLocked.setObjectName(u"pageLocked")
        self.lockedPanel = QWidget(self.pageLocked)
        self.lockedPanel.setObjectName(u"lockedPanel")
        self.lockedPanel.setGeometry(QRect(39, 19, 1051, 791))
        self.verticalLayout_4 = QVBoxLayout(self.lockedPanel)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(738, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.lockIconLabel = QLabel(self.lockedPanel)
        self.lockIconLabel.setObjectName(u"lockIconLabel")
        self.lockIconLabel.setAutoFillBackground(False)
        self.lockIconLabel.setStyleSheet(u"transparent;")
        self.lockIconLabel.setPixmap(QPixmap(u":/img/img/lock.png"))
        self.lockIconLabel.setScaledContents(False)
        self.lockIconLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.lockIconLabel)

        self.unlockHintLabel = QLabel(self.lockedPanel)
        self.unlockHintLabel.setObjectName(u"unlockHintLabel")
        self.unlockHintLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.unlockHintLabel)

        self.passwordRow = QWidget(self.lockedPanel)
        self.passwordRow.setObjectName(u"passwordRow")
        self.horizontalLayout_2 = QHBoxLayout(self.passwordRow)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.passwordLabel = QLabel(self.passwordRow)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.passwordLabel)

        self.passwordEdit = QLineEdit(self.passwordRow)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_2.addWidget(self.passwordEdit)


        self.verticalLayout_4.addWidget(self.passwordRow)

        self.unlockButton = QPushButton(self.lockedPanel)
        self.unlockButton.setObjectName(u"unlockButton")

        self.verticalLayout_4.addWidget(self.unlockButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.pageLocked)
        self.pageVault = QWidget()
        self.pageVault.setObjectName(u"pageVault")
        self.vaultPanel = QWidget(self.pageVault)
        self.vaultPanel.setObjectName(u"vaultPanel")
        self.vaultPanel.setGeometry(QRect(0, 0, 1091, 791))
        self.verticalLayout_2 = QVBoxLayout(self.vaultPanel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.entriesPanel = QWidget(self.vaultPanel)
        self.entriesPanel.setObjectName(u"entriesPanel")
        self.verticalLayout_3 = QVBoxLayout(self.entriesPanel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.searchRow = QWidget(self.entriesPanel)
        self.searchRow.setObjectName(u"searchRow")
        self.horizontalLayout = QHBoxLayout(self.searchRow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.searchEdit = QLineEdit(self.searchRow)
        self.searchEdit.setObjectName(u"searchEdit")

        self.horizontalLayout.addWidget(self.searchEdit)

        self.searchButton = QPushButton(self.searchRow)
        self.searchButton.setObjectName(u"searchButton")

        self.horizontalLayout.addWidget(self.searchButton)


        self.verticalLayout_3.addWidget(self.searchRow)

        self.entriesTable = QTableView(self.entriesPanel)
        self.entriesTable.setObjectName(u"entriesTable")
        self.entriesTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.entriesTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.entriesTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.entriesTable.horizontalHeader().setDefaultSectionSize(150)
        self.entriesTable.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.entriesTable)


        self.verticalLayout_2.addWidget(self.entriesPanel)

        self.stackedWidget.addWidget(self.pageVault)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionEdit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Delete)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionLock)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Vault", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"&New", None))
        self.actionEdit.setText(QCoreApplication.translate("MainWindow", u"&Edit", None))
        self.actionLock.setText(QCoreApplication.translate("MainWindow", u"&Lock", None))
        self.action_Delete.setText(QCoreApplication.translate("MainWindow", u"&Delete", None))
        self.lockIconLabel.setText("")
        self.unlockHintLabel.setText("")
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Master Password", None))
        self.passwordEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter master password", None))
        self.unlockButton.setText(QCoreApplication.translate("MainWindow", u"Unlock", None))
        self.searchEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search title/username/url\u2026", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

