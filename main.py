from client import Client
import requests


print("\t1 - Регистрация")
print("\t2 - Аутентификация")
print("\t0 = Выйти\n")
cmd = input("Введите команду: ")
while cmd != "0":
    if cmd == "1":
        username = input("\tПридумайте имя пользователя: ")
        password = input("\tПридумайте пароль: ")
        new_user = {'username': f'{username}', 'password': f'{password}'}
        rsp = requests.post('http://127.0.0.1:5000/user', data=new_user)
        if rsp.status_code == 200:
            print("\tВы успешно зарегистрировались!")
        else:
            print("Ошибка", rsp.status_code)
    elif cmd == "2":
        username = input("\tВведите имя пользователя: ")
        password = input("\tВведите пароль: ")
        client = Client(username, password)
        break
    else:
        print("Такой команды нет!")
    cmd = input("Введите команду: ")


print("\t1 - Получить список задач")
print("\t2 - Добавить задачу")
print("\t3 - Обновить задачу")
print("\t4 - Удалить задачу")
print("\t5 - Загрузить файл")
print("\t6 - Показать список файлов")
print("\t7 - Скачать файл")
print("\t8 - Удалить файл")
print("\t0 = Выйти\n")

cmd = input("Введите команду: ")
while cmd != "0":
    if cmd == "1":
        client.get_doings()
    elif cmd == "2":
        doings = input("\tДобавьте задачу: ")
        client.add_doings(doings)
    elif cmd == "3":
        id = input("\tКакую задачу вы хотите обновить?: ")
        doings = input("\tИзмените задачу: ")
        client.update_doings(doings, id)
    elif cmd == "4":
        id = input("\tКакую задачу вы хотите удалить?: ")
        client.delete_doings(id)
    elif cmd == "5":
        filename = input("\tВведите название файла, который вы хотите загрузить: ")
        client.upload_file(filename)
    elif cmd == "6":
        client.print_files()
    elif cmd == "7":
        filename = input("\tВведите название файла, который вы хотите скачать: ")
        client.download_file(filename)
    elif cmd == "8":
        filename = input("\tВведите название файла, который вы хотите удалить: ")
        client.delete_file(filename)
    else:
        print("Такой команды нет!")
    cmd = input("Введите команду: ")
