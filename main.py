import modul
from modul import *
import os
from logo import *
from color import style


def main():
    os.system('cls')
    logos.main_logo('self')
    print(fg(255, 255, 0) + ef.italic + lang.langs['main'][0] + rs.italic + fg.rs)
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
    print(fg(255, 20, 147) + ef.italic + "------------------------------------------" + rs.italic + fg.rs)
    # print(*lang.lang, sep="\n")
    print(fg(0, 255, 250) + ef.italic + lang.lang[1], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 240) + ef.italic + lang.lang[2], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 230) + ef.italic + lang.lang[3], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 220) + ef.italic + lang.lang[4], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 210) + ef.italic + lang.lang[5], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 200) + ef.italic + lang.lang[6], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 190) + ef.italic + lang.lang[7], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 180) + ef.italic + lang.lang[8], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 170) + ef.italic + lang.lang[9], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 160) + ef.italic + lang.lang[10], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 150) + ef.italic + lang.lang[11], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 140) + ef.italic + lang.lang[12], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 130) + ef.italic + lang.lang[13], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 120) + ef.italic + lang.lang[14], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 110) + ef.italic + lang.lang[15], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 90) + ef.italic + lang.lang[16], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 80) + ef.italic + lang.lang[17], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 70) + ef.italic + lang.lang[18], sep="\n" + rs.italic + fg.rs)
    print(fg(255, 20, 147) + ef.italic + lang.lang[19], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 50) + ef.italic + lang.lang[20], sep="\n" + rs.italic + fg.rs)

    print("\n")

    main_lista = lista[int(input(fg(255, 20, 147) + "" + lang.langs['main'][6]  + fg.rs))]

    if main_lista == lista[0]:
        os.system('cls')
        modul.win_mods.accs('self')
        main()

    if main_lista == lista[1]:
        os.system('cls')
        modul.win_mods.app('self')
        main()

    if main_lista == lista[2]:
        os.system('cls')
        modul.win_mods.cort('self')
        main()

    if main_lista == lista[3]:
        os.system('cls')
        modul.win_mods.devi('self')
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


