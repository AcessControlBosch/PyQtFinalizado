import requests
from datetime import datetime
from socket import gethostname
import socket
def getData():

    # print('hostname:', socket.gethostname())
    #
    # # print(socket.SocketType)
    # #
    # url = requests.get('http://localhost:8000/usersid/412177/')
    # print(url)
    #
    # urll = 'http://localhost:8000/users/'
    # urll2 = 'http://localhost:8000/users/11/'
    #
    # body = [{
    #         "name": "Testee teste",
    #         "EDV": "5478134",
    #         "id_card": "554546"
    # }]
    #
    #
    # url2 = requests.post(urll, json = body )
    #
    # print(url2.status_code)
    #
    # put = {
    #     "name": "Teste",
    #     "EDV": "8748545"
    # }
    # #
    # url3 = requests.put(urll2, json = put)
    # print(url3.status_code)
    #
    # print(datetime.today().strftime('%Y-%m-%d'))
    # data = datetime.today().strftime('%Y-%m-%d')
    # hora = datetime.today().strftime('%H:%M:%S')
    # print(datetime.today().strftime('%H:%M:%S'))

    # url = 'http://localhost:8000/releasemachines/'
    #
    # body = [{
    #     "date": data,
    #     "hour": hora,
    #     "idMachineFK": "1",
    #     "idAssociateFK": "11"
    # }]
    #
    # url2 = requests.post(url, json = body )

    # urlMachine = 'http://lo' \
    #              'calhost:8000/machines/2/'
    # false = False
    # put = {
    #     "name": "teste",
    #     "description": "tesete",
    #     "status": false,
    #     "ipaddress": "12"
    # }
    #
    # urlPut = requests.put(urlMachine, json=put)
    #
    # print(urlPut.status_code)
    # urlMachine = 'http://localhost:8000/machines/1/'
    #
    # put = {
    #     "name": "teste",
    #     "description": "tesete",
    #     "status": True,
    #     "ipaddress": "12",
    #     "statusmaint": True
    # }
    #
    # urlPut = requests.put(urlMachine, json=put)
    #
    # print(urlPut.status_code)
    #
    # data = datetime.today().strftime('%Y-%m-%d')
    # hora = datetime.today().strftime('%H:%M:%S:%f')
    #
    #
    # print(data,hora)
    # url = 'http://localhost:8000/releasemachines/'
    #
    # body = [{
    #     "date": data,
    #     "hour": hora,
    #     "hourFinish": None,
    #     "idMachineFK": "1",
    #     "idAssociateFK": 4
    # }]
    #
    # urlpost = requests.post(url, json=body)
    # print(urlpost.status_code)

    # urlMachine = 'http://192.168.88.108:8000/machines/1/'
    #
    # patch2 = {
    #     "status": False,
    # }
    #
    # urlPut = requests.patch(urlMachine, patch2)
    #
    # print('patch Desl', urlPut)

    # # print(socket.gethostbyaddr)
    # datanasc = '28/09/2022'
    # print('1:', type(datanasc))
    # dataNascFormat = datetime.strptime(datanasc, '%d/%m/%Y').date()
    # print('2:', type(dataNascFormat))
    # dataNascFormat = datetime.strftime(dataNascFormat, '%Y-%m-%d')
    # print('2:', type(dataNascFormat))
    # print('3:', dataNascFormat)

    # url = 'http://localhost:8000/releasemachines/'
    #
    # body = [{
    #     "date": '2022-11-13',
    #     "InitialHour": "10:24:58.444417",
	# 	"FinishHour": "14:21:00",
	# 	"idMachineFK": 1,
	# 	"idAssociateFK": 1
    # }]
    #
    # urlpost = requests.post(url, json=body)
    #
    # print(urlpost.headers)
    # print(urlpost.json())
    #
    # urlID = urlpost.json()
    # print(urlID[0]['id'])

    # data = datetime.today().strftime('%Y-%m-%d')
    # hora = datetime.today().strftime('%H:%M:%S:%f')
    #
    # body = [{
    #     "date": data,
    #     "hour": hora,
    #     "description": 'descricao',
    #     "idMachineFK": 1,
    #     "idAssociateFK": 1
    # }]
    #
    # url = 'http://localhost:8000/observations/'
    #
    # urlRelato = requests.post(url,json=body)
    # print(urlRelato.status_code)

    self.returnDesc = self.url + 'getreleasemachinesanalise/' + str(self.idValue) + '/'

    self.requestsDesc = requests.get(self.returnDesc).json()
    print('--------------------- ANALISE ---------------')
    print(self.returnDesc)


getData()