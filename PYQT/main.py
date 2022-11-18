##################### IMPORTANDO AS BIBLIOTECAS E FUNÇÕES ################################
import sys
import datetime
import requests
from datetime import datetime
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView, QPushButton, QLabel, QLineEdit, QTableWidget
from PyQt5.QtGui import QIcon, QPixmap

import sqlite3
import os

"""import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

trava_do_painel = 12
Alimentacao_maquina = 16
led_manutencao = 15

GPIO.setup(Alimentacao_maquina, GPIO.OUT)
GPIO.setup(led_manutencao, GPIO.OUT)
GPIO.setup(trava_do_painel, GPIO.OUT)

GPIO.output(Alimentacao_maquina, False)
GPIO.output(led_manutencao, False)
GPIO.output(trava_do_painel, False)
"""

##################### IMPORTANDO AS CLASSES DOS ARQUIVOS DE TELAS ################################
from Menu01 import Ui_Menu01
from Menu01Aprendiz import Ui_Menu01Aprendiz
from Menu02 import Ui_Menu02
from Caderno_Verde_Atencao import Ui_Atencao
from Liberação_Segurança import Ui_Liberacao_Seguranca
from Liberação_Meio_Ambiente import Ui_Liberacao_Meio_Ambiente
from Documentos_Menu import Ui_documentos_menu
from Documentos_Documentos_de_pecas_menuu import Ui_documentos_documentos_de_pecas_menu
from documentos_documentos_de_pecas_1 import Ui_peca01
from documentos_diagrama_eletrico_imagens import  Ui_documentos_diagrama_eletrico
from Documentos_mapa_de_risco import Ui_mapa_de_riscos
from Aviso_liberacao import Ui_Aviso_Liberacao
from Interface_didatica_menu import Ui_interface_didatica_menu
from Interface_didatica_menu_botoes_botoeira import Ui_interface_didatica_menu_botoes
from Interface_didatica_finalidade import  Ui_interface_didatica_finalidade
from Interface_didatica_menu_botao_emergencia import Ui_interface_didatica_menu_botao_emergencia
from Registros_menu import Ui_Registros_menu
from Cadastros_menu import Ui_cadastros_menu
from Cadastros_menu_adicionar import Ui_cadastros_classes
from Cadastros_adicionar_ficha01 import Ui_cadastros_adicionar_ficha01
from Usuario_registrado import Ui_Usuario_registrado
from Editar_cadastro import Ui_Editar_cadastro
from aproxime_cracha import Ui_Aproxime_cartao
from Registros_historico_utilizacao import Ui_cadastros_historico_utilizacao
from standby import Ui_Standby
from Menu01_skill2 import Ui_Menu01_skill2
from Relatos_liberacao import Ui_Relatos_liberacao
from leitor import Ui_leitor
from Manutencao import Ui_Manutencao

################################ VARIÁVEIS GLOBAIS ################################
serra_de_perfil = "1"

################################ CLASSE CONEXÃO COM O BANCO DE DADOS ################################
class Connection:

    def __init__(self, db):
        # self.url = 'http://192.168.0.11:8000/'
        self.url = 'http://localhost:8000/'
        self.banco = sqlite3.connect(db)
        self.nameColadorador = ''
        self.idColadorador = ''
        self.idCardColadorador = ''
        self.idReleaseMachine = ''
        self.statusMachine()
        self.requisitosMaquinaMeioAmb()
        self.requisitosMaquinaSeguranca()

    ################################ FUNÇÕES DO BANCO DE DADOS ################################

    #Verifica se o usuario esta no banco de dados
    def pesquisar_colaborador(self, idcard):
        self.json_response = requests.get(self.url + 'associates/' + idcard)

        if (self.json_response.status_code == 500):
            standby.hide()
            standby.show()

        if(self.json_response.status_code==200):
            return self.tipo_colaborador(self.json_response.json())

    #Verifica o status da máquina
    def statusMachine(self):
        self.statusMachinejson = requests.get(self.url + 'machines/' + serra_de_perfil).json()
        if self.statusMachinejson['status'] == True:
            return True

    #Busca os requisitos de segurança da máquina
    def requisitosMaquinaSeguranca(self):
        self.reqSeguranca= requests.get(self.url + 'greenbooks/1/1/').json()
        self.listreqSeguranca = list(self.reqSeguranca)
        self.listreqSeguranca2 = []
        for x in range(len(self.listreqSeguranca)):
            self.listreqSeguranca2.append(self.listreqSeguranca[x]['question'])

    #Busca os requisitos de meio ambiente da máquina
    def requisitosMaquinaMeioAmb(self):
        self.reqMeioAmb= requests.get(self.url + 'greenbooks/1/2/').json()

        self.listreqMeioAmb = list(self.reqMeioAmb)
        self.listreqMeioAmb2 = []
        for x in range(len(self.listreqMeioAmb)):
            self.listreqMeioAmb2.append(self.listreqMeioAmb[x]['question'])

    #Busca os registros de utilização da máquina
    def registrosList(self):
        try:
            self.registros = requests.get(self.url + 'getreleasemachines/').json()
            return self.registros
        except ValueError:
            print(ValueError)

    #Busca os registros de utilização da máquina (auxiliar)
    def registrosList2(self):
        try:
            self.registros2 = requests.get(self.url + 'getreleasemachines/').json()

            return self.registros2
        except ValueError:
            print(ValueError)

    #Busca os tods usuários
    def todosUsers(self):
        # TODOS OS USUÁRIOS
        self.json_responseUser = requests.get(self.url + 'getassociates/')
        if(self.json_responseUser.status_code == 200):
            return list(self.json_responseUser.json())

        else:
            print("deu erro na aquisição")

    #Verifica o tipo de colaborador
    def tipo_colaborador(self, dadosJson):
        # APRENDIZ
        self.nameColadorador = dadosJson['name']
        self.idColadorador = str(dadosJson['id'])
        self.edvColadorador = dadosJson['EDV']
        self.idCardColadorador = dadosJson['id_card']
        self.adminU = dadosJson['adminU']
        self.dataNascColaborador = dadosJson['birth']
        self.jobposition = dadosJson['jobposition']
        self.skill = dadosJson['skill']
        self.skill2 = dadosJson['skill2']

        global idGlobal
        idGlobal = self.idColadorador

        self.dataNascFormat = datetime.strptime(self.dataNascColaborador, '%Y-%m-%d')
        self.dataNascFormat2 = datetime.strftime(self.dataNascFormat, '%d/%m/%Y')

        #---------------- TIPOS DE USUÁRIOS -------------

        # --------------- users com skill2
        if self.jobposition == 1 and self.skill2 == True or self.jobposition == 4 and self.skill2 == True or self.jobposition == 2:
            return ['n2', self.idCardColadorador, self.edvColadorador, self.nameColadorador, self.dataNascFormat2]

        #-------------- users com skill1
        elif self.jobposition == 1 or self.jobposition == 4:
            return ['n1', self.idCardColadorador, self.edvColadorador, self.nameColadorador, self.dataNascFormat2]

        elif self.jobposition == 3:
            return ['adm', self.idCardColadorador, self.edvColadorador, self.nameColadorador, self.dataNascFormat2]

        # elif self.jobposition['typeJob'] == "Instrutor":
        #     return ['adm', self.idCardColadorador, self.edvColadorador, self.nameColadorador, self.dataNascFormat2]

    #Adiciona um novo usuário no banco
    def adicionar_cadastro(self, tag_cartao, nome, classe, edv, datanasc):
        cursor = self.banco.cursor()
        self.cargo = 0
        skilladd: False
        skill2add: False
        self.adminU: False
        dataNascFormat = datetime.strptime(datanasc, '%d/%m/%Y').date()
        dataNascFormat = datetime.strftime(dataNascFormat, '%Y-%m-%d')

        if classe == 'Aprendiz':
            self.cargo = 1
            cadastro.cadastrarColaborador(tag_cartao, nome,self.cargo,edv,dataNascFormat, True, False, False)

        if classe == 'Meio_Oficial':
            self.cargo = 4
            cadastro.cadastrarColaborador(tag_cartao, nome, self.cargo, edv, dataNascFormat, True, False, False)

        elif classe == 'Responsável':
            self.cargo = 3
            cadastro.cadastrarColaborador(tag_cartao, nome, self.cargo, edv, dataNascFormat, True, True, True)

        elif classe == 'Manutentor':
            self.cargo = 2
            cadastro.cadastrarColaborador(tag_cartao, nome, self.cargo, edv, dataNascFormat,True, True, False)

    #Altera o valor da tag do cartão no banco
    def update_tag(self, tag_cartao, edv):
        self.idjson = requests.get(self.url + 'getassociatesedv/' + edv +'/').json()
        self.id = self.idjson['id']
        path = self.url + 'getassociatesedv/' + str(self.id) + '/'
        body = {
            "id_card": tag_cartao
        }

        try:
            urlpatchTag = requests.patch(path, body)
            return True
        except:
            print("error")

    #Busca o edv do cadastro que está sendo alterado
    def busca_edv(self, edv):
        self.idjson = requests.get(self.url + 'getassociatesedv/' + edv +'/').json()
        self.id = self.idjson['id']
        self.birth2 = self.idjson['birth']
        return [self.id, self.birth2]

    def retorna_descricao_registro(self, edv, hora, data):
        self.idValue = self.busca_edv(edv)
        self.idValue = self.idValue[0]
        self.returnDesc = self.url + 'getreleasemachinesanalise/' + str(self.idValue) + '/'
        dataNascFormat = datetime.strptime(data, '%d/%m/%Y')
        dataNascFormat2 = datetime.strftime(dataNascFormat, '%Y-%m-%d')
        dataNascFormat2 = str(dataNascFormat2)
        self.requestsDesc = requests.get(self.returnDesc).json()
        for i in range(len(self.requestsDesc)):
            if(self.requestsDesc[i]['description']!='' and self.requestsDesc[i]['date'] == dataNascFormat2):
                return(self.returnDesc[i]['description'])

################################ ADICIONA NOVO USUÁRIO NO BANCO ################################

class Adicionar():
    def cadastrarColaborador(self, tag_cartao, nome, classe, edv, dataNascFormat, skilladd, skill2add, adminU):
        path = 'associates/'

        body = [{
            "jobposition": classe,
            "name": nome,
            "EDV": edv,
            "id_card": tag_cartao,
            "skill": skilladd,
            "skill2": skill2add,
            "adminU": adminU,
            "birth": dataNascFormat,

        }]
        try:
            urlPost = banco_dados.url + path

            post = requests.post(urlPost, json=body)

            if post.status_code == 200:
                print('post realizado', post.status_code)

            else:
                print('post NÃO realizado', post.status_code)
        except:
            print("error")

################################ TELA DE ENTRADA E STANDBY ################################
class Standby(QMainWindow, Ui_Standby):  # Tela que ocorre a validação do ID_Card do colaborador.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.lineEdit_tag.setFocus()
        self.lineEdit_tag.returnPressed.connect(self.comeca)
        self.lineEdit_tag.setText("")
        self.botao_imagem.clicked.connect(self.mousePressEvent)

        # ******************************* VARIÁVEIS *******************************

        self.cadeado_manutencao = QIcon("imagens/Cadeado_manutencao.png")
        self.cadeado_normal = QIcon("imagens/CADEADO_FECHADO.png")

    # ******************************* FUNÇÕES DA CLASSE *******************************
    def mousePressEvent(self, e): # Função caso clique na tela, ainda garante que a tag seja escrita na lineEdit_tag.
        self.lineEdit_tag.setFocus()

    # Função que é chamada para fazer a verificação da tag do usuário após passar o crachá sobre o leitor/ENTER for pressionado.
    def comeca(self):
        tag = self.lineEdit_tag.text()

        self.colaboradorB = banco_dados.pesquisar_colaborador(tag)

        if(self.colaboradorB  != None):
            self.classeColaborador = self.colaboradorB[0]
            self.colaborador2 = self.colaboradorB[3].split(" ")
            self.configurar()

        else:
            self.lineEdit_tag.setFocus()
            self.lineEdit_tag.setText("")
            self.label_titulo.setText("ERRO DE LEITURA\nTENTE NOVAMENTE")
            pass

    def configurar(self):# Função que personaliza o menu com os dados do usuário, Nome, Edv e Classe.
        strNome = "Nome: " + self.colaboradorB[3]

        # Se o usuário estiver cadastrado como Aprendiz ou Meio Oficial aparece apenas o Menu 01.
        if (self.colaboradorB[0] == "n2"  or self.colaboradorB[0] == "ma"):
            relatos_liberacao.label_nome.setText(strNome)
            Menu01_skill2.Label_Colaborador.setText(f'COLABORADOR: {self.colaborador2[0]} {self.colaborador2[-1]}')
            Menu01_skill2.Label_EDV.setText(f"EDV: {self.colaboradorB[2]}")
            standby.hide()
            Menu01_skill2.show()

        # Se o usuário estiver cadastrado como Aprendiz ou Meio Oficial aparece apenas o Menu 01 Aprendiz.
        elif (self.colaboradorB[0] == 'n1'):
            relatos_liberacao.label_nome.setText(strNome)
            Menu01Aprendiz.Label_Colaborador.setText(f'COLABORADOR: {self.colaborador2[0]} {self.colaborador2[-1]}')
            Menu01Aprendiz.Label_EDV.setText(f"EDV: {self.colaboradorB[2]}")
            standby.hide()
            Menu01Aprendiz.show()

        # Se o usuário estiver cadastrado como Administrador Menu 01.
        elif (self.colaboradorB[0] == 'adm'):
            Menu01.Label_Colaborador.setText(f'COLABORADOR: {self.colaborador2[0]} {self.colaborador2[-1]}')
            relatos_liberacao.label_nome.setText(strNome)
            Menu01.Label_EDV.setText(f"EDV: {self.colaboradorB[2]}")
            Menu02.Label_Colaborador.setText(f'COLABORADOR: {self.colaborador2[0]} {self.colaborador2[-1]}')
            Menu02.Label_EDV.setText(f"EDV: {self.colaboradorB[2]}")
            standby.hide()
            Menu01.show()

        # Verifica como está o estado de manutenção da máquina.
        if reqManutencao.verifica_estado_de_manutencao(serra_de_perfil) == True:
            Menu01.Botao_Liberar_Maquina.setIcon(self.cadeado_manutencao)
            Menu01Aprendiz.Botao_Liberar_Maquina.setIcon(self.cadeado_manutencao)
            Menu01_skill2.Botao_Liberar_Maquina.setIcon(self.cadeado_manutencao)
            Menu01.Botao_Liberar_Maquina.setIconSize(QtCore.QSize(231, 231))
            Menu01Aprendiz.Botao_Liberar_Maquina.setIconSize(QtCore.QSize(231, 231))
            Menu01_skill2.Botao_Liberar_Maquina.setIconSize(QtCore.QSize(231, 231))

        else:
            Menu01.Botao_Liberar_Maquina.setIcon(self.cadeado_normal)
            Menu01Aprendiz.Botao_Liberar_Maquina.setIcon(self.cadeado_normal)
            Menu01_skill2.Botao_Liberar_Maquina.setIcon(self.cadeado_normal)
            Menu01.Botao_Liberar_Maquina.setIconSize(QtCore.QSize(220, 220))
            Menu01Aprendiz.Botao_Liberar_Maquina.setIconSize(QtCore.QSize(220, 220))
            Menu01_skill2.Botao_Liberar_Maquina.setIconSize(QtCore.QSize(220, 220))

    #Função de sair e ir para standby
    def sairMenu(self):
        banco_dados.todosUsers()
        if (self.colaboradorB[0] == 'n1'):
             Menu01Aprendiz.hide()
             standby.show()

        elif(self.colaboradorB[0] == 'n2' or self.colaboradorB[0] == 'ma'):
             Menu01_skill2.hide()
             standby.show()

        else:
            Menu02.hide()
            standby.show()

    #Função que vai para a Home
    def homeShow(self):
        if (self.colaboradorB[0] == 'n1'):
             Menu01Aprendiz.show()

        elif(self.colaboradorB[0] == 'n2' or self.colaboradorB[0] == 'ma'):
             Menu01_skill2.show()

        else:
            Menu01.show()

    #Função que fecha a Home
    def homeHide(self):
        if (self.colaboradorB[0] == 'n1'):
             Menu01Aprendiz.hide()

        elif(self.colaboradorB[0] == 'n2' or self.colaboradorB[0] == 'ma'):
             Menu01_skill2.hide()

        else:
            Menu01.show()

#Classe de logout
class Sair():
    def sair(self): #se a máquina não estiver liberada, apenas sairá e vai para a tela standby, se estiver chama a função sairBanco e a máquina fica liberada
        if (standby.classeColaborador == 'n1'):
            if (Menu01Aprendiz.maquina_liberada == False):
                standby.sairMenu()
            else:
                self.sairBanco()

        if (standby.classeColaborador == 'n2'):
            if (Menu01_skill2.maquina_liberada == False):
                standby.sairMenu()

            else:
                self.sairBanco()

        else:
            if(Menu01.maquina_liberada == False):
                standby.sairMenu()
            else:
                self.sairBanco()

    def sairBanco(self):
        url = banco_dados.url + 'releasemachines/' + str(banco_dados.idReleaseMachine) + '/'

        try:
            hora = datetime.today().strftime('%H:%M:%S:%f')

            url = banco_dados.url + 'releasemachines/' + str(banco_dados.idReleaseMachine) + '/'

            patch = {
                "FinishHour": hora,
            }

            urlpost = requests.patch(url, patch)

            if (urlpost.status_code == 200):
                try:

                    urlMachine = banco_dados.url + 'machines/1/'

                    patch2 = {
                        "status": False,
                    }

                    urlPut = requests.patch(urlMachine, patch2)

                    if (urlPut.status_code == 200):
                        standby.lineEdit_tag.setText("")
                        standby.sairMenu()
                        banco_dados.todosUsers()
                        # standby.show()
                except:
                    print(urlPut.status_code)
        except:
            print(urlpost.status_code)

##################### MENU 01 ################################
class Primeiro_Menu(QMainWindow, Ui_Menu01):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

    # ******************************* AÇÕES *******************************

        self.Botao_Seta_Direita.clicked.connect(self.proxima_tela)
        self.Botao_Liberar_Maquina.clicked.connect(self.liberacao_de_maquina)
        self.Botao_Interface_Didatica.clicked.connect(self.interface_didatica)
        self.Botao_Documentos.clicked.connect(self.menu_documentos)
        self.Botao_Registros.clicked.connect(self.menu_registros)

    # ******************************* VARIÁVEIS *******************************
        self.maquina_liberada = False
        self.cadeado_fechado = QIcon("imagens/CADEADO_FECHADO.png")
        self.img2 = QIcon("imagens/CADEADO_ABERTO.png")
        self.confMenu()

    #Configura o Menu dependendo do status da máquina
    def confMenu(self):
        if banco_dados.statusMachine() == True:
            self.maquina_liberada = True
            self.Botao_Liberar_Maquina.setIcon(self.img2)
        else:
            pass

    def proxima_tela(self): #FUNÇÃO QUE CHAMA O MENU 02.
        Menu02.show()
        Menu01.hide()

    def liberacao_de_maquina(self): #FUNÇÃO QUE INICIA O PROCESSO DE LIBERAÇÃO DE MÁQUINA.

        relatos_liberacao.label_itens_nao_conformes.clear()
        liberacao_seguranca.string_da_lista = " "
        liberacao_seguranca.inconformidades.clear()
        liberacao_seguranca.lista_erros = []

        if reqManutencao.verifica_estado_de_manutencao(serra_de_perfil) == False:
            if self.maquina_liberada == False:
                liberacao_atencao.show()
                Menu01.hide()
            else:
                self.Botao_Liberar_Maquina.setIcon(self.img2)

        else:
            # print("Não deixou entrar")
            pass

    def menu_documentos(self): # FUNÇÃO QUE CHAMA A TELA DE MENU DE DOCUMENTOS
        documentos_menu.show()
        Menu01.hide()

    # Função que chama a tela de Interface Didática Menu.
    def interface_didatica(self):
        interface_menu.show()
        Menu01.hide()

    # Função que chama a tela de Menu de Registros.
    def menu_registros(self):
        registros_menu.show()
        Menu01.hide()

class Primeiro_MenuSkill(QMainWindow, Ui_Menu01_skill2):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.Botao_Liberar_Maquina.clicked.connect(self.liberacao_de_maquina)
        self.Botao_Interface_Didatica.clicked.connect(self.interface_didatica)
        self.Botao_Documentos.clicked.connect(self.menu_documentos)
        self.Botao_Registros.clicked.connect(self.menu_registros)
        self.Botao_Sair.clicked.connect(self.sairFunc)
        self.Botao_Manutencao.clicked.connect(self.manutencao)

        # ******************************* VARIÁVEIS *******************************
        self.cadeado_fechado = QIcon("imagens/CADEADO_FECHADO.png")
        self.maquina_liberada = False

    def proxima_tela(self): #FUNÇÃO QUE CHAMA O MENU 02.
        Menu02.show()
        Menu01_skill2.hide()

    def liberacao_de_maquina(self): #FUNÇÃO QUE INICIA O PROCESSO DE LIBERAÇÃO DE MÁQUINA.
        if reqManutencao.verifica_estado_de_manutencao(serra_de_perfil) == False:
            if self.maquina_liberada == False:
                liberacao_atencao.show()
                Menu01_skill2.hide()
            else:
                print("segundo else")

        else:
            print("Não deixou entrar")
            pass
    def menu_documentos(self): # FUNÇÃO QUE CHAMA A TELA DE MENU DE DOCUMENTOS
        documentos_menu.show()
        Menu01_skill2.hide()

    def interface_didatica(self):# Função que chama a tela de Interface Didática Menu.
        interface_menu.show()
        Menu01_skill2.hide()

    def menu_registros(self):# Função que chama a tela de Menu de Registros.
        registros_menu.show()
        Menu01_skill2.hide()

    def sairFunc(self): #Função de logout
        sairDef.sair()
        Menu01Aprendiz.maquina_liberada = False
        self.clear_checkboxes()
        standby.lineEdit_tag.setText("")
        standby.label_titulo.setText("APROXIME O CRACHÁ\nSOBRE O LEITOR")
        #GPIO.output(Alimentacao_maquina, False)

    def manutencao(self): #Função que chama a tela de manutenção
        manutencao.show()
        Menu02.hide()

    def clear_checkboxes(self): #Função que limpa os checkboxes
        Menu01Aprendiz.maquina_liberada = False
        self.checkboxes = [liberacao_seguranca.checkBox_1, liberacao_seguranca.checkBox_2,
                           liberacao_seguranca.checkBox_3,
                           liberacao_seguranca.checkBox_4, liberacao_seguranca.checkBox_5,
                           liberacao_seguranca.checkBox_6,
                           liberacao_seguranca.checkBox_7, liberacao_seguranca.checkBox_8,
                           liberacao_seguranca.checkBox_9,
                           liberacao_meio_ambiente.checkBox_1]
        for i in self.checkboxes:
            i.setChecked(False)
        Menu01Aprendiz.Botao_Liberar_Maquina.setIcon(self.cadeado_fechado)

##################### MENU 01 APRENDIZ ################################
class Primeiro_MenuAPRENDIZ(QMainWindow, Ui_Menu01Aprendiz):
    # --------------------------  Essa classe possui as mesmas funções do Menu01, porém limitada, não pode ir para o Menu02 -----------------------
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************
        self.Botao_Liberar_Maquina.clicked.connect(self.liberacao_de_maquina)
        self.Botao_Interface_Didatica.clicked.connect(self.interface_didatica)
        self.Botao_Documentos.clicked.connect(self.menu_documentos)
        self.Botao_Registros.clicked.connect(self.menu_registros)
        self.Botao_Sair.clicked.connect(self.sairFunc)

        # ******************************* VARIÁVEIS *******************************

        self.maquina_liberada = False
        self.cadeado_fechado = QIcon("imagens/CADEADO_FECHADO.png")

    def liberacao_de_maquina(self):

        if reqManutencao.verifica_estado_de_manutencao(serra_de_perfil) == False:
            if self.maquina_liberada == False:
                liberacao_atencao.show()
                Menu01Aprendiz.hide()
            else:
                ""

        else:
            # print("Não deixou entrar")
            pass

    def menu_documentos(self):  # FUNÇÃO QUE CHAMA A TELA DE MENU DE DOCUMENTOS
        documentos_menu.show()
        Menu01Aprendiz.hide()

    def interface_didatica(self): # Função que chama a tela de Interface Didática Menu.
        interface_menu.show()
        Menu01Aprendiz.hide()

    def menu_registros(self):# Função que chama a tela de Menu de Registros.
        registros_menu.show()
        Menu01Aprendiz.hide()

    # Função de logout
    def sairFunc(self):
        sairDef.sair()
        Menu01Aprendiz.maquina_liberada = False
        self.clear_checkboxes()
        standby.lineEdit_tag.setText("")
        standby.label_titulo.setText("APROXIME O CRACHÁ\nSOBRE O LEITOR")
        #GPIO.output(Alimentacao_maquina, False)

    # Função que limpa os checkboxes
    def clear_checkboxes(self):
        Menu01Aprendiz.maquina_liberada = False
        self.checkboxes = [liberacao_seguranca.checkBox_1, liberacao_seguranca.checkBox_2,
                           liberacao_seguranca.checkBox_3,
                           liberacao_seguranca.checkBox_4, liberacao_seguranca.checkBox_5,
                           liberacao_seguranca.checkBox_6,
                           liberacao_seguranca.checkBox_7, liberacao_seguranca.checkBox_8,
                           liberacao_seguranca.checkBox_9,
                           liberacao_meio_ambiente.checkBox_1]
        for i in self.checkboxes:
            i.setChecked(False)
        Menu01Aprendiz.Botao_Liberar_Maquina.setIcon(self.cadeado_fechado)

############################## SEGUNDO MENU ##############################
class Segundo_Menu(QMainWindow, Ui_Menu02): #Tela do segundo menu, que contém manutenção e cadastros.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************
        self.Botao_Seta_Esquerda.clicked.connect(self.tela_anterior)
        self.Botao_Cadastros.clicked.connect(self.cadastros)
        self.Botao_Sair.clicked.connect(self.sair)
        self.Botao_Manutencao.clicked.connect(self.manutencao)

        # ******************************* VARIÁVEIS *******************************
        self.cadeado_fechado = QIcon("imagens/CADEADO_FECHADO.png")

        # ******************************* FUNÇÕES DA CLASSE *******************************
    def tela_anterior(self):# Função que volta para o menu 01.
        Menu01.show()
        Menu02.hide()

    def cadastros(self): # Função que abre o menu de cadastros.
        cadastros_menu.load_tabela()
        cadastros_menu.show()
        Menu02.hide()

    def sair(self): # Função de sair e que reconfigura todas as funções e telas para seu estado original.
        interface_menu_botoes.label_titulo.setText(
            "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">BOTOEIRA</span></p></body></html>")
        interface_menu_botoes.label_caixa_de_texto.setText(
            "             Clique nos números para verificar a respectiva \nfunção do botão ou chave seletora. \n")
        sairDef.sair()
        Menu01.maquina_liberada = False
        self.clear_checkboxes()
        standby.lineEdit_tag.setText("")
        standby.label_titulo.setText("APROXIME O CRACHÁ\nSOBRE O LEITOR")
        #GPIO.output(Alimentacao_maquina, False)
        standby.show()

    def clear_checkboxes(self): # Desmarca todos os check_boxes para a próxima liberação.
        Menu01.maquina_liberada = False
        self.checkboxes = [liberacao_seguranca.checkBox_1, liberacao_seguranca.checkBox_2,
                           liberacao_seguranca.checkBox_3,
                           liberacao_seguranca.checkBox_4, liberacao_seguranca.checkBox_5,
                           liberacao_seguranca.checkBox_6,
                           liberacao_seguranca.checkBox_7, liberacao_seguranca.checkBox_8,
                           liberacao_seguranca.checkBox_9,
                           liberacao_meio_ambiente.checkBox_1]
        for i in self.checkboxes:
            i.setChecked(False)
        Menu01.Botao_Liberar_Maquina.setIcon(self.cadeado_fechado)

    def manutencao(self): # Função que abre a tela de manutenção.
        manutencao.show()
        Menu02.hide()

################################ TELA DE INSTRUÇÕES PARA LIBERAÇÃO ################################
class Liberacao_atencao(QMainWindow, Ui_Atencao): # Tela de advertência sobre o processo de libreação de máquina.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_continuar.clicked.connect(self.tela_de_seguranca)
        self.botao_home.clicked.connect(self.home)

        # ******************************* FUNÇÕES DA CLASSE *******************************

    # Função que avança para a Liberação_Segurança.
    def tela_de_seguranca(self):
        liberacao_seguranca.show()
        liberacao_atencao.hide()

    # Função que retorna para o Menu01 (HOME).
    def home(self):
        liberacao_atencao.hide()
        standby.homeShow()

################################ TELA DE LIBERAÇÃO DOS REQUISITOS DE SEGURANÇA ################################
#Tela que o usuário verifica os requisitos de segurança.
class Liberacao_seguranca(QMainWindow, Ui_Liberacao_Seguranca):
    # Tela que o usuário verifica os requisitos de segurança.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_home.clicked.connect(self.home)
        self.botao_continuar.clicked.connect(self.tela_meio_ambiente)
        self.allcheckBox = [self.checkBox_1, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5,
                            self.checkBox_6, self.checkBox_7, self.checkBox_8, self.checkBox_9]

        # ******************************* VARIÁVEIS *******************************

        self.liberacao_seguranca = False
        self.lista_real = []  # Lista de Check_Boxes checados.
        self.lista_erros = []  # Lista de Check_Boxes não checados.
        self.texto = []  # Texto  indicando os Check_boxes não checados.
        self.contador = 0  # Contador auxiliar.
        self.inconformidades = []

        self.string_da_lista = ""

        # ******************************* FUNÇÕES DA CLASSE *******************************

    def verifica_checkBox(self):# Função que valida se todos os Check_Boxes estão checados.
        self.lista_real = []
        self.contador = 0

        for i in self.allcheckBox:
            if i.isChecked():
                self.contador = self.contador + 1
                self.lista_real.append(self.contador)

            else:
                self.contador = self.contador + 1

        for reqs in range(len(banco_dados.listreqSeguranca2)):
            if banco_dados.listreqSeguranca2[reqs] not in self.lista_real:
                inconformidade = "\n" + banco_dados.listreqSeguranca2[reqs]
                self.inconformidades.append(inconformidade)
    def verifica_check_boxes_seguranca(self):  # Função que verifica os Checkboxes de segurança.
        for i in range(1, 10):
            if i not in self.lista_real:
                self.lista_erros.append(i)

        if len(self.lista_erros) != 0:
            self.texto = str(self.lista_erros)
            return False
        else:
            return True


    def home(self):  # Função que retorna para o Menu01 (HOME).
        standby.homeShow()
        # Menu01.show()
        liberacao_seguranca.hide()

    def tela_meio_ambiente(self): # Função que passa para a tela de meio-ambiente caso todos os checkboxes de segurança estiverem checados.
        self.verifica_checkBox()
        if self.verifica_check_boxes_seguranca() == True:
            self.liberacao_seguranca = True
            aviso_liberacao.label_itens_seguranca.setText("OK")

        else:
            aviso_liberacao.label_itens_seguranca.setText(f"<html><head/><body><p align=\"center\">{self.texto}")
            self.liberacao_seguranca = False

        liberacao_meio_ambiente.show()
        liberacao_seguranca.hide()

    def relatos_liberacao(self): # Função qeu chama a tela de relatar incidente.
        relatos_liberacao.lineEdit_descricao.setFocus()
        liberacao_seguranca.string_da_lista = " ".join(liberacao_seguranca.inconformidades)
        relatos_liberacao.label_itens_nao_conformes.setText(liberacao_seguranca.string_da_lista)

        relatos_liberacao.show()
        aviso_liberacao.hide()

################################ TELA DE AVISO ################################
class Aviso_liberacao(QMainWindow, Ui_Aviso_Liberacao):  # Tela que adverte o colaborador de que alguns Checkboxes ficaram deschecados, caso seja engano ele pode voltar, e se caso for algum incidente procede para a tela de Relatos de Incidentes.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_voltar.clicked.connect(self.voltar_check_list)
        self.botao_relatar_problema.clicked.connect(self.relatos_liberacao)

    # ******************************* FUNÇÕES DA CLASSE *******************************

    #Função que retorna para os Checkboxes da respectiva tela de liberação.
    def voltar_check_list(self):
        if liberacao_seguranca.liberacao_seguranca == False:
            liberacao_seguranca.lista_erros = []
            relatos_liberacao.label_itens_nao_conformes.clear()
            liberacao_seguranca.string_da_lista = " "
            liberacao_seguranca.inconformidades.clear()

            liberacao_seguranca.show()
            aviso_liberacao.hide()

        else:
            #self.label_itens_seguranca.setText("OK")
            liberacao_meio_ambiente.show()
            aviso_liberacao.hide()

    #Função qeu chama a tela de relatar incidente.
    def relatos_liberacao(self): # Função qeu chama a tela de relatar incidente.

        relatos_liberacao.voltar_registros_ou_liberacao = False
        relatos_liberacao.botao_finalizar.setDisabled(False)
        relatos_liberacao.label_itens_nao_conformes.clear()
        relatos_liberacao.lineEdit_descricao.clear()

        relatos_liberacao.lineEdit_descricao.setFocus()
        liberacao_seguranca.string_da_lista = " ".join(liberacao_seguranca.inconformidades)
        relatos_liberacao.label_itens_nao_conformes.setText(liberacao_seguranca.string_da_lista)
        data = datetime.today().strftime('%d/%m/%Y')
        hora = datetime.today().strftime('%H:%M')
        relatos_liberacao.label_data.setText(data)
        relatos_liberacao.label_periodo.setText(hora)
        relatos_liberacao.show()
        aviso_liberacao.hide()

################################ TELA DE RELATO DE INCONFORMIDADES DA LIBERAÇÃO ################################
class Relatos_liberacao(QMainWindow, Ui_Relatos_liberacao):  #Tela que mostra todas as inconformidades encontradas durante o processo de liberação e disponibiliza um campo para o usuário digitar algum comentário caso necessário.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************
        self.botao_cancelar.clicked.connect(self.voltar)
        self.botao_finalizar.clicked.connect(self.salvar)

        # ******************************* VARIÁVEIS *******************************

        self.voltar_registros_ou_liberacao = False

        # ******************************* CONFIGURAÇÕES *******************************

        self.lineEdit_descricao.clear()
        self.lineEdit_descricao.setPlaceholderText(
            "Digite aqui uma breve descrição sobre o incidente ou anomalia encontrada.")

        # Função que quebra a linha da line_edit_descrição. (teste)
        """def digita(self):
            self.value = self.lineEdit_descricao.text()

            self.wrapper = textwrap.TextWrapper(width=10)
            self.string = self.wrapper.fill(text=self.value)
            self.lineEdit_descricao.setText(self.string)
            self.teste = self.string.split()


            for i in self.teste:
                self.teste.insert(1, '\n')
            print(self.teste)
            print(self.string)"""
    def salvar(self):  # Função que salva o registro digitado pelo usuário e as inconformidades no banco de dados.
        self.label_itens_nao_conformes.clear()

        data = datetime.today().strftime('%Y-%m-%d')
        hora = datetime.today().strftime('%H:%M:%S:%f')
        descricao = self.lineEdit_descricao.text()

        body = [{
            "date": data,
            "InitialHour": hora,
            "FinishHour": None,
            "idMachineFK": "1",
            "idAssociateFK": idGlobal,
            "examA": 'A',
            "examB": 'B',
            "description": descricao,
            "result": 'NÃO OK'
        }]

        try:
            url = banco_dados.url + 'releasemachines/'

            urlRelato = requests.post(url,json= body)
            if(urlRelato.status_code == 200):
                reqManutencao.estado_manutencao(True, serra_de_perfil)
                relatos_liberacao.hide()
                standby.homeShow()
            else:
                print(urlRelato.status_code)
        except:
            print(urlRelato.status_code)

    def voltar(self): #Função de voltar.
        self.label_itens_nao_conformes.clear()
        liberacao_seguranca.string_da_lista = " "
        liberacao_seguranca.inconformidades.clear()
        liberacao_seguranca.lista_erros = []
        if self.voltar_registros_ou_liberacao == False:
            liberacao_seguranca.show()
            relatos_liberacao.hide()

        else:
            registro_historico_utilizacao.show()
            relatos_liberacao.hide()

################################ TELA DE LIBERAÇÃO DOS REQUISITOS DE MEIO-AMBIENTE ################################
class Liberacao_meio_ambiente(QMainWindow, Ui_Liberacao_Meio_Ambiente): # Tela que o usuário verifica os requisitos de meio-ambiente.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_home.clicked.connect(self.home)
        self.botao_continuar.clicked.connect(self.Verifica_checkboxes)

        # ******************************* VARIÁVEIS *******************************
        self.liberacao_meio_ambiente = False
        self.img2 = QIcon("imagens/CADEADO_ABERTO.png")
        self.cadeado_manutencao = QIcon("imagens/CADEADO_MANUTENCAO.png")
        self.allcheckBox = [self.checkBox_1]

    # ******************************* FUNÇÕES DA CLASSE *******************************
    def home(self): # Função que retorna para o Menu.
        liberacao_meio_ambiente.hide()
        standby.homeShow()
        # Menu01.show()

    # Função que verifica os Chechboxes de meio-ambiente e envia o sinal de uma porta analógica da Raspberry para comutar o contator elétrico caso o status da liberação seja OK.
    # Se a liberação for "Não OK" e o colaborador identificar algum problema na integridade e funcionamento da máquina, abre-se uma ficha para que o incidente seja relatado.
    def Verifica_checkboxes(self):

        if self.checkBox_1.isChecked():
            #classeColaborador é o variável da classe standby
            if (standby.classeColaborador == 'n1'):
                Menu01Aprendiz.maquina_liberada = True
                aviso_liberacao.label_itens_meio_ambiente.setText("OK")


            elif (standby.classeColaborador == 'n2'):
                Menu01_skill2.maquina_liberada = True
                aviso_liberacao.label_itens_meio_ambiente.setText("OK")


            else:
                Menu01.maquina_liberada = True
                aviso_liberacao.label_itens_meio_ambiente.setText("OK")

        else:
            inconformidade = "\n" + banco_dados.listreqMeioAmb2[0]

            liberacao_seguranca.inconformidades.append(inconformidade)

            self.liberacao_meio_ambiente = False
            aviso_liberacao.label_itens_meio_ambiente.setText(f"<html><head/><body><p align=\"center\">1")

        if self.checkBox_1.isChecked() and (liberacao_seguranca.liberacao_seguranca == True):
            # GPIO.output(Alimentacao_maquina, True)
            data = datetime.today().strftime('%Y-%m-%d')
            hora = datetime.today().strftime('%H:%M:%S:%f')

            url = banco_dados.url + 'releasemachines/'

            body = [{
                "date": data,
                "InitialHour": hora,
                "FinishHour": None,
                "idMachineFK": "1",
                "idAssociateFK": idGlobal,
                "examA": 'A',
                "examB": 'B',
                "description": None,
                "result": 'OK'
            }]

            try:
                urlpost = requests.post(url, json = body)
                if(urlpost.status_code==200):
                    try:
                        urlID = urlpost.json()

                        banco_dados.idReleaseMachine = urlID[0]['id']

                        urlMachine = banco_dados.url + 'machines/1/'
                        patch = {
                            "status": True,
                        }

                        urlPut = requests.patch(urlMachine, json=patch)
                        if(urlPut.status_code==200):
                            if (standby.classeColaborador == 'n1'):
                                Menu01Aprendiz.Botao_Liberar_Maquina.setIcon(self.img2)
                                liberacao_meio_ambiente.hide()
                                Menu01Aprendiz.show()

                            elif (standby.classeColaborador == 'n2' or standby.classeColaborador == 'ma'):
                                Menu01_skill2.Botao_Liberar_Maquina.setIcon(self.img2)
                                liberacao_meio_ambiente.hide()
                                Menu01_skill2.show()

                            else:
                                Menu01.Botao_Liberar_Maquina.setIcon(self.img2)
                                liberacao_meio_ambiente.hide()
                                Menu01.show()
                    except:
                        print(urlPut.status_code)
            except:
                print(urlpost.status_code)

        else:
            # aviso_liberacao.label_texto.setText("<html><head/><body><p align=\"center\">O(s) seguinte(s) item(s) de Meio Ambiente não foram </p><p align=\"center\"> marcado(s), o que significa que ele(s) apresenta(m)</p><p align=\"center\"> não conformidade:</p></body></html>")
            # aviso_liberacao.label_itens_desmarcados.setText(f"<html><head/><body><p align=\"center\">1")
            aviso_liberacao.show()
            liberacao_meio_ambiente.hide()

################################ TELA DE MENU DE DOCUMENTOS E DESENHOS ################################ TELA MENU DE INTERFACE DIDÁTICA ################################
class Interface_didatica_menu(QMainWindow, Ui_interface_didatica_menu): # Tela que fornece um suporte didático sobre a utilização da máquina para os colaboradores.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_botoes.clicked.connect(self.botoes)
        self.botao_finalidades.clicked.connect(self.finalidade)
        self.botao_home.clicked.connect(self.home)

        # ******************************* FUNÇÕES DA CLASSE *******************************

    def finalidade(self): # Função que chama a tela de Finalidade da Máquina.
        interface_menu_finalidade.show()
        interface_menu.hide()

    def botoes(self): # Função que chama a tela que explica os botões existentes na máquina.
        interface_menu_botoes.show()
        interface_menu.hide()

    def home(self): # Função que volta para o Menu.
        Menu01.show()
        interface_menu.hide()


################################ TELA DE BOTÕES DA MÁQUINA ################################
class Interface_botoes(QMainWindow, Ui_interface_didatica_menu_botoes): # Tela que Explica a funcionalidade de cada botão existente na sera de perfil.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_1.clicked.connect(self.botao_01)
        self.botao_2.clicked.connect(self.botao_02)
        self.botao_3.clicked.connect(self.botao_03)
        self.botao_4.clicked.connect(self.botao_04)
        self.botao_5.clicked.connect(self.botao_05)
        self.botao_home.clicked.connect(self.home)
        self.botao_seta_dirteita.clicked.connect(self.botao_emergencia)

        # ******************************* VARIÁVEIS *******************************

        self.estilo_fonte = "border-style: outset;\n" "border-color: rgb(0, 0, 0);\n""border-width:6px;\n""\n""\n""font: 75 30pt \"Bosch Sans Bold\";\n""background-color: rgb(0,0,0);"

        # ******************************* FUNÇÕES DA CLASSE *******************************

    def botao_01(self): # Função que configura e descreve a função do Botão Liga.
        self.label_indicacao.setText("1")
        self.label_titulo.setStyleSheet(self.estilo_fonte)
        self.label_titulo.setText("<html><head/><body><p align=\"center\"><span style=\" color:#FFC000;\">BOTÃO LIGA A SERRA</span></p></body></html>")
        self.label_caixa_de_texto.setText("             Botão responsável por iniciar o processo de \ncorte do perfil se a porta estiver trancada e a peça \ntravada. \n")

    def botao_02(self): # Função que configura e descreve a função da Chave Seletora.
        self.label_titulo.setStyleSheet(self.estilo_fonte)
        self.label_indicacao.setText("2")
        self.label_titulo.setText("<html><head/><body><p align=\"center\"><span style=\" color:#FFC000;\">CHAVE SELETORA DE PERFIL 30/45</span></p></body></html>")
        self.label_caixa_de_texto.setText("             Chave seletora responsável por definir se o \nperfil a ser cortado é de 30 ou 45 para estabelecer a \ndistância que a serra deverá cortar para ultrapassar o \nperfil de 30/45 completamente.")

    def botao_03(self): # Função que configura e descreve a função do Botão Liga.
        self.label_indicacao.setText("3")
        self.label_titulo.setStyleSheet(self.estilo_fonte)
        self.label_titulo.setText("<html><head/><body><p align=\"center\"><span style=\" color:#FFC000;\">CHAVE SELETORA DE PORTA TRANCADA</span></p></body></html>")
        self.label_caixa_de_texto.setText("             Chave seletora responsável por garantir o \ntravamento da porta.\n\n")

    def botao_04(self): # Função que configura e descreve a função do Botão de Travar a Peça.
        self.label_indicacao.setText("4")
        self.label_titulo.setStyleSheet(self.estilo_fonte)
        self.label_titulo.setText("<html><head/><body><p align=\"center\"><span style=\" color:#FFC000;\">BOTÃO PARA TRAVAR PEÇA</span></p></body></html>")
        self.label_caixa_de_texto.setText("             Ao pressionar o botão, dois pistões pneumáticos \ntravam a peça na posição estabelecida pelo usuário.\n\n")

    def botao_05(self): # Função que configura e descreve a função do Botão Reset.
        self.label_indicacao.setText("5")
        self.label_titulo.setStyleSheet(self.estilo_fonte)
        self.label_titulo.setText("<html><head/><body><p align=\"center\"><span style=\" color:#FFC000;\">BOTÃO RESET</span></p></body></html>")
        self.label_caixa_de_texto.setText("             Botão necessário para reiniciar os processos da \nmáquina caso ocorra alguma falha, como a tentativa de \nabrir as portas de segurança durante a operação, ou ao \npressionar o botão de emergência.")

    def botao_emergencia(self): # Função que chama a tela de explicação do Botão de Emergência.
        interface_menu_botao_emergencia.show()
        interface_menu_botoes.hide()

    def home(self): # Função que volta para o menu interface.
        interface_menu.show()
        interface_menu_botoes.hide()


################################ TELA DE BOTÃO DE EMERGÊNCIA ################################
class Interface_botao_emergencia(QMainWindow, Ui_interface_didatica_menu_botao_emergencia): # Tela que explica a funcionalidade do botão de emergência.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_home.clicked.connect(self.home)
        self.botao_seta_esquerda.clicked.connect(self.botoeira)

        # ******************************* FUNÇÕES DA CLASSE *******************************

    def home(self): # Função que volta para o menu interface.
        interface_menu.show()
        interface_menu_botao_emergencia.hide()

    def botoeira(self): # Função que chama a tela de Botões da Máquina.
        interface_menu_botoes.show()
        interface_menu_botao_emergencia.hide()


################################ TELA DE FINALIDADE DE MÁQUINA ################################
class Interface_finalidade(QMainWindow, Ui_interface_didatica_finalidade): # Tela de explicação sobre a finalidade da serra de perfil.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_home.clicked.connect(self.home)

        # ******************************* FUNÇÕES DA CLASSE *******************************

    def home(self): # Função que volta para o menu interface.
        interface_menu.show()
        interface_menu_finalidade.hide()


################################ TELA DE MENU DE DOCUMENTOS E DESENHOS ################################
class Documentos_menu(QMainWindow, Ui_documentos_menu): # Tela de menu de documentos que contém as peças a serem desenvolvidas, o diagrama elétrico da máquina e o mapa de riscos e danos.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_home.clicked.connect(self.home)
        self.botao_documentos_de_pecas01.clicked.connect(self.documentos_de_pecas)
        self.botao_documentos_de_pecas02.clicked.connect(self.documentos_de_pecas)
        self.botao_diagrama_eletrico01.clicked.connect(self.diagrama_eletrico)
        self.botao_diagrama_eletrico02.clicked.connect(self.diagrama_eletrico)
        self.botao_mae01.clicked.connect(self.mapa_de_riscos)
        self.botao_mae02.clicked.connect(self.mapa_de_riscos)

    # ******************************* FUNÇÕES DA CLASSE *******************************

    def home(self): # Função que volta para o menu documentos.
        Menu01.show()
        documentos_menu.hide()

    def documentos_de_pecas(self): # Função que abre o menu de documentos de perfis (desenhos técnicos e especificações).
        documentos_de_pecas_menu.show()
        documentos_menu.hide()

    def diagrama_eletrico(self): # Função que abre o diagrama elétrico.
        diagrama_eletrico.show()
        documentos_menu.hide()

    def mapa_de_riscos(self): # Função que abre o mapa de riscos e danos.
        mapa_de_riscos.show()
        documentos_menu.hide()


################################ TELA DE MENU DE DESENHOS DE PEÇAS ################################
class Documentos_documentos_de_pecas_menu(QMainWindow, Ui_documentos_documentos_de_pecas_menu): # Tela que possui os desenhos mecânicos sobre as peças a serem desenvolvidas durante as aulas.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_home.clicked.connect(self.home)
        self.botao_peca01_1.clicked.connect(self.perfil_de_aluminio_30)
        self.botao_peca01_2.clicked.connect(self.perfil_de_aluminio_30)
        self.botao_peca02_1.clicked.connect(self.perfil_de_aluminio_45)
        self.botao_peca02_2.clicked.connect(self.perfil_de_aluminio_45)
        self.botao_peca03_1.clicked.connect(self.perfil_de_aluminio_60)
        self.botao_peca03_2.clicked.connect(self.perfil_de_aluminio_60)

        # ******************************* VARIÁVEIS *******************************

        self.perfil_30 = QPixmap("imagens/Perfil_30.png")
        self.perfil_30_2 = QPixmap("imagens/Perfil_30_2.png")
        self.perfil_45 = QPixmap("imagens/Perfil_45_certo.png")
        self.perfil_45_2 = QPixmap("imagens/Perfil_45_2.png")
        self.perfil_60 = QPixmap("imagens/Perfil_60.png")
        self.perfil_60L = QPixmap("imagens/Perfil_60L.png")

    # ******************************* FUNÇÕES DA CLASSE *******************************

    def home(self): # Função que volta para o menu documentos.
        documentos_menu.show()
        documentos_de_pecas_menu.hide()

    def perfil_de_aluminio_30(self): # Função que abre o as informações do perfil de alumínio de 30x30.
        perfil_de_aluminio.troca_pagina = 1
        perfil_de_aluminio.label_titulo.setText("PERFIL DE ALUMÍNIO DE 30x30")
        perfil_de_aluminio.label_imagem.move(110,110)
        perfil_de_aluminio.label_imagem.setPixmap(self.perfil_30)
        perfil_de_aluminio.show()
        documentos_de_pecas_menu.hide()

    def perfil_de_aluminio_45(self): # Função que abre o as informações do perfil de alumínio de 45x45.
        perfil_de_aluminio.troca_pagina = 2
        perfil_de_aluminio.label_titulo.setText("PERFIL DE ALUMÍNIO DE 45x45")
        perfil_de_aluminio.label_imagem.move(110, 110)
        perfil_de_aluminio.label_imagem.setPixmap(self.perfil_45)
        perfil_de_aluminio.show()
        documentos_de_pecas_menu.hide()

    def perfil_de_aluminio_60(self): # Função que abre o as informações do perfil de alumínio de 60x60.
        perfil_de_aluminio.troca_pagina = 3
        perfil_de_aluminio.label_titulo.setText("PERFIL DE ALUMÍNIO DE 60x60")
        perfil_de_aluminio.label_imagem.move(110, 110)
        perfil_de_aluminio.label_imagem.setPixmap(self.perfil_60)
        perfil_de_aluminio.show()
        documentos_de_pecas_menu.hide()


################################ TELA PERFIL DE ALUMÍNIO ################################
class Documentos_de_peca_perfil_de_aluminio(QMainWindow, Ui_peca01): # Tela que mostra as informações doos perfis de alumínio.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_home.clicked.connect(self.home)
        self.botao_seta.clicked.connect(self.troca_imagem)

        # ******************************* VARIÁVEIS *******************************

        self.troca_pagina = 0

    # ******************************* FUNÇÕES DA CLASSE *******************************

    def home(self): # Função que volta para o menu documentos.
        documentos_de_pecas_menu.show()
        perfil_de_aluminio.hide()

    def troca_imagem(self): # Função que troca as imagens dos perfis.
        if self.troca_pagina == 1:
            self.label_imagem.move(230,90)
            self.label_imagem.setPixmap(documentos_de_pecas_menu.perfil_30_2)
            self.troca_pagina = 11

        elif self.troca_pagina == 11:
            self.label_imagem.move(110,110)
            self.label_imagem.setPixmap(documentos_de_pecas_menu.perfil_30)
            self.troca_pagina = 1

        if self.troca_pagina == 2:
            self.label_imagem.move(230,90)
            self.label_titulo.setText("PERFIS DE ALUMÍNIO DE 40, 45 E 50")
            self.label_imagem.setPixmap(documentos_de_pecas_menu.perfil_45_2)
            self.troca_pagina = 22

        elif self.troca_pagina == 22:
            self.label_imagem.move(110,110)
            self.label_titulo.setText("PERFIL DE ALUMÍNIO DE 45x45")
            self.label_imagem.setPixmap(documentos_de_pecas_menu.perfil_45)
            self.troca_pagina = 2

        if self.troca_pagina == 3:
            self.label_imagem.move(110,90)
            self.label_titulo.setText("PERFIS DE ALUMÍNIO DE 60x60")
            self.label_imagem.setPixmap(documentos_de_pecas_menu.perfil_60)
            self.troca_pagina = 33

        elif self.troca_pagina == 33:
            self.label_imagem.move(110,90)
            self.label_titulo.setText("PERFIL DE ALUMÍNIO DE 60x60 L")
            self.label_imagem.setPixmap(documentos_de_pecas_menu.perfil_60L)
            self.troca_pagina = 3


################################ TELA DE DIAGRAMA ELÉTRICO ################################
class Diagrama_eletrico(QMainWindow, Ui_documentos_diagrama_eletrico): # Tela que contém o diagrama elétrico da máquina.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_home.clicked.connect(self.home)
        self.botao_seta_direita.clicked.connect(self.proxima_pagina)
        self.botao_seta_esquerda.clicked.connect(self.pagina_anterior)

        # ******************************* VARIÁVEIS *******************************

        self.contador = 1  # Contador que representa o número da página
        self.pagina1 = QPixmap("imagens/Diagrama_eletrico_01.png")
        self.pagina2 = QPixmap("imagens/Diagrama_eletrico_02.png")
        self.pagina3 = QPixmap("imagens/Diagrama_eletrico_03.png")

        # ******************************* CONFIGURAÇÕES *******************************

        self.label_imagem.setPixmap(self.pagina1)

        # ******************************* FUNÇÕES DA CLASSE *******************************

    def home(self): # Função que volta para o menu documentos.
        documentos_menu.show()
        diagrama_eletrico.hide()

    def proxima_pagina(self): # Função que muda a imagem do diagrama e o número da página (Próxima Página).
        if self.contador < 3:
            self.contador += 1

        if self.contador == 2:
            self.label_imagem.setPixmap(self.pagina2)
            self.label_paginas.setText("PÁGINA 02/03")

        if self.contador == 3:
            self.label_imagem.setPixmap(self.pagina3)
            self.label_paginas.setText("PÁGINA 03/03")

    def pagina_anterior(self): # Função que muda a imagem do diagrama e o número da página (Página Anterior).
        if self.contador > 1:
            self.contador -= 1

        if self.contador == 1:
            self.label_imagem.setPixmap(self.pagina1)
            self.label_paginas.setText("PÁGINA 01/03")

        if self.contador == 2:
            self.label_imagem.setPixmap(self.pagina2)
            self.label_paginas.setText("PÁGINA 02/03")

################################ TELA DE MAPA DE PERIGOS E RISCOS ################################
class Mapa_de_riscos(QMainWindow, Ui_mapa_de_riscos): # Tela que contém o mapa de perigos e riscos e as assinaturas dos responsáveis pelo setor.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_home.clicked.connect(self.home)
        self.botao_seta.clicked.connect(self.muda_pagina)

        # ******************************* VARIÁVEIS *******************************

        self.mapa_de_riscos_01 = QPixmap("imagens/Mapa_de_riscos_01.png")
        self.mapa_de_riscos_02 = QPixmap("imagens/Mapa_de_riscos_02.png")
        self.mapa_de_riscos_03 = QPixmap("imagens/Mapa_de_riscos_03.png")
        self.pagina = 2

    # ******************************* FUNÇÕES DA CLASSE *******************************

    def home(self): # Função que volta para o menu documentos.
        documentos_menu.show()
        mapa_de_riscos.hide()

    def muda_pagina(self): # Função que muda a página.
        if self.pagina == 1:
            self.label_imagem.setPixmap(self.mapa_de_riscos_01)
            self.pagina = 2

        elif self.pagina == 2:
            self.label_imagem.setPixmap(self.mapa_de_riscos_02)
            self.pagina = 3

        elif self.pagina == 3:
            self.label_imagem.setPixmap(self.mapa_de_riscos_03)
            self.pagina = 1

################################ TELA DE MENU DE REGISTROS ################################
class Registros_menu(QMainWindow, Ui_Registros_menu):# Tela que contém todos as liberações realizadas.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************
        self.botao_home.clicked.connect(self.home)
        self.botao_historico_utilizacao_01.clicked.connect(self.resgistros_de_uso)
        self.botao_historico_utilizacao_02.clicked.connect(self.resgistros_de_uso)
        self.botao_relatorio_defeitos_01.clicked.connect(self.registros_defeitos)
        self.botao_relatorio_defeitos_02.clicked.connect(self.registros_defeitos)
        # ******************************* VARIÁVEIS *******************************

        self.defeitos = False

        # ******************************* FUNÇÕES DA CLASSE *******************************


    def home(self): # Função que volta para o menu 01.
        standby.homeShow()
        registros_menu.hide()

    def resgistros_de_uso(self):  # Função que lista todos os registros.
        self.defeitos = False
        registro_historico_utilizacao.load_registros()
        registro_historico_utilizacao.show()
        registros_menu.hide()

    def registros_defeitos(self): # Função que lista apenas as liberações que deram "NÃO OK".
        self.defeitos = True
        registro_historico_utilizacao.load_registros()
        registro_historico_utilizacao.show()
        registros_menu.hide()

################################ TELA DE HISTÓRICO DE UTILIZAÇÃO  ################################
class Registro_historico_utilizacao(QMainWindow, Ui_cadastros_historico_utilizacao):
    # Tela que mostra o histórico de quem e quando foi utilizada a máquina.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_voltar.clicked.connect(self.voltar)
        self.botao_analisar.clicked.connect(self.analisar)

        # ******************************* CONFIGURAÇÕES *******************************

        # self.load_registros()

        # ******************************* FUNÇÕES DA CLASSE *******************************

    def analisar(self): # Função responsável por abrir a ficha da liberação selecionada pelo usuário.
        self.load_registros() # Carrega os registros

        try: # Pega os dados da linha selecionada.
            index = (self.tabela_utilizacao.selectionModel().currentIndex())
            row = self.tabela_utilizacao.currentItem().row()
            self.nome = index.sibling(row, 0).data()
            self.edv = index.sibling(row, 1).data()
            self.data = index.sibling(row, 2).data()
            self.horario = index.sibling(row, 3).data()
            self.resultado = index.sibling(row, 5).data()

        except Exception as erro:
            print(erro)

        if self.resultado == "NÃO OK": # Se a linha selecionada for um registro "NÃO OK":
            try:
                self.informacoes = banco_dados.retorna_descricao_registro(self.edv,self.horario,self.data) # Retorna os dados sobre a liberação selecionada (Data, Hora, Descrição...)

            except Exception as erro:
                print(erro)

            relatos_liberacao.label_nome.setText(f"NOME: {self.nome}")
            relatos_liberacao.label_data.setText(self.data)
            relatos_liberacao.label_periodo.setText(self.horario)

            try:
                relatos_liberacao.label_itens_nao_conformes.setText(self.informacoes[1])
                relatos_liberacao.lineEdit_descricao.setText(self.informacoes[0])

            except Exception as erro:
                print(erro)

            relatos_liberacao.voltar_registros_ou_liberacao = True
            relatos_liberacao.botao_finalizar.move(2000,0)
            relatos_liberacao.botao_cancelar.setText("VOLTAR")
            relatos_liberacao.botao_finalizar.setDisabled(True)
            relatos_liberacao.show()
            registro_historico_utilizacao.hide()

        else:
            pass
    def load_registros(self):# Função que carrega as configurações e dados da tabela de utilização.
        self.tabela_utilizacao.setColumnCount(6)
        self.tabela_utilizacao.setColumnWidth(0, 360)
        self.tabela_utilizacao.setColumnWidth(1, 150)
        self.tabela_utilizacao.setColumnWidth(2, 170)
        self.tabela_utilizacao.setColumnWidth(3, 180)
        self.tabela_utilizacao.setColumnWidth(4, 120)
        self.tabela_utilizacao.setColumnWidth(5, 200)

        self.tabela_utilizacao.setHorizontalHeaderLabels(["NOME", "EDV", "DATA", "HORA", "EXAME", "RESULTADO"])
        self.tabela_utilizacao.setSelectionBehavior(QAbstractItemView.SelectRows)

        try:
            registros = banco_dados.registrosList()
        except:
            registros = banco_dados.registrosList2()

        registros = list(registros)
        self.tabela_utilizacao.setRowCount(len(registros))
        row = 0

        for x in range(len(registros)):
            name = registros[x]['idAssociateFK']['name'].split(" ")
            name = name[0] + " " + name[-1]
            dataNascFormat = datetime.strptime(registros[x]['date'], '%Y-%m-%d')
            dataNascFormat2 = datetime.strftime(dataNascFormat, '%d/%m/%Y')
            horaInicial = registros[x]['InitialHour'].split(':')
            try:
                horaFinal = registros[x]['FinishHour'].split(':')
                horaFinal = horaFinal[0] + ":" + horaFinal[1]
            except:
                horaFinal = " "
            horaInicial = horaInicial[0] + ":" + horaInicial[1]

            hora = horaInicial + ' - ' + horaFinal
            exame = registros[x]['examA'] + ',' + registros[x]['examB']
            self.tabela_utilizacao.setItem(row, 0, QTableWidgetItem(name))
            try:
                self.tabela_utilizacao.setItem(row, 1, QTableWidgetItem(str((registros[x]['idAssociateFK']['EDV']))))
            except Exception as erro:
                print(f"{erro} AQUI02")
            self.tabela_utilizacao.setItem(row, 2, QTableWidgetItem(dataNascFormat2))
            self.tabela_utilizacao.setItem(row, 3, QTableWidgetItem(hora))
            self.tabela_utilizacao.setItem(row, 4, QTableWidgetItem((exame)))
            self.tabela_utilizacao.setItem(row, 5, QTableWidgetItem((registros[x]['result'])))
            #
            row = row + 1



        # row = 0

        # self.tabela_utilizacao.setItem(row, 0, QTableWidgetItem(0,str(self.hoje)))

    def voltar(self):# Função que volta para o menu registros.
        self.load_registros()
        registros_menu.show()
        registro_historico_utilizacao.hide()

################################ TELA DE MENU CADASTROS ################################
class Cadastros_menu(QMainWindow, Ui_cadastros_menu):# Tela de gerenciamento dos cadastros dos usuários, na qual é possível adicionar, editar e excluir.

    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* VARIÁVEIS *******************************
        self.imagem_aprendiz2 = QPixmap("imagens\Aprendiz_03.png")
        self.imagem_meio_oficial2 = QPixmap("imagens\Meio_oficial_03.png")
        self.imagem_manutentor2 = QPixmap("imagens\Manutentor_03.png")
        self.imagem_responsavel2 = QPixmap("imagens\Responsavel_03.png")

        self.nome = ""
        self.edv = ""
        self.classe = ""

        # ******************************* AÇÕES *******************************
        self.botao_voltar.clicked.connect(self.home)
        self.botao_adicionar.clicked.connect(self.adicionar_usuario)
        self.botao_editar.clicked.connect(self.editar)
        self.load_tabela()

    # ******************************* FUNÇÕES DA CLASSE *******************************
    def editar(self):# Função que abre e configura a tela de edição de usuário a partir da linha da tabela selecionada.
        self.load_tabela()

        try: # Coleta os dados da linha selecionada.
            index = (self.tabela.selectionModel().currentIndex())
            value = index.sibling(index.row(), index.column()).data()
            row = self.tabela.currentItem().row()
            col = self.tabela.currentItem().column()
            item = self.tabela.horizontalHeaderItem(col).text()
            value_02 = index.sibling(row + 1, index.column()).data()

            self.nome = index.sibling(row, 0).data()
            self.edv = index.sibling(row, 1).data()
            self.classe = index.sibling(row, 2).data()
            self.ID = banco_dados.edvColadorador
            self.skill = banco_dados.skill
            self.skill2 = banco_dados.skill2
            self.IDedit = banco_dados.idColadorador
            self.Data_Nascimento = banco_dados.busca_edv(self.edv)
            self.Data_Nascimento = self.Data_Nascimento[1]
            result = banco_dados.busca_edv(self.edv)
            dataNascFormat = datetime.strptime(self.Data_Nascimento, '%Y-%m-%d')
            dataNascFormat2 = datetime.strftime(dataNascFormat, '%d/%m/%Y')
            self.Data_Nascimento = dataNascFormat2
            cadastros_menu_adicionar.alterar_classe = True
            self.ficha()

        except:
            pass

    def ficha(self): # Configura a tela e as lineEdits com os dados do usuário.
        if self.classe == "Aprendiz":
            cadastros_menu_editar.label_imagem_patente.setPixmap(self.imagem_aprendiz2)
            cadastros_menu_editar.comboBox.setCurrentIndex(1)
            cadastros_menu_editar.jobPosition = 1

        if self.classe == "Meio_Oficial":
            cadastros_menu_editar.label_imagem_patente.setPixmap(self.imagem_meio_oficial2)
            cadastros_menu_editar.comboBox.setCurrentIndex(2)
            cadastros_menu_editar.jobPosition = 4

        if self.classe == "Responsável" or  self.classe == "Administrador":
            cadastros_menu_editar.label_imagem_patente.setPixmap(self.imagem_responsavel2)
            cadastros_menu_editar.comboBox.setCurrentIndex(4)
            cadastros_menu_editar.jobPosition = 3

        if self.classe == "Manutentor":
            cadastros_menu_editar.label_imagem_patente.setPixmap(self.imagem_manutentor2)
            cadastros_menu_editar.comboBox.setCurrentIndex(3)
            cadastros_menu_editar.jobPosition = 2

        cadastros_menu_editar.lineEdit_nome.setText(self.nome)
        cadastros_menu_editar.lineEdit_edv.setText(self.edv)
        cadastros_menu_editar.lineEdit_data_nascimento.setText(str(self.Data_Nascimento))

        if self.skill == True:
            cadastros_menu_editar.cbSkill.setChecked(True)

        elif self.skill2 == True:
            cadastros_menu_editar.cbSkill.setChecked(True)
            cadastros_menu_editar.cbSkill_2.setChecked(True)

        cadastros_menu_editar.show()
        cadastros_menu.hide()

    def load_tabela(self): # Carrega e configura a tabela de usuários com os dados do Banco de Dados.
        self.tabela.setColumnCount(3)
        self.tabela.setColumnWidth(0, 480)
        self.tabela.setColumnWidth(1, 150)
        self.tabela.setColumnWidth(2, 200)

        self.tabela.setHorizontalHeaderLabels(["NOME", "EDV", "CLASSE"])
        self.tabela.setSelectionBehavior(QAbstractItemView.SelectRows)

        listUser = banco_dados.todosUsers()
        self.tabela.setRowCount(len(listUser))

        row = 0
        for x in listUser:
            self.tabela.setItem(row, 0, QTableWidgetItem(x['name']))
            self.tabela.setItem(row, 1, QTableWidgetItem(x['EDV']))
            self.tabela.setItem(row, 2, QTableWidgetItem(x['jobposition']['typeJob']))

            row = row + 1

    def adicionar_usuario(self): # Função de inicia o processo de adicionar usuário.
        cadastros_menu_leitor.adicionar = True
        cadastros_menu_adicionar.alterar_classe = False
        cadastros_menu_adicionar.show()
        cadastros_menu.hide()

    def home(self): # Função que volta para o Menu 02.
        Menu02.show()
        cadastros_menu.hide()

################################ TELA DE EDIÇÃO DE USUÁRIO  ################################
class Cadastros_menu_editar(QMainWindow, Ui_Editar_cadastro): # Tela na qual os dados do usuário podem ser alterados ou excluir o
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_cancelar.clicked.connect(self.home)
        self.botao_alterar_tag_cartao.clicked.connect(self.leitor)
        self.botao_atualizar.clicked.connect(self.atualizar)

        # ******************************* CONFIGURAÇÕES *******************************
        self.lineEdit_nome.setText("")
        self.lineEdit_data_nascimento.setText("")
        self.lineEdit_edv.setText("")
        self.lineEdit_nome.setPlaceholderText("NOME COMPLETO")
        self.lineEdit_edv.setPlaceholderText("EDV")
        self.lineEdit_data_nascimento.setPlaceholderText("DATA DE NASCIMENTO")
        self.idcardEdit = ''

    # ******************************* FUNÇÕES DA CLASSE *******************************
    def leitor(self):# Função que abre a tela para alterar a tag do crachá.
        cadastros_menu_leitor.adicionar = False  # Variável que é utilizada para adicionar ou alterar a tag do usuário.
        cadastros_menu.ficha()
        cadastros_menu_leitor.opcao = False
        cadastros_menu_leitor.show()
        cadastros_menu_editar.hide()

    def home(self): # Função que volta para o menu de cadastros.
        cadastros_menu.show()
        cadastros_menu_editar.hide()

    def mudar_classe(self):  # Função que inicia o processo de mudar a classe do usuário.
        cadastros_menu_adicionar.show()
        cadastros_menu_editar.hide()

    def atualizar(self): # Função que atualiza os novos dados cadastrados nas lineEdits.
        self.nome = self.lineEdit_nome.text()
        self.data_nascimento = self.lineEdit_data_nascimento.text()
        self.edv = self.lineEdit_edv.text()
        self.skill = True
        self.skill2 = False
        self.admU = False
        self.idEdit = banco_dados.busca_edv(self.edv)
        self.jobPosition = cadastros_menu_editar.comboBox.currentText()
        classe = self.jobPosition.split(" ")

        if classe[-1] == "Aprendiz":
            self.jobPosition = 1
            self.admU = False

        elif classe[-1] == "Meio_Oficial":
            self.jobPosition = 4
            self.admU = False

        elif classe[-1] == "Responsável" or classe[-1] == "Administrador":
            self.jobPosition = 3
            self.admU = True

        elif classe[-1]== "Manutentor":
            self.jobPosition = 2
            self.admU = False
            self.skill2 = True

        url = banco_dados.url + 'associates/' + str(self.idEdit) + '/'

        body = {
            "name": self.nome,
            "EDV": self.edv,
            "skill": self.skill,
            "skill2": self.skill2,
            "adminU": self.admU,
            "birth": self.data_nascimento,
            "jobposition": self.jobPosition
        }

        try:
            urlpost = requests.patch(url, json=body)

            if (urlpost.status_code == 200):
                cadastros_menu.load_tabela()
                cadastros_menu_editar.hide()
                cadastros_menu_leitor.adicionar = False
                cadastros_menu_leitor.opcao = False
                cadastros_menu.show()
        except:
            print(urlpost.status_code)

################################ TELA DE HISTÓRICO DE UTILIZAÇÃO  ################################
class Cadastros_menu_leitor(QMainWindow, Ui_Aproxime_cartao):# Tela de alterar ou adicionar a tag do cartão.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* VARIÁVEIS *******************************
        self.adicionar = bool
        self.tag_cartao = " "

        # ******************************* CONFIGURAÇÕES *******************************
        self.lineEdit_tag_cartao.setText("")
        self.lineEdit_tag_cartao.setFocus()

        # ******************************* AÇÕES *******************************
        self.botao_cancelar.clicked.connect(self.voltar)
        self.botao_registrar.clicked.connect(self.registrar)

        # ******************************* FUNÇÕES DA CLASSE *******************************

    def voltar(self): # Função de voltar.
        if self.adicionar == True: # Se for o processo de adicionar volta para a tela de adicionar.
            cadastros_menu_adicionar_ficha_01.show()
            cadastros_menu_leitor.hide()

        else: # Se for o processo de editar volta para a tela de editar usuario.
            cadastros_menu_editar.show()
            cadastros_menu_leitor.hide()

    def registrar(self): # Termina o processo de adicionar usuário ou apenas altera a tag do cartão se for o processo de editar.
        self.tag_cartao = self.lineEdit_tag_cartao.text()
        if not self.tag_cartao == "":
            if self.adicionar == True:
                cadastros_menu_leitor.hide()
                banco_dados.adicionar_cadastro(self.tag_cartao, cadastros_menu_adicionar_ficha_01.nome, cadastros_menu_adicionar_ficha_01.classe, cadastros_menu_adicionar_ficha_01.edv, cadastros_menu_adicionar_ficha_01.data_nascimento)
                # usuario_registrado.show()
                cadastros_menu.show()
                # AQUI FALTA O DELAY ENTRE AS TELAS
                # usuario_registrado.hide()
                self.lineEdit_tag_cartao.setText("")
                cadastros_menu_adicionar_ficha_01.lineEdit_edv.setText("")
                cadastros_menu_adicionar_ficha_01.lineEdit_nome.setText("")
                cadastros_menu_adicionar_ficha_01.lineEdit_data_nascimento.setText("")
                cadastros_menu_leitor.hide()
                cadastros_menu.load_tabela()
                self.lineEdit_tag_cartao.setFocus()

            else: # Alterar tag do cartão
                self.lineEdit_tag_cartao.setFocus()
                if banco_dados.update_tag(self.tag_cartao,  cadastros_menu_editar.lineEdit_edv.text()) == True:
                    cadastros_menu.load_tabela()
                    cadastros_menu.show()
                    cadastros_menu_leitor.hide()


        else:
            print("Tente novamente")

################################ TELA DE ADICIONAR CADASTRO  ################################
class Cadastros_menu_adicionar(QMainWindow, Ui_cadastros_classes): # Tela de selecionar a classe do colaborador.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_voltar.clicked.connect(self.home)
        self.botao_aprendiz.clicked.connect(self.aprendiz)
        self.botao_meio_oficial.clicked.connect(self.meio_oficial)
        self.botao_manutentor.clicked.connect(self.manutentor)
        self.botao_responsavel.clicked.connect(self.responsavel)

        # ******************************* VARIÁVEIS *******************************

        self.imagem_aprendiz = QPixmap("imagens\Aprendiz_02.png")
        self.imagem_meio_oficial = QPixmap("imagens\Meio_oficial_02.png")
        self.imagem_manutentor = QPixmap("imagens\Manutentor_02.png")
        self.imagem_responsavel = QPixmap("imagens\Responsavel_02.png")
        self.alterar_classe = False

    # ******************************* FUNÇÕES DA CLASSE *******************************

    def aprendiz(self):  # Função de adicionar aprendiz.
        if self.alterar_classe == False:
            cadastros_menu_adicionar_ficha_01.classe = "Aprendiz"
            cadastros_menu_adicionar_ficha_01.label_imagem_classe.setPixmap(self.imagem_aprendiz)
            cadastros_menu_adicionar_ficha_01.show()
            cadastros_menu_adicionar.hide()

        else:
            try:
                cadastros_menu_editar.label_imagem_patente.setPixmap(cadastros_menu.imagem_aprendiz2)
                cadastros_menu_editar.show()
                cadastros_menu_adicionar.hide()
                cadastros_menu.load_tabela()

            except Exception as erro:
                print(erro)

    def meio_oficial(self): # Função de adicionar meio oficial.
        if self.alterar_classe == False:
            cadastros_menu_adicionar_ficha_01.classe = "Meio_Oficial"
            cadastros_menu_adicionar_ficha_01.label_imagem_classe.setPixmap(self.imagem_meio_oficial)
            cadastros_menu_adicionar_ficha_01.show()
            cadastros_menu_adicionar.hide()

        else:
            try:
                cadastros_menu_editar.label_imagem_patente.setPixmap(cadastros_menu.imagem_meio_oficial2)
                cadastros_menu_editar.show()
                cadastros_menu_adicionar.hide()
                cadastros_menu.load_tabela()

            except Exception as erro:
                print(erro)

    def manutentor(self): # Função de adicionar manutentor.
        if self.alterar_classe == False:
            cadastros_menu_adicionar_ficha_01.classe = "Manutentor"
            cadastros_menu_adicionar_ficha_01.label_imagem_classe.setPixmap(self.imagem_manutentor)
            cadastros_menu_adicionar_ficha_01.show()
            cadastros_menu_adicionar.hide()

        else:
            try:
                cadastros_menu_editar.label_imagem_patente.setPixmap(cadastros_menu.imagem_manutentor2)
                cadastros_menu_editar.show()
                cadastros_menu_adicionar.hide()
                cadastros_menu.load_tabela()

            except Exception as erro:
                print(erro)

    def responsavel(self):  # Função de adicionar responsável
        if self.alterar_classe == False:
            cadastros_menu_adicionar_ficha_01.classe = "Responsável"
            cadastros_menu_adicionar_ficha_01.label_imagem_classe.setPixmap(self.imagem_responsavel)
            cadastros_menu_adicionar_ficha_01.show()
            cadastros_menu_adicionar.hide()

        else:
            try:
                cadastros_menu_editar.label_imagem_patente.setPixmap(cadastros_menu.imagem_responsavel2)
                cadastros_menu_editar.show()
                cadastros_menu_editar.hide()
                cadastros_menu.load_tabela()

            except Exception as erro:
                print(erro)

    def home(self): # Função de voltar para menu de cadastros.
        cadastros_menu.show()
        cadastros_menu_adicionar.hide()

################################ TELA DE ADICIONAR OS DADOS DO NOVO USUÁRIO ################################
class Cadastros_menu_adicionar_ficha01(QMainWindow, Ui_cadastros_adicionar_ficha01): # Tela de preencher os dados do novo usuário, Nome, Edv e Data de nascimento.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************
        self.botao_cancelar.clicked.connect(self.home)
        self.botao_avancar.clicked.connect(self.cadastro)

        # ******************************* VARIAVEIS *******************************
        self.classe = " "
        self.data_nascimento = " "
        self.edv = " "
        self.nome = " "

        # ******************************* CONFIGURAÇÕES *******************************
        self.lineEdit_nome.setText("")
        self.lineEdit_data_nascimento.setText("")
        self.lineEdit_edv.setText("")
        self.lineEdit_nome.setPlaceholderText("NOME COMPLETO")
        self.lineEdit_edv.setPlaceholderText("EDV")
        self.lineEdit_data_nascimento.setPlaceholderText("DATA DE NASCIMENTO")

    # ******************************* FUNÇÕES DA CLASSE *******************************
    def cadastro(self): #Função que valida os dados escritos para passar para a tela do leitor.
        self.nome = self.lineEdit_nome.text()
        self.edv = str(self.lineEdit_edv.text())
        self.data_nascimento = self.lineEdit_data_nascimento.text()

        if (self.nome == "") or (self.edv == "") or (self.data_nascimento == ""):
            print("Tente novamente")

        else:
            cadastros_menu_leitor.opcao = True
            cadastros_menu_leitor.show()
            cadastros_menu_adicionar_ficha_01.hide()

    def home(self): #Função de voltar para a tela de escolher classes.
        cadastros_menu_adicionar.show()
        cadastros_menu_adicionar_ficha_01.hide()

################################ TELA DE USUÁRIO CADASTRADO ################################
class Usuario_registrado(QMainWindow, Ui_Usuario_registrado):  # Tela que retorna que o usuário foi adicionado no banco. (Ainda não estamos usando, falta a thread)
    def __init__(self):
        super().__init__()
        super().setupUi(self)

################################ TELA DE MANUTENÇÃO ################################
class Manutencao(QMainWindow, Ui_Manutencao): # Tela de manutenção, na qual é possível fazer testes com os componentes eletrônicos e controlar o estado de manutenção da máquina.
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_home.clicked.connect(self.home)
        self.botao_energizar_contator_1.clicked.connect(self.energizar_maquina)
        self.botao_energizar_contator_2.clicked.connect(self.energizar_maquina)
        self.botao_liberar_trava1.clicked.connect(self.liberar_trava)
        self.botao_liberar_trava2.clicked.connect(self.liberar_trava)
        self.botao_maquina_manutencao.clicked.connect(self.maquina_em_manutencao)

        # ******************************* VARIÁVEIS *******************************
        self.cadeado_normal = QIcon("imagens/CADEADO_FECHADO.png")
        self.cadeado_aberto = QIcon("imagens/CADEADO_ABERTO.png")
        self.cadeado_manutencao = QIcon("imagens/Cadeado_manutencao.png")
        self.painel_liberado = False
        self.painel_energizado = False

        if reqManutencao.verifica_estado_de_manutencao(serra_de_perfil) == True:
            self.estado_manutencao = True

        else:
            self.estado_manutencao = False

        self.maquina_em_manutencao()

    # ******************************* FUNÇÕES DA CLASSE *******************************
    def energizar_maquina(self): # Função para energizar o contatorl, dessa forma, liberando a alimentação da máquina.
        if self.painel_energizado == False:
            self.painel_energizado = True
            self.label_raio.setStyleSheet(
                "border-style: outset;\n" "color: rgb(0, 0, 0);\n" "border-color: rgb(0, 0, 0);\n" "border-width:6px;\n" "font: 75 34pt \"Bosch Sans Bold\";\n"
                "background-color: rgb(255,207,0);")
            self.botao_energizar_contator_2.setStyleSheet(
                "border-style: outset;\n" "border-color: rgb(0, 0, 0);\n" "border-width:7px;\n" "border-radius: 0px;\n"
                "background-color: rgb(237, 0, 7);")
            #GPIO.output(Alimentacao_maquina, True)
        else:
            self.painel_energizado = False
            self.label_raio.setStyleSheet(
                "border-style: outset;\n" "color: rgb(0, 0, 0);\n" "border-color: rgb(0, 0, 0);\n" "border-width:6px;\n" "font: 75 34pt \"Bosch Sans Bold\";\n"
                "background-color: rgb(255,255,255);")
            self.botao_energizar_contator_2.setStyleSheet(
                "border-style: outset;\n" "border-color: rgb(0, 0, 0);\n" "border-width:7px;\n" "border-radius: 0px;\n"
                "background-color: rgb(255, 255, 255);")
            #GPIO.output(Alimentacao_maquina, False)

    def liberar_trava(self): # Função de liberar a trava do painel elétrico da máquina.
        if self.painel_liberado == False:
            self.painel_liberado = True
            self.botao_liberar_trava2.setStyleSheet(
                "border-style: outset;\n" "border-color: rgb(0, 0, 0);\n" "border-width:7px;\n" "border-radius: 0px;\n"
                "background-color: rgb(237, 0, 7);")
            self.label_trava_solenoide.move(330, 565)
            #GPIO.output(trava_do_painel, True)
        else:
            self.painel_liberado = False
            self.botao_liberar_trava2.setStyleSheet(
                "border-style: outset;\n" "border-color: rgb(0, 0, 0);\n" "border-width:7px;\n" "border-radius: 0px;\n"
                "background-color: rgb(255, 255, 255);")
            self.label_trava_solenoide.move(370, 565)
            #GPIO.output(trava_do_painel, False)

    def maquina_em_manutencao(self):  # Função alterar o estado de manutenção da máquina.
        if self.estado_manutencao == False:
            reqManutencao.estado_manutencao(self.estado_manutencao, serra_de_perfil)
            self.estado_manutencao = True # Variável estado de manutenção.
            if banco_dados.statusMachine() == True: #Configurações do botão de manutenção:
                Menu01.Botao_Liberar_Maquina.setIcon(self.cadeado_aberto)
            else:
                Menu01.Botao_Liberar_Maquina.setIcon(self.cadeado_normal)
            Menu01.Botao_Liberar_Maquina.setIconSize(QtCore.QSize(220, 220))
            self.label_sim_nao.move(580, 500)
            self.botao_maquina_manutencao.move(790, 500)
            self.label_sim_nao.setText("NÃO")
            self.label_sim_nao.setStyleSheet(
                "border-style: outset;\n" "color: rgb(0, 0, 0);\n" "border-color: rgb(0, 0, 0);\n" "border-width:6px;\n" "border-radius: 0px;\n" "\n" "font: 75 55pt \"Bosch Sans Bold\";\n"
                "background-color: rgb(0, 136, 74);")
            self.label_painel_eletrico.setStyleSheet(
                "\n" "color: rgb(0, 0, 0);\n" "border-color: rgb(0, 0, 0);\n" "border-radius: 90px;\n" "font: 75 28pt \"Bosch Sans Bold\";\n"
                "background-color: rgb(138, 144, 151);")
            self.label_fundo_painel.setStyleSheet(
                "border-style: outset;\n" "color: rgb(0, 0, 0);\n" "border-color: rgb(0, 0, 0);\n" "border-width:6px;\n" "border-radius: 90px;\n" "font: 75 34pt \"Bosch Sans Bold\";\n"
                "background-color: rgb(138, 144, 151);")
            #GPIO.output(led_manutencao, False)

        else:
            reqManutencao.estado_manutencao(self.estado_manutencao, serra_de_perfil)
            self.estado_manutencao = False # Variável estado de manutenção.
            Menu01.Botao_Liberar_Maquina.setIcon(self.cadeado_manutencao) #Configurações do botão de manutenção:
            Menu01.Botao_Liberar_Maquina.setIconSize(QtCore.QSize(231, 231))
            self.label_sim_nao.move(970, 500)
            self.botao_maquina_manutencao.move(580, 500)
            self.label_sim_nao.setText("SIM")
            self.label_sim_nao.setStyleSheet(
                "border-style: outset;\n" "color: rgb(0, 0, 0);\n" "border-color: rgb(0, 0, 0);\n" "border-width:6px;\n" "border-radius: 0px;\n" "\n" "font: 75 55pt \"Bosch Sans Bold\";\n"
                "background-color: rgb(237, 0, 7);")
            self.label_painel_eletrico.setStyleSheet(
                "\n" "color: rgb(0, 0, 0);\n" "border-color: rgb(0, 0, 0);\n" "border-radius: 90px;\n" "font: 75 28pt \"Bosch Sans Bold\";\n"
                "background-color: rgb(237, 0, 7);")
            self.label_fundo_painel.setStyleSheet(
                "border-style: outset;\n" "color: rgb(0, 0, 0);\n" "border-color: rgb(0, 0, 0);\n" "border-width:6px;\n" "border-radius: 90px;\n" "font: 75 34pt \"Bosch Sans Bold\";\n"
                "background-color: rgb(237, 0, 7);")

            #GPIO.output(led_manutencao, True)
            # GPIO.output(Alimentacao_maquina, False)
    def home(self): # Função que volta para o Menu 02.
        standby.homeShow()
        manutencao.hide()

################################ CLASSE QUE REGISTRA NO BANCO UMA MANUTENÇÃO  ################################
class RequestManutencao():
    def verifica_estado_de_manutencao(self, id_maquina):
        urlManutencao = banco_dados.url + 'maintenances/' + id_maquina + '/1/'
        self.idMaint = ''
        try:
            urlget = requests.get(urlManutencao)
            json = urlget.json()
            if len(json) != 0:
                self.idMaint = json[0]['id']
                return True
            else:
                return False

        except:
            print(urlget.status_code)

    def estado_manutencao(self, bool, maquina):
        self.verifica_estado_de_manutencao(maquina)
        postManutencao = banco_dados.url + 'maintenances/'
        data = datetime.today().strftime('%Y-%m-%d')
        hora = datetime.today().strftime('%H:%M:%S')

        if(bool == True):
            bool = 1
            body = [{
                "date": data,
                "Initialhour": hora,
                "Finishhour": None,
                "statusMaint": bool,
                "idMachineFK": maquina,
                "idAssociateFK": banco_dados.idColadorador,
            }]
            postMachine = banco_dados.url + 'machines/' + serra_de_perfil + '/'
            patchMachine = {
                "statusMaint": True
            }
            try:
                post = requests.post(postManutencao, json=body)
                urlPatch = requests.patch(postMachine, patchMachine)
                idMaint = post.json()

            except:
                print('error')

        else:
            bool = 0
            hora = datetime.today().strftime('%H:%M:%S')
            patch = {
                "Finishhour": hora,
                "statusMaint": bool
            }
            postManutencao = banco_dados.url + 'maintenances/' + str(self.idMaint) + '/'
            postMachine = banco_dados.url + 'machines/' + serra_de_perfil + '/'

            patchMachine = {
                "statusMaint": False
            }
            try:
                urlPut = requests.patch(postManutencao, patch)
                urlPatch = requests.patch(postMachine, patchMachine)
            except:
                print("erro")

        return print("Mudou")

os.environ['NO_PROXY'] = 'localhost'
ap = QApplication(sys.argv)
ap.setStyle("Fusion")
banco_dados = Connection("Banco.db")
Menu01 = Primeiro_Menu()
Menu02 = Segundo_Menu()
Menu01Aprendiz = Primeiro_MenuAPRENDIZ()
Menu01_skill2 = Primeiro_MenuSkill()
liberacao_seguranca = Liberacao_seguranca()
liberacao_atencao = Liberacao_atencao()
liberacao_meio_ambiente = Liberacao_meio_ambiente()
documentos_menu = Documentos_menu()
documentos_de_pecas_menu = Documentos_documentos_de_pecas_menu()
perfil_de_aluminio = Documentos_de_peca_perfil_de_aluminio()
diagrama_eletrico = Diagrama_eletrico()
reqManutencao = RequestManutencao()
manutencao = Manutencao()
mapa_de_riscos = Mapa_de_riscos()
aviso_liberacao = Aviso_liberacao()
interface_menu = Interface_didatica_menu()
interface_menu_botoes = Interface_botoes()
interface_menu_finalidade = Interface_finalidade()
interface_menu_botao_emergencia = Interface_botao_emergencia()
registros_menu = Registros_menu()
cadastros_menu = Cadastros_menu()
cadastros_menu_editar = Cadastros_menu_editar()
cadastros_menu_leitor = Cadastros_menu_leitor()
cadastros_menu_adicionar = Cadastros_menu_adicionar()
cadastros_menu_adicionar_ficha_01 = Cadastros_menu_adicionar_ficha01()
usuario_registrado = Usuario_registrado()
registro_historico_utilizacao = Registro_historico_utilizacao()
sairDef = Sair()
relatos_liberacao = Relatos_liberacao()
cadastro = Adicionar()
standby = Standby()
standby.show()
sys.exit(ap.exec())
