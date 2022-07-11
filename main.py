import lang
import modul
from modul import *
import logo
import os


class starter():
    def start():
        logo.logos.main_logo()
        list = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20"
        ]
        print("------------------------------------------")
        print(*lang.lang, sep="\n")
        print("\n")

        main_lista = list[int(input("" + lang.langs['main'][6]))]

        if main_lista == list[0]:
            os.system('cls')
            logo.logos.main_logo()
            modul.winmod.accs()

        if main_lista == list[1]:
            print("1")
            starter.start()

        if main_lista == list[2]:
            print("2")
            starter.start()

        if main_lista == list[3]:
            print("3")
            starter.start()

        if main_lista == list[4]:
            print("4")
            starter.start()

        if main_lista == list[5]:
            print("5")
            starter.start()

        if main_lista == list[6]:
            print("6")
            starter.start()

        if main_lista == list[7]:
            print("7")
            starter.start()

        if main_lista == list[8]:
            print("8")
            starter.start()

        if main_lista == list[9]:
            print("9")
            starter.start()

        if main_lista == list[10]:
            print("10")
            starter.start()

        if main_lista == list[11]:
            print("11")
            starter.start()

        if main_lista == list[12]:
            print("12")
            starter.start()

        if main_lista == list[13]:
            print("13")
            starter.start()

        if main_lista == list[14]:
            print("14")
            starter.start()

        if main_lista == list[15]:
            print("15")
            starter.start()

        if main_lista == list[16]:
            print("16")
            starter.start()

        if main_lista == list[17]:
            print("17")
            starter.start()

        if main_lista == list[18]:
            print("18")
            starter.start()

        if main_lista == list[19]:
            exit

        if main_lista == list[20]:
            exit

starter.start()
