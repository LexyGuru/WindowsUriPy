import os
import lang


class win_mods:
    def accs(self):
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
        print(*lang.access, sep="\n")
        print("\n")

        accs_lista = accs[int(input("" + lang.langs['main'][6]))]

        if accs_lista == accs[0]:
            os.system("start " + accs_lista)

        if accs_lista == accs[1]:
            os.system("start " + accs_lista)

        if accs_lista == accs[2]:
            os.system("start " + accs_lista)

        if accs_lista == accs[3]:
            os.system("start " + accs_lista)

        if accs_lista == accs[4]:
            os.system("start " + accs_lista)

        if accs_lista == accs[5]:
            os.system("start " + accs_lista)

        if accs_lista == accs[6]:
            os.system("start " + accs_lista)

        if accs_lista == accs[7]:
            os.system("start " + accs_lista)

    def app(self):
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
        print(*lang.apps, sep="\n")
        print("\n")

        app_lista = apps[int(input("" + lang.langs['main'][6]))]

        if app_lista == apps[0]:
            os.system("start " + app_lista)

        if app_lista == apps[1]:
            os.system("start " + app_lista)

        if app_lista == apps[2]:
            os.system("start " + app_lista)

        if app_lista == apps[3]:
            os.system("start " + app_lista)

        if app_lista == apps[4]:
            os.system("start " + app_lista)

        if app_lista == apps[5]:
            os.system("start " + app_lista)

        if app_lista == apps[6]:
            os.system("start " + app_lista)

    def cort(self):
        cortana = [
            "ms-settings:cortana-notifications",
            "ms-settings:cortana-moredetails",
            "ms-settings:cortana-permissions",
            "ms-settings:cortana-windowssearch",
            "ms-settings:cortana-talktocortana"
        ]

        print("------------------------------------------")
        print(*lang.cortana, sep="\n")
        print("\n")

        cortana_lista = cortana[int(input("" + lang.langs['main'][6]))]

        if cortana_lista == cortana[0]:
            os.system("start " + cortana_lista)

        if cortana_lista == cortana[1]:
            os.system("start " + cortana_lista)

        if cortana_lista == cortana[2]:
            os.system("start " + cortana_lista)

        if cortana_lista == cortana[3]:
            os.system("start " + cortana_lista)

        if cortana_lista == cortana[4]:
            os.system("start " + cortana_lista)

    def devi(self):
        devices = [
            "ms-settings:autoplay",
            "ms-settings:bluetooth",
            "ms-settings:camera",
            "ms-settings:mousetouchpad",
            "ms-settings:pen",
            "ms-settings:printers",
            "ms-settings:devices-touchpad",
            "ms-settings:devicestyping-hwkbtextsuggestions",
            "ms-settings:usb",
            "ms-settings:mobile-devices"
        ]

        print("------------------------------------------")
        print(*lang.devices, sep="\n")
        print("\n")

        devices_lista = devices[int(input("" + lang.langs['main'][6]))]

        if devices_lista == devices[0]:
            os.system("start " + devices_lista)

        if devices_lista == devices[1]:
            os.system("start " + devices_lista)

        if devices_lista == devices[2]:
            os.system("start " + devices_lista)

        if devices_lista == devices[3]:
            os.system("start " + devices_lista)

        if devices_lista == devices[4]:
            os.system("start " + devices_lista)

        if devices_lista == devices[5]:
            os.system("start " + devices_lista)

        if devices_lista == devices[6]:
            os.system("start " + devices_lista)

        if devices_lista == devices[7]:
            os.system("start " + devices_lista)

        if devices_lista == devices[8]:
            os.system("start " + devices_lista)

        if devices_lista == devices[9]:
            os.system("start " + devices_lista)

