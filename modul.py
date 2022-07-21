import os
import color_list
import lang
from sty import ef, rs
from logo import *


class win_mods:

    @staticmethod
    def acs():
        os.system('cls')
        logos.main_logo()
        print(fg(255, 255, 0) + ef.italic + lang.langs['main'][0] + rs.italic + fg.rs)
        access = [
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

        access_lista = access[int(input(fg(255, 20, 147) + "" + lang.langs['main'][6] + fg.rs))]
        # access[int(input("" + lang.langs['main'][6]))]

        if access_lista == access[0]:
            os.system("start " + access_lista)

        if access_lista == access[1]:
            os.system("start " + access_lista)

        if access_lista == access[2]:
            os.system("start " + access_lista)

        if access_lista == access[3]:
            os.system("start " + access_lista)

        if access_lista == access[4]:
            os.system("start " + access_lista)

        if access_lista == access[5]:
            os.system("start " + access_lista)

        if access_lista == access[6]:
            os.system("start " + access_lista)

        if access_lista == access[7]:
            os.system("start " + access_lista)

    @staticmethod
    def app():
        os.system('cls')
        logos.main_logo()
        print(fg(255, 255, 0) + ef.italic + lang.langs['main'][0] + rs.italic + fg.rs)
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

        app_lista = apps[int(input(fg(255, 20, 147) + "" + lang.langs['main'][6] + fg.rs))]

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

    @staticmethod
    def cort():
        os.system('cls')
        logos.main_logo()
        print(fg(255, 255, 0) + ef.italic + lang.langs['main'][0] + rs.italic + fg.rs)
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

        cortana_lista = cortana[int(input(fg(255, 20, 147) + "" + lang.langs['main'][6] + fg.rs))]

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

    @staticmethod
    def devi():
        os.system('cls')
        logos.main_logo()
        print(fg(255, 255, 0) + ef.italic + lang.langs['main'][0] + rs.italic + fg.rs)
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

        devices_lista = devices[int(input(fg(255, 20, 147) + "" + lang.langs['main'][6] + fg.rs))]

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

    @staticmethod
    def ease():
        os.system('cls')
        logos.main_logo()
        print(fg(255, 255, 0) + ef.italic + lang.langs['main'][0] + rs.italic + fg.rs)
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

        easee_lista = easee[int(input(fg(255, 20, 147) + "" + lang.langs['main'][6] + fg.rs))]

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

    @staticmethod
    def extr():
        os.system('cls')
        logos.main_logo()
        print(fg(255, 255, 0) + ef.italic + lang.langs['main'][0] + rs.italic + fg.rs)
        extras = [
            "ms-settings:extras"
        ]

        color_list.color_von()
        color_list.extras_list_color()
        color_list.color_von()
        print("\n")

        extras_lista = extras[int(input(fg(255, 20, 147) + "" + lang.langs['main'][6] + fg.rs))]

        if extras_lista == extras[0]:
            os.system("start " + extras_lista)

    @staticmethod
    def game():
        os.system('cls')
        logos.main_logo()
        print(fg(255, 255, 0) + ef.italic + lang.langs['main'][0] + rs.italic + fg.rs)
        games = [
            "ms-settings:gaming-gamebar",
            "ms-settings:gaming-gamedvr",
            "ms-settings:gaming-gamemode",
            "ms-settings:quietmomentsgame",
            "ms-settings:gaming-trueplay"
        ]

        color_list.color_von()
        color_list.gaming_list_color()
        color_list.color_von()

        games_lista = games[int(input(fg(255, 20, 147) + "" + lang.langs['main'][6] + fg.rs))]

        if games_lista == games[0]:
            os.system("start " + games_lista)

        if games_lista == games[1]:
            os.system("start " + games_lista)

        if games_lista == games[2]:
            os.system("start " + games_lista)

        if games_lista == games[3]:
            os.system("start " + games_lista)

        if games_lista == games[4]:
            os.system("start " + games_lista)

    @staticmethod
    def home():
        os.system('cls')
        logos.main_logo()
        print(fg(255, 255, 0) + ef.italic + lang.langs['main'][0] + rs.italic + fg.rs)
        home = [
            "ms-settings:defaultbrowsersettings",
            "ms-settings:holographic-audio",
            "ms-settings:privacy-holographic-environment",
            "ms-settings:holographic-headset",
            "ms-settings:holographic-management",
            "ms-settings:holographic-startupandesktop"
        ]

        color_list.color_von()
        print(fg(255, 20, 147) + "" + lang.langs['main'][7] + fg.rs)
        color_list.color_von()
        color_list.home_list_color()
        color_list.color_von()
        print("\n")

        home_lista = home[int(input(fg(255, 20, 147) + "" + lang.langs['main'][6] + fg.rs))]

        if home_lista == home[0]:
            os.system("start " + home_lista)

        if home_lista == home[1]:
            os.system("start " + home_lista)

        if home_lista == home[2]:
            os.system("start " + home_lista)

        if home_lista == home[3]:
            os.system("start " + home_lista)

        if home_lista == home[4]:
            os.system("start " + home_lista)

        if home_lista == home[5]:
            os.system("start " + home_lista)
