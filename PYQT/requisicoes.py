import requests

def getData():
    url = requests.get('http://localhost:8000/users/465233/')
    print(url.status_code)

    if(url.status_code == 500):
        print('usuário não cadastrado')

    else:
        print('user cad')
        print(url.json())

getData()