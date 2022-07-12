import modul
from modul import *
import os
from logo import *


def main():
    os.system('cls')
    logos.main_logo('self')
    print(lang.langs['main'][0])
    """

    :rtype: object
    """
    lista = [
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

    main_lista = lista[int(input("" + lang.langs['main'][6]))]

    if main_lista == lista[0]:
        os.system('cls')
        modul.win_mods.accs('self')
        main()

    if main_lista == lista[1]:
        os.system('cls')
        modul.win_mods.app('self')
        main()

    if main_lista == lista[2]:
        print("2")
        main()

    if main_lista == lista[3]:
        print("3")
        main()

    if main_lista == lista[4]:
        print("4")
        main()

    if main_lista == lista[5]:
        print("5")
        main()

    if main_lista == lista[6]:
        print("6")
        main()

    if main_lista == lista[7]:
        print("7")
        main()

    if main_lista == lista[8]:
        print("8")
        main()

    if main_lista == lista[9]:
        print("9")
        main()

    if main_lista == lista[10]:
        print("10")
        main()

    if main_lista == lista[11]:
        print("11")
        main()

    if main_lista == lista[12]:
        print("12")
        main()

    if main_lista == lista[13]:
        print("13")
        main()

    if main_lista == lista[14]:
        print("14")
        main()

    if main_lista == lista[15]:
        print("15")
        main()

    if main_lista == lista[16]:
        print("16")
        main()

    if main_lista == lista[17]:
        print("17")
        main()

    if main_lista == lista[18]:
        print("18")
        main()

    if main_lista == lista[19]:
        main()

    if main_lista == lista[20]:
        os.system('cls')
        logos.main_logo('self')
        yn = input(lang.langs['main'][5] + ' (yes/no): ')
        if yn == 'yes':
            exit()
        else:
            main()


main()
