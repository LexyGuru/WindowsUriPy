import os
import lang
import logo



class winmod():
    def accs():
        accs = [
            "ms-settings:workplace",
            "ms-settings:emailandaccounts",
            "ms-settings:otherusers",
            "ms-settings:assignedaccess",
            "ms-settings:signinoptions",
            "ms-settings:sync",
            "ms-settings:signinoptions-launchfaceenrollment",
            "ms-settings:yourinfo"
        ]

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

    def app():
        # Settings page	URI
        # Apps & Features	ms-settings:appsfeatures
        # App features	ms-settings:appsfeatures-app (Reset, manage add-on & downloadable content, etc. for the app)
        # Apps for websites	ms-settings:appsforwebsites
        # Default apps	ms-settings:defaultapps
        # Manage optional features	ms-settings:optionalfeatures
        # Offline Maps	ms-settings:maps
        # Startup apps	ms-settings:startupapps0
        # Video playback	ms-settings:videoplayback

        apps = [
            "ms-settings:appsfeatures",
            "ms-settings:appsforwebsites",
            "ms-settings:defaultapps",
            "ms-settings:optionalfeatures",
            "ms-settings:maps",
            "ms-settings:startupapps",
            "ms-settings:videoplayback"
        ]

        print("------------------------------------------")
        print(*lang.app, sep="\n")
        print("\n")

        app_lista = apps[int(input("" + lang.langs['main'][6]))]

        if app_lista == apps[0]:
            os.system("start " + app_lista)
            import main
            main.starter.start()

        if app_lista == apps[1]:
            os.system("start " + app_lista)
            import main
            main.starter.start()

        if app_lista == apps[2]:
            os.system("start " + app_lista)
            import main
            main.starter.start()

        if app_lista == apps[3]:
            os.system("start " + app_lista)
            import main
            main.starter.start()

        if app_lista == apps[4]:
            os.system("start " + app_lista)
            import main
            main.starter.start()

        if app_lista == apps[5]:
            os.system("start " + app_lista)
            import main
            main.starter.start()

        if app_lista == apps[6]:
            os.system("start " + app_lista)
            import main
            main.starter.start()
#é
#ó
#á