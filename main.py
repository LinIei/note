import json
import datetime
import sys


class style:
    RESET = '\033[0m'
    BRIGHT = '\033[1m'
    DIM = '\033[2m'
    ITALICS = '\033[3m'
    LINED = '\033[4m'


def fopenR():
    with open("zametki.json", "r") as f:
        return json.load(f)


def fopenW(lst):
    with open('zametki.json', "w") as f:
        json.dump(lst, f, indent=2)


def dataToday():
    date = datetime.datetime.today()
    return date.strftime("%Y-%m-%d-%H.%M.%S")


def PrintLst(lst, i):
    print("Номер:", i + 1)
    print("Заголовок:", lst["header"])
    print("Заметка:", lst["note"])
    print("Дата:", lst["date"])
    print()


def styleText(tmp):
    styleTxt = input("Поменять стиль текста?\n1. Да\n2. Нет\n")
    if styleTxt == "1":
        print('1.Изменить стиль на курсив',
              '2.Изменить стиль на жирный',
              '3.Изменить стиль на блеклый',
              '4.Изменить стиль на подчеркнутый',
              '5.Изменить стиль на стандартный',
              sep='\n'
              )
        nStyle = int(input('Введите цифру: '))
        clStyle = style()
        match nStyle:
            case 1:
                tmp = clStyle.ITALICS + tmp + clStyle.RESET
            case 2:
                tmp = clStyle.BRIGHT + tmp + clStyle.RESET
            case 3:
                tmp = clStyle.DIM + tmp + clStyle.RESET
            case 4:
                tmp = clStyle.LINED + tmp + clStyle.RESET
            case 5:
                tmp = tmp.replace(clStyle.LINED, '')
                tmp = tmp.replace(clStyle.DIM, '')
                tmp = tmp.replace(clStyle.BRIGHT, '')
                tmp = tmp.replace(clStyle.ITALICS, '')
    return tmp


def isText():
    if input("Поменять текст?\n1. Да\n2. Нет\n") == "1":
        return True
    return False


def Search(lst, word):
    fl = False
    for i in range(len(lst)):
        if word in lst[i]["header"] or word in lst[i]["note"]:
            fl = True
            print("Номер " + str(i + 1) + "\n" + lst[i]["header"] + "\n" + lst[i]["note"] + "\n" + lst[i]["date"])
    return fl


index = 0
lst = []
lst = fopenR()
while True:
    print(
        "1. Добавить заметку",
        "2. Удалить заметку",
        "3. Вывести список всех заметок",
        "4. Редактировать заметку",
        "5. Поиск заметок по слову",
        "0. Закрыть",
        sep="\n"
    )
    try:
        menu = int(input())
    except ValueError:
        print("введено не число")
        print()
        continue
    print()
    if menu == 1:
        index += 1
        lst.append(
            {"header": input("Заголовок: "), "note": input("Заметка: "), "date": dataToday()})
        print()
    elif menu == 2:
        try:
            indexDel = int(input("Введите номер заметки для удаления "))
        except ValueError:
            print("введено не число")
            print()
        else:
            try:
                del lst[indexDel - 1]
            except IndexError:
                print("индекс не входит в диапазон элементов")
                print()
            else:
                print(indexDel, "заметка удалена")
                print()
    elif menu == 3:
        for i in range(len(lst)):
            PrintLst(lst[i], i)
    elif menu == 4:
        try:
            indexСhanges = int(input("Введите номер заметки для изменения "))
        except ValueError:
            print("введено не число")
            print()
            continue
        try:
            PrintLst(lst[indexСhanges - 1], indexСhanges - 1)
        except IndexError:
            print("индекс не входит в диапазон элементов")
            print()
        else:
            tmpS = input("Изменить:\n"
                         "1. Заголовок\n"
                         "2. Заметку\n"
                         "3. Все\n")
            if tmpS == "1":
                if isText():
                    lst[indexСhanges - 1]["header"] = input("Заголовок ")
                    lst[indexСhanges - 1]["date"] = dataToday()
                lst[indexСhanges - 1]["header"] = styleText(lst[indexСhanges - 1]["header"])
                PrintLst(lst[indexСhanges - 1], indexСhanges - 1)
            elif tmpS == "2":
                if isText():
                    lst[indexСhanges - 1]["note"] = input("Заметка \n")
                    lst[indexСhanges - 1]["date"] = dataToday()
                lst[indexСhanges - 1]["note"] = styleText(lst[indexСhanges - 1]["note"])
                PrintLst(lst[indexСhanges - 1], indexСhanges - 1)
            elif tmpS == "3":
                print("Изменение Заголовка:")
                if isText():
                    lst[indexСhanges - 1]["header"] = input("Заголовок ")
                    lst[indexСhanges - 1]["date"] = dataToday()
                lst[indexСhanges - 1]["header"] = styleText(lst[indexСhanges - 1]["header"])
                print()
                print("Изменение Заметки:")
                if isText():
                    lst[indexСhanges - 1]["note"] = input("Заметка \n")
                    lst[indexСhanges - 1]["date"] = dataToday()
                lst[indexСhanges - 1]["note"] = styleText(lst[indexСhanges - 1]["note"])
                PrintLst(lst[indexСhanges - 1], indexСhanges - 1)
    elif menu == 5:
        print("Введите слово ")
        word = input()
        if not Search(lst, word):
            print("Данного слова нет в заметках")
            print()
    else:
        break
fopenW(lst)
sys.exit("Программа завершена")
