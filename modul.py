import os
import color_list
import lang


class win_mods:
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

        color_list.color_von()
        color_list.access_list_color()
        color_list.color_von()

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

    def app():
        apps = [
            "ms-settings:appsfeatures",
            "ms-settings:appsforwebsites",
            "ms-settings:defaultapps",
            "ms-settings:optionalfeatures",
            "ms-settings:maps",
            "ms-settings:startupapps",
            "ms-settings:videoplayback"
        ]

        color_list.color_von()
        color_list.apps_list_color()
        color_list.color_von()
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

    def cort():
        cortana = [
            "ms-settings:cortana-notifications",
            "ms-settings:cortana-moredetails",
            "ms-settings:cortana-permissions",
            "ms-settings:cortana-windowssearch",
            "ms-settings:cortana-talktocortana"
        ]

        color_list.color_von()
        color_list.cortana_list_color()
        color_list.color_von()
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

    def devi():
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

        color_list.color_von()
        color_list.devices_list_color()
        color_list.color_von()
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

    def ease():
        easee = ["ms-settings:easeofaccess-audio",
                 "ms-settings:easeofaccess-closedcaptioning",
                 "ms-settings:easeofaccess-colorfilter",
                 "ms-settings:easeofaccess-display",
                 "ms-settings:easeofaccess-eyecontrol",
                 "ms-settings:fonts",
                 "ms-settings:easeofaccess-highcontrast",
                 "ms-settings:easeofaccess-keyboard",
                 "ms-settings:easeofaccess-magnifier",
                 "ms-settings:easeofaccess-mouse",
                 "ms-settings:easeofaccess-mousepointer",
                 "ms-settings:easeofaccess-narrator",
                 "ms-settings:easeofaccess-speechrecognition",
                 "ms-settings:easeofaccess-cursor",
                 "ms-settings:easeofaccess-visualeffects"
            ]

        color_list.color_von()
        color_list.easee_list_color()
        color_list.color_von()
        print("\n")

        easee_lista = easee[int(input("" + lang.langs['main'][6]))]

        if easee_lista == easee[0]:
            os.system("start " + easee_lista)

        if easee_lista == easee[1]:
            os.system("start " + easee_lista)

        if easee_lista == easee[2]:
            os.system("start " + easee_lista)

        if easee_lista == easee[3]:
            os.system("start " + easee_lista)

        if easee_lista == easee[4]:
            os.system("start " + easee_lista)

        if easee_lista == easee[5]:
            os.system("start " + easee_lista)

        if easee_lista == easee[6]:
            os.system("start " + easee_lista)

        if easee_lista == easee[7]:
            os.system("start " + easee_lista)

        if easee_lista == easee[8]:
            os.system("start " + easee_lista)

        if easee_lista == easee[9]:
            os.system("start " + easee_lista)

        if easee_lista == easee[10]:
            os.system("start " + easee_lista)

        if easee_lista == easee[11]:
            os.system("start " + easee_lista)

        if easee_lista == easee[12]:
            os.system("start " + easee_lista)

        if easee_lista == easee[13]:
            os.system("start " + easee_lista)

        if easee_lista == easee[14]:
            os.system("start " + easee_lista)


