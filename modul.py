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

    @staticmethod
    def net():
        os.system('cls')
        logos.main_logo()
        print(fg(255, 255, 0) + ef.italic + lang.langs['main'][0] + rs.italic + fg.rs)
        netw = [
            "ms-settings:network-status",
            "ms-settings:network-airplanemode",
            "ms-settings:network-cellular",
            "ms-settings:network-dialup",
            "ms-settings:network-directaccess",
            "ms-settings:network-ethernet",
            "ms-settings:network-wifisettings",
            "ms-settings:network-mobilehotspot",
            "ms-settings:network-proxy",
            "ms-settings:network-vpn",
            "ms-settings:network-wifi",
            "ms-settings:wifi-provisioning"
        ]

        color_list.color_von()
        print(fg(255, 20, 147) + "" + lang.langs['main'][7] + fg.rs)
        color_list.color_von()
        color_list.network_list_color()
        color_list.color_von()
        print("\n")

        netw_lista = netw[int(input(fg(255, 20, 147) + "" + lang.langs['main'][6] + fg.rs))]

        if netw_lista == netw[0]:
            os.system("start " + netw_lista)

        # NINCS BEFEJEZVE

    @staticmethod
    def pers():
        os.system('cls')
        logos.main_logo()
        print(fg(255, 255, 0) + ef.italic + lang.langs['main'][0] + rs.italic + fg.rs)
        person = [
            "ms-settings:personalization-background",
            "ms-settings:personalization-start-places",
            "ms-settings:colors",
            "ms-settings:personalization-glance",
            "ms-settings:lockscreen",
            "ms-settings:personalization-navbar",
            "ms-settings:personalization",
            "ms-settings:personalization-start",
            "ms-settings:taskbar",
            "ms-settings:personalization-touchkeyboard",
            "ms-settings:themes"
        ]

        color_list.color_von()
        print(fg(255, 20, 147) + "" + lang.langs['main'][7] + fg.rs)
        color_list.color_von()
        color_list.persona_list_color()
        color_list.color_von()
        print("\n")

        personal_lista = person[int(input(fg(255, 20, 147) + "" + lang.langs['main'][6] + fg.rs))]

        if personal_lista == person[0]:
            os.system("start " + personal_lista)

        # NINCS BEFEJEZVE


#Phone
#Settings page	URI
#Your phone	ms-settings:mobile-devices
#ms-settings:mobile-devices-addphone
#ms-settings:mobile-devices-addphone-direct (Opens Your Phone app)
#Device Usage	ms-settings:deviceusage

#Privacy
#Settings page	URI
#Accessory apps	ms-settings:privacy-accessoryapps (Deprecated in Windows 10, version 1809 and later)
#Account info	ms-settings:privacy-accountinfo
#Activity history	ms-settings:privacy-activityhistory
#Advertising ID	ms-settings:privacy-advertisingid (Deprecated in Windows 10, version 1809 and later)
#App diagnostics	ms-settings:privacy-appdiagnostics
#Automatic file downloads	ms-settings:privacy-automaticfiledownloads
#Background Apps	ms-settings:privacy-backgroundapps
#Background Spatial Perception	ms-settings:privacy-backgroundspatialperception
#Calendar	ms-settings:privacy-calendar
#Call history	ms-settings:privacy-callhistory
#Camera	ms-settings:privacy-webcam
#Contacts	ms-settings:privacy-contacts
#Documents	ms-settings:privacy-documents
#Downloads folder	ms-settings:privacy-downloadsfolder
#Email	ms-settings:privacy-email
#Eye tracker	ms-settings:privacy-eyetracker (requires eyetracker hardware)
#Feedback & diagnostics	ms-settings:privacy-feedback
#File system	ms-settings:privacy-broadfilesystemaccess
#General	ms-settings:privacy or ms-settings:privacy-general
#Graphics	ms-settings:privacy-graphicscaptureprogrammatic
#ms-settings:privacy-graphicscapturewithoutborder
#Inking & typing	ms-settings:privacy-speechtyping
#Location	ms-settings:privacy-location
#Messaging	ms-settings:privacy-messaging
#Microphone	ms-settings:privacy-microphone
#Motion	ms-settings:privacy-motion
#Music Library	ms-settings:privacy-musiclibrary
#Notifications	ms-settings:privacy-notifications
#Other devices	ms-settings:privacy-customdevices
#Phone calls	ms-settings:privacy-phonecalls
#Pictures	ms-settings:privacy-pictures
#Radios	ms-settings:privacy-radios
#Speech	ms-settings:privacy-speech
#Tasks	ms-settings:privacy-tasks
#Videos	ms-settings:privacy-videos
#Voice activation	ms-settings:privacy-voiceactivation

#Search
#Settings page	URI
#Search	ms-settings:search
#Search more details	ms-settings:search-moredetails
#Search Permissions	ms-settings:search-permissions

#Surface Hub
#Settings page	URI
#Accounts	ms-settings:surfacehub-accounts
#Session cleanup	ms-settings:surfacehub-sessioncleanup
#Team Conferencing	ms-settings:surfacehub-calling
#Team device management	ms-settings:surfacehub-devicemanagenent
#Welcome screen	ms-settings:surfacehub-welcome

#System
#Settings page	URI
#About	ms-settings:about
#Advanced display settings	ms-settings:display-advanced (only available on devices that support advanced display options)
#App volume and device preferences	ms-settings:apps-volume (Added in Windows 10, version 1903)
#Battery Saver	ms-settings:batterysaver (only available on devices that have a battery, such as a tablet)
#Battery Saver settings	ms-settings:batterysaver-settings (only available on devices that have a battery, such as a tablet)
#Battery use	ms-settings:batterysaver-usagedetails (only available on devices that have a battery, such as a tablet)
#Clipboard	ms-settings:clipboard
#Display	ms-settings:display
#Default Save Locations	ms-settings:savelocations
#Display	ms-settings:screenrotation
#Duplicating my display	ms-settings:quietmomentspresentation
#During these hours	ms-settings:quietmomentsscheduled
#Encryption	ms-settings:deviceencryption
#Focus assist	ms-settings:quiethours
#Graphics Settings	ms-settings:display-advancedgraphics (only available on devices that support advanced graphics options)
#Graphics Default Settings	ms-settings:display-advancedgraphics-default
#Multitasking	ms-settings:multitasking
#ms-settings:multitasking-sgupdate
#Night light settings	ms-settings:nightlight
#Projecting to this PC	ms-settings:project
#Shared experiences	ms-settings:crossdevice
#Tablet mode	ms-settings:tabletmode (Removed in Windows 11)
#Taskbar	ms-settings:taskbar
#Notifications & actions	ms-settings:notifications
#Remote Desktop	ms-settings:remotedesktop
#Phone	ms-settings:phone (Deprecated in Windows 10, version 1809 and later)
#Power & sleep	ms-settings:powersleep
#Sound	ms-settings:sound
#Sound devices	ms-settings:sound-devices
#Storage	ms-settings:storagesense
#Storage Sense	ms-settings:storagepolicies
#Storage recommendations	ms-settings:storagerecommendations
#Disks & volumes	ms-settings:disksandvolumes

#Time and language
#Settings page	URI
#Date & time	ms-settings:dateandtime
#Japan IME settings	ms-settings:regionlanguage-jpnime (available if the Microsoft Japan input method editor is installed)
#Region	ms-settings:regionformatting
#Language	ms-settings:keyboard
#ms-settings:keyboard-advanced
#ms-settings:regionlanguage
#ms-settings:regionlanguage-bpmfime
#ms-settings:regionlanguage-cangjieime
#ms-settings:regionlanguage-chsime-wubi-udp
#ms-settings:regionlanguage-quickime
#ms-settings:regionlanguage-korime
#Pinyin IME settings	ms-settings:regionlanguage-chsime-pinyin (available if the Microsoft Pinyin input method editor is installed)
#ms-settings:regionlanguage-chsime-pinyin-domainlexicon
#ms-settings:regionlanguage-chsime-pinyin-keyconfig
#ms-settings:regionlanguage-chsime-pinyin-udp
#Speech	ms-settings:speech
#Wubi IME settings	ms-settings:regionlanguage-chsime-wubi (available if the Microsoft Wubi input method editor is installed)
#Add display language	ms-settings:regionlanguage-adddisplaylanguage
#Language options	ms-settings:regionlanguage-languageoptions
#Set display language	ms-settings:regionlanguage-setdisplaylanguage

#Update and security
#Settings page	URI
#Activation	ms-settings:activation
#Backup	ms-settings:backup (page removed in Windows 11; opens Sync)
#Delivery Optimization	ms-settings:delivery-optimization
#ms-settings:delivery-optimization-activity
#ms-settings:delivery-optimization-advanced
#Find My Device	ms-settings:findmydevice
#For developers	ms-settings:developers
#Recovery	ms-settings:recovery
#Launch Security Key Enrollment	ms-settings:signinoptions-launchsecuritykeyenrollment
#Troubleshoot	ms-settings:troubleshoot
#Windows Security	ms-settings:windowsdefender
#Windows Insider Program	ms-settings:windowsinsider (only present if user is enrolled in WIP)
#ms-settings:windowsinsider-optin
#Windows Update	ms-settings:windowsupdate
#ms-settings:windowsupdate-action
#Windows Update-Active hours	ms-settings:windowsupdate-activehours
#Windows Update-Advanced options	ms-settings:windowsupdate-options
#Windows Update-Optional updates	ms-settings:windowsupdate-optionalupdates
#Windows Update-Restart options	ms-settings:windowsupdate-restartoptions
#Windows Update-Seeker on demand	ms-settings:windowsupdate-seekerondemand
#Windows Update-View update history	ms-settings:windowsupdate-history

#User accounts
#Settings page	URI
#Provisioning	ms-settings:workplace-provisioning (only available if enterprise has deployed a provisioning package)
#Repair token	ms-settings:workplace-repairtoken
#Provisioning	ms-settings:provisioning (only available on mobile and if the enterprise has deployed a provisioning package)
#Windows Anywhere	ms-settings:windowsanywhere (device must be Windows Anywhere-capable)
