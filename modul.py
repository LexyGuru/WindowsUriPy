import os
import lang
import logo



class winmod():
    def accs():
        accs = ["ms-settings:workplace", "ms-settings:emailandaccounts", "ms-settings:otherusers",
                "ms-settings:assignedaccess", "ms-settings:signinoptions", "ms-settings:sync",
                "ms-settings:signinoptions-launchfaceenrollment", "ms-settings:yourinfo"]

        print("------------------------------------------")
        print(*lang.acc, sep="\n")
        print("\n")

        accs_lista = accs[int(input("" + lang.langs['main'][6]))]

        if accs_lista == accs[0]:
            os.system("start " + accs_lista)
            import main
            main.starter.start()

        if accs_lista == accs[1]:
            os.system("start " + accs_lista)
            import main
            main.starter.start()

        if accs_lista == accs[2]:
            os.system("start " + accs_lista)
            import main
            main.starter.start()

        if accs_lista == accs[3]:
            os.system("start " + accs_lista)
            import main
            main.starter.start()

        if accs_lista == accs[4]:
            os.system("start " + accs_lista)
            import main
            main.starter.start()

        if accs_lista == accs[5]:
            os.system("start " + accs_lista)
            import main
            main.starter.start()

        if accs_lista == accs[6]:
            os.system("start " + accs_lista)
            import main
            main.starter.start()

        if accs_lista == accs[7]:
            os.system("start " + accs_lista)
            import main
            main.starter.start()