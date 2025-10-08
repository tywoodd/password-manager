# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entry_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QProgressBar, QSizePolicy, QSpacerItem, QTextEdit,
    QToolButton, QVBoxLayout, QWidget)
from . import resources_rc

class Ui_EntryEditorDialog(object):
    def setupUi(self, EntryEditorDialog):
        if not EntryEditorDialog.objectName():
            EntryEditorDialog.setObjectName(u"EntryEditorDialog")
        EntryEditorDialog.resize(848, 803)
        self.verticalLayout = QVBoxLayout(EntryEditorDialog)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.formContainer = QWidget(EntryEditorDialog)
        self.formContainer.setObjectName(u"formContainer")
        self.verticalLayout_2 = QVBoxLayout(self.formContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.titleLabel = QLabel(self.formContainer)
        self.titleLabel.setObjectName(u"titleLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.titleLabel)

        self.usernameLabel = QLabel(self.formContainer)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.usernameLabel)

        self.uRLLabel = QLabel(self.formContainer)
        self.uRLLabel.setObjectName(u"uRLLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.uRLLabel)

        self.passwordLabel = QLabel(self.formContainer)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.passwordLabel)

        self.passwordWidget = QWidget(self.formContainer)
        self.passwordWidget.setObjectName(u"passwordWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.passwordWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.passwordRow = QHBoxLayout()
        self.passwordRow.setObjectName(u"passwordRow")
        self.passwordEdit = QLineEdit(self.passwordWidget)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordEdit.setClearButtonEnabled(True)

        self.passwordRow.addWidget(self.passwordEdit)


        self.horizontalLayout_2.addLayout(self.passwordRow)

        self.togglePwdButton = QToolButton(self.passwordWidget)
        self.togglePwdButton.setObjectName(u"togglePwdButton")
        icon = QIcon()
        icon.addFile(u":/img/img/eye.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.togglePwdButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.togglePwdButton)

        self.generatePwdButton = QToolButton(self.passwordWidget)
        self.generatePwdButton.setObjectName(u"generatePwdButton")
        self.generatePwdButton.setMinimumSize(QSize(0, 25))
        icon1 = QIcon()
        icon1.addFile(u":/img/img/random.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.generatePwdButton.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.generatePwdButton)


        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.passwordWidget)

        self.strengthLabel = QLabel(self.formContainer)
        self.strengthLabel.setObjectName(u"strengthLabel")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.strengthLabel)

        self.strengthWidget = QWidget(self.formContainer)
        self.strengthWidget.setObjectName(u"strengthWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.strengthWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.progressBar = QProgressBar(self.strengthWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_3.addWidget(self.progressBar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.strengthWidget)

        self.notesLabel = QLabel(self.formContainer)
        self.notesLabel.setObjectName(u"notesLabel")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.notesLabel)

        self.notesWidget = QWidget(self.formContainer)
        self.notesWidget.setObjectName(u"notesWidget")
        self.horizontalLayout = QHBoxLayout(self.notesWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.notesEdit = QTextEdit(self.notesWidget)
        self.notesEdit.setObjectName(u"notesEdit")
        self.notesEdit.setMinimumSize(QSize(0, 375))

        self.horizontalLayout.addWidget(self.notesEdit)


        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.notesWidget)

        self.uRLWidget = QWidget(self.formContainer)
        self.uRLWidget.setObjectName(u"uRLWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.uRLWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.uRLEdit = QLineEdit(self.uRLWidget)
        self.uRLEdit.setObjectName(u"uRLEdit")

        self.horizontalLayout_4.addWidget(self.uRLEdit)


        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.uRLWidget)

        self.usernameWidget = QWidget(self.formContainer)
        self.usernameWidget.setObjectName(u"usernameWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.usernameWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.usernameEdit = QLineEdit(self.usernameWidget)
        self.usernameEdit.setObjectName(u"usernameEdit")

        self.horizontalLayout_5.addWidget(self.usernameEdit)


        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.usernameWidget)

        self.titleWidget = QWidget(self.formContainer)
        self.titleWidget.setObjectName(u"titleWidget")
        self.horizontalLayout_6 = QHBoxLayout(self.titleWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.titleEdit = QLineEdit(self.titleWidget)
        self.titleEdit.setObjectName(u"titleEdit")

        self.horizontalLayout_6.addWidget(self.titleEdit)


        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.titleWidget)

        self.retypePasswordLabel = QLabel(self.formContainer)
        self.retypePasswordLabel.setObjectName(u"retypePasswordLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.retypePasswordLabel)

        self.retypePasswordWidget = QWidget(self.formContainer)
        self.retypePasswordWidget.setObjectName(u"retypePasswordWidget")
        self.horizontalLayout_7 = QHBoxLayout(self.retypePasswordWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.retypePasswordEdit = QLineEdit(self.retypePasswordWidget)
        self.retypePasswordEdit.setObjectName(u"retypePasswordEdit")
        self.retypePasswordEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_7.addWidget(self.retypePasswordEdit)

        self.toolButton = QToolButton(self.retypePasswordWidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setIcon(icon)

        self.horizontalLayout_7.addWidget(self.toolButton)


        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.retypePasswordWidget)

        self.passwordHintLabel = QLabel(self.formContainer)
        self.passwordHintLabel.setObjectName(u"passwordHintLabel")
        self.passwordHintLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.passwordHintLabel)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.formContainer)

        self.buttonBox = QDialogButtonBox(EntryEditorDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(EntryEditorDialog)
        self.buttonBox.accepted.connect(EntryEditorDialog.accept)
        self.buttonBox.rejected.connect(EntryEditorDialog.reject)

        QMetaObject.connectSlotsByName(EntryEditorDialog)
    # setupUi

    def retranslateUi(self, EntryEditorDialog):
        EntryEditorDialog.setWindowTitle(QCoreApplication.translate("EntryEditorDialog", u"New Entry", None))
        self.titleLabel.setText(QCoreApplication.translate("EntryEditorDialog", u"Title", None))
        self.usernameLabel.setText(QCoreApplication.translate("EntryEditorDialog", u"Username", None))
        self.uRLLabel.setText(QCoreApplication.translate("EntryEditorDialog", u"URL", None))
        self.passwordLabel.setText(QCoreApplication.translate("EntryEditorDialog", u"Password", None))
#if QT_CONFIG(tooltip)
        self.togglePwdButton.setToolTip(QCoreApplication.translate("EntryEditorDialog", u"<html><head/><body><p>Show/Hide Password</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.togglePwdButton.setText("")
#if QT_CONFIG(tooltip)
        self.generatePwdButton.setToolTip(QCoreApplication.translate("EntryEditorDialog", u"<html><head/><body><p>Generate Password</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.generatePwdButton.setText("")
        self.strengthLabel.setText("")
        self.progressBar.setFormat(QCoreApplication.translate("EntryEditorDialog", u"( Weak )", None))
        self.notesLabel.setText(QCoreApplication.translate("EntryEditorDialog", u"Notes", None))
        self.retypePasswordLabel.setText(QCoreApplication.translate("EntryEditorDialog", u"Retype Password", None))
        self.toolButton.setText("")
        self.passwordHintLabel.setText("")
    # retranslateUi

