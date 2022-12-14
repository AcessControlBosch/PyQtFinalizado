# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manutencao.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Manutencao(object):
    def setupUi(self, Manutencao):
        Manutencao.setObjectName("Manutencao")
        Manutencao.resize(1290, 841)
        Manutencao.setMinimumSize(QtCore.QSize(1290, 841))
        Manutencao.setMaximumSize(QtCore.QSize(1290, 841))
        Manutencao.setStyleSheet("background-color: rgb(255, 255, 255);")
        Manutencao.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(Manutencao)
        self.centralwidget.setObjectName("centralwidget")
        self.Label_Borda = QtWidgets.QLabel(self.centralwidget)
        self.Label_Borda.setGeometry(QtCore.QRect(0, 783, 1290, 18))
        self.Label_Borda.setText("")
        self.Label_Borda.setPixmap(QtGui.QPixmap("imagens/Borda.png"))
        self.Label_Borda.setScaledContents(True)
        self.Label_Borda.setObjectName("Label_Borda")
        self.label_fundo = QtWidgets.QLabel(self.centralwidget)
        self.label_fundo.setGeometry(QtCore.QRect(20, 10, 1251, 761))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans Bold")
        font.setPointSize(65)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_fundo.setFont(font)
        self.label_fundo.setStyleSheet("border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:7px;\n"
"border-radius: 0px;\n"
"background-color: rgb(208, 212, 216);")
        self.label_fundo.setText("")
        self.label_fundo.setObjectName("label_fundo")
        self.botao_home = QtWidgets.QPushButton(self.centralwidget)
        self.botao_home.setGeometry(QtCore.QRect(1120, 10, 151, 141))
        self.botao_home.setStyleSheet("border-style: outset;\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:6px;\n"
"\n"
"\n"
"font: 75 34pt \"Bosch Sans Bold\";\n"
"background-color: rgb(255,207,0);")
        self.botao_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagens/home_preto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_home.setIcon(icon)
        self.botao_home.setIconSize(QtCore.QSize(130, 130))
        self.botao_home.setObjectName("botao_home")
        self.label_manutencao = QtWidgets.QLabel(self.centralwidget)
        self.label_manutencao.setGeometry(QtCore.QRect(20, 10, 1111, 141))
        self.label_manutencao.setStyleSheet("font: 75 52pt \"Bosch Sans Bold\";\n"
"border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:6px;\n"
"background-color: rgb(255,207,0);")
        self.label_manutencao.setAlignment(QtCore.Qt.AlignCenter)
        self.label_manutencao.setObjectName("label_manutencao")
        self.label_fundo_painel = QtWidgets.QLabel(self.centralwidget)
        self.label_fundo_painel.setGeometry(QtCore.QRect(60, 370, 431, 371))
        self.label_fundo_painel.setStyleSheet("border-style: outset;\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:6px;\n"
"border-radius: 90px;\n"
"\n"
"font: 75 34pt \"Bosch Sans Bold\";\n"
"background-color: rgb(138, 144, 151);")
        self.label_fundo_painel.setText("")
        self.label_fundo_painel.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fundo_painel.setObjectName("label_fundo_painel")
        self.label_raio = QtWidgets.QLabel(self.centralwidget)
        self.label_raio.setGeometry(QtCore.QRect(100, 500, 181, 181))
        self.label_raio.setStyleSheet("border-style: outset;\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:6px;\n"
"\n"
"\n"
"font: 75 34pt \"Bosch Sans Bold\";\n"
"background-color: rgb(255,255,255);")
        self.label_raio.setText("")
        self.label_raio.setPixmap(QtGui.QPixmap("imagens/Raio.png"))
        self.label_raio.setScaledContents(True)
        self.label_raio.setObjectName("label_raio")
        self.botao_liberar_trava2 = QtWidgets.QPushButton(self.centralwidget)
        self.botao_liberar_trava2.setGeometry(QtCore.QRect(1095, 180, 151, 151))
        self.botao_liberar_trava2.setStyleSheet("border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:7px;\n"
"border-radius: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.botao_liberar_trava2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imagens/Touch_painel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_liberar_trava2.setIcon(icon1)
        self.botao_liberar_trava2.setIconSize(QtCore.QSize(120, 120))
        self.botao_liberar_trava2.setObjectName("botao_liberar_trava2")
        self.label_painel_eletrico = QtWidgets.QLabel(self.centralwidget)
        self.label_painel_eletrico.setGeometry(QtCore.QRect(90, 400, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans Bold")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_painel_eletrico.setFont(font)
        self.label_painel_eletrico.setStyleSheet("\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"\n"
"border-radius: 90px;\n"
"\n"
"font: 75 28pt \"Bosch Sans Bold\";\n"
"background-color: rgb(138, 144, 151);")
        self.label_painel_eletrico.setAlignment(QtCore.Qt.AlignCenter)
        self.label_painel_eletrico.setObjectName("label_painel_eletrico")
        self.label_solenoide = QtWidgets.QLabel(self.centralwidget)
        self.label_solenoide.setGeometry(QtCore.QRect(330, 550, 81, 51))
        self.label_solenoide.setStyleSheet("border-style: outset;\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:6px;\n"
"border-radius: 0px;\n"
"\n"
"font: 75 34pt \"Bosch Sans Bold\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_solenoide.setText("")
        self.label_solenoide.setAlignment(QtCore.Qt.AlignCenter)
        self.label_solenoide.setObjectName("label_solenoide")
        self.label_trava_solenoide = QtWidgets.QLabel(self.centralwidget)
        self.label_trava_solenoide.setGeometry(QtCore.QRect(370, 565, 91, 20))
        self.label_trava_solenoide.setStyleSheet("border-style: outset;\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:6px;\n"
"border-radius: 0px;\n"
"\n"
"font: 75 34pt \"Bosch Sans Bold\";\n"
"background-color: rgb(237, 0, 7);")
        self.label_trava_solenoide.setText("")
        self.label_trava_solenoide.setAlignment(QtCore.Qt.AlignCenter)
        self.label_trava_solenoide.setObjectName("label_trava_solenoide")
        self.label__abertura = QtWidgets.QLabel(self.centralwidget)
        self.label__abertura.setGeometry(QtCore.QRect(430, 530, 51, 91))
        self.label__abertura.setStyleSheet("border-style: outset;\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:6px;\n"
"border-radius: 20px;\n"
"\n"
"font: 75 34pt \"Bosch Sans Bold\";\n"
"background-color: rgb(255, 255, 255);")
        self.label__abertura.setText("")
        self.label__abertura.setAlignment(QtCore.Qt.AlignCenter)
        self.label__abertura.setObjectName("label__abertura")
        self.botao_liberar_trava1 = QtWidgets.QPushButton(self.centralwidget)
        self.botao_liberar_trava1.setGeometry(QtCore.QRect(680, 200, 421, 111))
        self.botao_liberar_trava1.setStyleSheet("border-style: outset;\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:6px;\n"
"border-radius: 0px;\n"
"\n"
"font: 75 24pt \"Bosch Sans Bold\";\n"
"background-color: rgb(155, 228, 179);")
        self.botao_liberar_trava1.setIconSize(QtCore.QSize(120, 120))
        self.botao_liberar_trava1.setObjectName("botao_liberar_trava1")
        self.botao_energizar_contator_2 = QtWidgets.QPushButton(self.centralwidget)
        self.botao_energizar_contator_2.setGeometry(QtCore.QRect(465, 180, 151, 151))
        self.botao_energizar_contator_2.setStyleSheet("border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:7px;\n"
"border-radius: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.botao_energizar_contator_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imagens/Raio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_energizar_contator_2.setIcon(icon2)
        self.botao_energizar_contator_2.setIconSize(QtCore.QSize(125, 125))
        self.botao_energizar_contator_2.setObjectName("botao_energizar_contator_2")
        self.botao_energizar_contator_1 = QtWidgets.QPushButton(self.centralwidget)
        self.botao_energizar_contator_1.setGeometry(QtCore.QRect(50, 200, 421, 111))
        self.botao_energizar_contator_1.setStyleSheet("border-style: outset;\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:6px;\n"
"border-radius: 0px;\n"
"\n"
"font: 75 24pt \"Bosch Sans Bold\";\n"
"background-color: rgb(155, 228, 179);")
        self.botao_energizar_contator_1.setIconSize(QtCore.QSize(120, 120))
        self.botao_energizar_contator_1.setObjectName("botao_energizar_contator_1")
        self.botao_maquina_manutencao = QtWidgets.QPushButton(self.centralwidget)
        self.botao_maquina_manutencao.setGeometry(QtCore.QRect(790, 500, 401, 211))
        self.botao_maquina_manutencao.setStyleSheet("border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:7px;\n"
"border-radius: 0px;\n"
"background-color: rgb(113, 118, 124);")
        self.botao_maquina_manutencao.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imagens/botao_estado_manutencao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_maquina_manutencao.setIcon(icon3)
        self.botao_maquina_manutencao.setIconSize(QtCore.QSize(600, 600))
        self.botao_maquina_manutencao.setObjectName("botao_maquina_manutencao")
        self.label_maquina_em_manutencao = QtWidgets.QLabel(self.centralwidget)
        self.label_maquina_em_manutencao.setGeometry(QtCore.QRect(580, 405, 611, 101))
        self.label_maquina_em_manutencao.setStyleSheet("border-style: outset;\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:6px;\n"
"border-radius: 0px;\n"
"\n"
"font: 75 30pt \"Bosch Sans Bold\";\n"
"background-color: rgb(255,207,0);")
        self.label_maquina_em_manutencao.setAlignment(QtCore.Qt.AlignCenter)
        self.label_maquina_em_manutencao.setObjectName("label_maquina_em_manutencao")
        self.label_sim_nao = QtWidgets.QLabel(self.centralwidget)
        self.label_sim_nao.setGeometry(QtCore.QRect(580, 500, 221, 211))
        self.label_sim_nao.setStyleSheet("border-style: outset;\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:6px;\n"
"border-radius: 0px;\n"
"\n"
"font: 75 55pt \"Bosch Sans Bold\";\n"
"background-color: rgb(237, 0, 7);")
        self.label_sim_nao.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sim_nao.setObjectName("label_sim_nao")
        self.Label_Borda.raise_()
        self.label_fundo.raise_()
        self.label_manutencao.raise_()
        self.label_fundo_painel.raise_()
        self.label_raio.raise_()
        self.botao_home.raise_()
        self.botao_liberar_trava2.raise_()
        self.label_painel_eletrico.raise_()
        self.label__abertura.raise_()
        self.label_trava_solenoide.raise_()
        self.label_solenoide.raise_()
        self.botao_liberar_trava1.raise_()
        self.botao_energizar_contator_2.raise_()
        self.botao_energizar_contator_1.raise_()
        self.botao_maquina_manutencao.raise_()
        self.label_maquina_em_manutencao.raise_()
        self.label_sim_nao.raise_()
        Manutencao.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Manutencao)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1290, 21))
        self.menubar.setObjectName("menubar")
        Manutencao.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Manutencao)
        self.statusbar.setObjectName("statusbar")
        Manutencao.setStatusBar(self.statusbar)

        self.retranslateUi(Manutencao)
        QtCore.QMetaObject.connectSlotsByName(Manutencao)

    def retranslateUi(self, Manutencao):
        _translate = QtCore.QCoreApplication.translate
        Manutencao.setWindowTitle(_translate("Manutencao", "MainWindow"))
        self.botao_home.setWhatsThis(_translate("Manutencao", "<html><head/><body><p><span style=\" color:#ffffff;\">OI</span></p></body></html>"))
        self.label_manutencao.setText(_translate("Manutencao", "MANUTEN????O"))
        self.label_painel_eletrico.setText(_translate("Manutencao", "PAINEL EL??TRICO"))
        self.botao_liberar_trava1.setText(_translate("Manutencao", "LIBERAR TRAVA DO\n"
"PAINEL EL??TRICO"))
        self.botao_energizar_contator_1.setText(_translate("Manutencao", "ENERGIZAR CONTATOR"))
        self.label_maquina_em_manutencao.setText(_translate("Manutencao", "M??QUINA EM MANUTEN????O"))
        self.label_sim_nao.setText(_translate("Manutencao", "SIM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Manutencao = QtWidgets.QMainWindow()
    ui = Ui_Manutencao()
    ui.setupUi(Manutencao)
    Manutencao.show()
    sys.exit(app.exec_())
