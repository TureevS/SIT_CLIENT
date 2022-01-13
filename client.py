import requests
import json


class Client:
    header = ''

    def __init__(self, username, password):
        user = {'username': f'{username}', 'password': f'{password}'}
        rsp = requests.post('http://128.199.122.96/authentication', data=user)
        if rsp.status_code == 200:
            js = json.loads(rsp.text)
            Client.header = {'Authorization': f"Bearer {js['token']}"}
            print(f"\n\tЗдравствуйте, {username}!")
        else:
            print("Ошибка", rsp.status_code)

    def get_doings(self):
        rsp = requests.get('http://128.199.122.96/todo', headers=Client.header)
        if rsp.status_code == 200:
            print(json.loads(rsp.text))
        else:
            print("Ошибка", rsp.status_code)

    def add_doings(self, doings):
        do = {'doings': f'{doings}'}
        rsp = requests.post('http://128.199.122.96/todo', data=do, headers=Client.header)
        if rsp.status_code == 200:
            print("\tЗадача успешно добавлена!")
        else:
            print("Ошибка", rsp.status_code)

    def update_doings(self, doings, id):
        do = {'doings': f'{doings}'}
        rsp = requests.put(f'http://128.199.122.96/todo/{id}', data=do, headers=Client.header)
        if rsp.status_code == 200:
            print("\tЗадача успешно изменена!")
        else:
            print("Ошибка", rsp.status_code)

    def delete_doings(self, id):
        rsp = requests.delete(f'http://128.199.122.96/todo/{id}', headers=Client.header)
        if rsp.status_code == 200:
            print("\tЗадача успешно удалена!")
        else:
            print("Ошибка", rsp.status_code)

    def upload_file(self, filename):
        file = {'file': open(filename, 'rb')}
        rsp = requests.post('http://128.199.122.96/files', files=file, headers=Client.header)
        if rsp.status_code == 200:
            print("\tФайл успешно добавлен!")
        else:
            print("Ошибка", rsp.status_code)

    def print_files(self):
        rsp = requests.get('http://128.199.122.96/files', headers=Client.header)
        if rsp.status_code == 200:
            print(json.loads(rsp.text))
        else:
            print("Ошибка", rsp.status_code)

    def download_file(self, filename):
        rsp = requests.get(f'http://128.199.122.96/files/{filename}', headers=Client.header)
        if rsp.status_code == 200:
            f = open(f'./{filename}', 'wb')
            f.write(rsp.content)
            f.close()
            print("\tФайл успешно скачан")
        else:
            print("Ошибка", rsp.status_code)

    def delete_file(self, filename):
        rsp = requests.delete(f'http://128.199.122.96/files/{filename}', headers=Client.header)
        if rsp.status_code == 200:
            print("\tФайл успешно удален!")
        else:
            print("Ошибка", rsp.status_code)
