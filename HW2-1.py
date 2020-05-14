# То, что нужно проверить в ДЗ, лежит в строках 95 и 121.


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "passport", "number": "2435 8976 3213"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name():
    document_number = input('Введите номер документа: ')
    for doc in documents:
        if document_number == doc["number"]:
            print(doc["name"])
            break
    else:
        print('Такого документа не существует')


def get_shelf():
    document_number = input('Введите номер документа: ')
    for shelf, docs in directories.items():
        if document_number in docs:
            print(shelf)
            break
    else:
        print('Такого документа не существует')


def print_list():
    for doc in documents:
        print(doc["type"], doc["number"], doc["name"])


def add_document():
    user_type = input('Введите тип документа: ')
    user_number = input('Введите номер документа: ')
    user_name = input('Введите имя владельца документа: ')
    while True:
        user_shelf = input('Введите номер полки, на которой будет лежать документ: ')
        if user_shelf in directories:
            documents.append({"type": user_type, "number": user_number, "name": user_name})
            directories[user_shelf].append(user_number)
            break
        else:
            print('Полки, на которую вы пытаетесь добавить документ, не существует')
            continue


def delete_doc():
    document_number = input('Введите номер документа, который необходимо удалить: ')
    for doc in documents:
        if document_number == doc["number"]:
            documents.remove(doc)
            for shelf in directories:
                if document_number in directories[shelf]:
                    directories[shelf].remove(document_number)
                    break
            break
    else:
        print('Такого документа не существует')


def move_doc():
    user_doc = input('Введите номер документа, который хотите перенести: ')
    for shelf, docs in directories.items():
        if user_doc in docs:
            target_shelf = input('Введите номер полки, на который хотите перенести документ: ')
            if target_shelf in directories:
                docs.remove(user_doc)
                directories[target_shelf].append(user_doc)
                break
            else:
                print('Такой полки не существует')
                break
    else:
        print('Такого документа на полках нет')


def add_shelf():
    new_shelf = input('Введите номер новой полки: ')
    if new_shelf in directories:
        print('Такая полка уже есть')
    else:
        directories[new_shelf] = []


def print_name():     #Новая функция, добавленная в последнем ДЗ.
    for doc in documents:
        try:
            doc["name"]
        except KeyError:
            print('У документа под номером ' + doc["number"] + ' отсутствует присвоенное имя владельца')
        else:
            print(doc["name"])

def main():
    while True:
        command = input('Введите команду: ')
        if command == 'p':
            get_name()
        elif command == 's':
            get_shelf()
        elif command == 'l':
            print_list()
        elif command == 'a':
            add_document()
        elif command == 'd':
            delete_doc()
        elif command == 'm':
            move_doc()
        elif command == 'as':
            add_shelf()
        elif command == 'n':  #Добавленная в ДЗ функция
            print_name()
        else:
            print('Такой команды не существует')

main()
