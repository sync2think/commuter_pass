# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QPushButton,
    QSizePolicy, QWidget)

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(507, 403)
        self.widget = QWidget(dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(390, 20, 82, 86))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pBtnEnd = QPushButton(self.widget)
        self.pBtnEnd.setObjectName(u"pBtnEnd")

        self.gridLayout.addWidget(self.pBtnEnd, 0, 0, 1, 1)

        self.pBtnExcel = QPushButton(self.widget)
        self.pBtnExcel.setObjectName(u"pBtnExcel")

        self.gridLayout.addWidget(self.pBtnExcel, 1, 0, 1, 1)

        self.pBtnDone = QPushButton(self.widget)
        self.pBtnDone.setObjectName(u"pBtnDone")

        self.gridLayout.addWidget(self.pBtnDone, 2, 0, 1, 1)


        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"\u5b9a\u671f\u4ee3", None))
        self.pBtnEnd.setText(QCoreApplication.translate("dialog", u"\u7d42\u4e86", None))
        self.pBtnExcel.setText(QCoreApplication.translate("dialog", u"\u30a8\u30af\u30bb\u30eb\u30d5\u30a1\u30a4\u30eb", None))
        self.pBtnDone.setText(QCoreApplication.translate("dialog", u"\u5b9f\u884c", None))
    # retranslateUi

