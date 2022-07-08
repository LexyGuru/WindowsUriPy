import time
import os

class accounts:
    def acc():
        #Settings page	URI
        #Access work or school	ms-settings:workplace
        #Email & app accounts	ms-settings:emailandaccounts
        #Family & other people	ms-settings:otherusers
        #Set up a kiosk	ms-settings:assignedaccess
        #Sign-in options	ms-settings:signinoptions
        #Sync your settings	ms-settings:sync
        #Windows Hello setup	ms-settings:signinoptions-launchfaceenrollment
        #Your info	ms-settings:yourinfo
        accs = ["ms-settings:workplace", "ms-settings:emailandaccounts", "ms-settings:otherusers", "ms-settings:assignedaccess", "ms-settings:signinoptions", "ms-settings:sync", "ms-settings:signinoptions-launchfaceenrollment", "ms-settings:yourinfo"]
        a = ["[00]: Access work or school", "[01]: Email & app accounts", "[02]: Family & other people", "[03]: Set up a kiosk", "[04]: Sign-in options", "[05]: Sync your settings", "[06]: Windows Hello setup", "[07]: Your info"]
        print(*a, sep = "\n" )
        print("\n")

        accsettings = accs[int(input("Enter a Number: "))]
        #accsettings = accs[input("Enter a Number: ")]
    
        if accsettings ==  accs[0]:
            os.system("start " + accsettings)
            import Start
        if accsettings ==  accs[1]:
            os.system("start " + accsettings)
            import Start
        if accsettings ==  accs[2]:
            os.system("start " + accsettings)
            import Start
        if accsettings ==  accs[3]:
            os.system("start " + accsettings)
            import Start
        if accsettings ==  accs[4]:
            os.system("start " + accsettings)
            import Start
        if accsettings ==  accs[5]:
            os.system("start " + accsettings)
            import Start
        if accsettings ==  accs[6]:
            os.system("start " + accsettings)
            import Start
        if accsettings == accs[7]:
            os.system("start " + accsettings)
            import Start

    def app():
        #Settings page	URI
        #Apps & Features	ms-settings:appsfeatures
        #App features	ms-settings:appsfeatures-app (Reset, manage add-on & downloadable content, etc. for the app)
        #Apps for websites	ms-settings:appsforwebsites
        #Default apps	ms-settings:defaultapps
        #Manage optional features	ms-settings:optionalfeatures
        #Offline Maps	ms-settings:maps
        #Startup apps	ms-settings:startupapps
        #Video playback	ms-settings:videoplayback   

        apps = ["ms-settings:appsfeatures", "ms-settings:appsfeatures-app", "ms-settings:appsforwebsites", "ms-settings:defaultapps", "ms-settings:optionalfeatures", "ms-settings:maps", "ms-settings:startupapps", "ms-settings:videoplayback"]
        a = ["[00]: Apps & Features", "[01]: App features", "[02]: Apps for websites", "[03]: Default apps", "[04]: Manage optional features", "[05]: Offline Maps", "[06]: Startup apps", "[07]: Video playback"]
        print(*a, sep = "\n" )
        print("\n")

        accsettings = apps[int(input("Enter a Number: "))]

        if accsettings == apps[0]:
            os.system("start " + accsettings)
            import Start

        if accsettings == apps[1]:
            os.system("start " + accsettings)
            import Start

        if accsettings == apps[2]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == apps[3]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == apps[4]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == apps[5]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == apps[6]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == apps[7]:
            os.system("start " + accsettings)
            import Start
        
    def cort():
        #Settings page	URI
        #Cortana across my devices	ms-settings:cortana-notifications
        #More details	ms-settings:cortana-moredetails
        #Permissions & History	ms-settings:cortana-permissions
        #Searching Windows	ms-settings:cortana-windowssearch
        #Talk to Cortana	ms-settings:cortana-language  

        cortana = ["ms-settings:cortana-notifications", "ms-settings:cortana-moredetails", "ms-settings:cortana-permissions", "ms-settings:cortana-windowssearch", "ms-settings:cortana-talktocortana"]
        a = ["[00]: Cortana across my devices", "[01]: More details", "[02]: Permissions & History", "[03]: Searching Windows", "[04]: Talk to Cortana"]
        print(*a, sep = "\n" )
        print("\n")

        accsettings = cortana[int(input("Enter a Number: "))]

        if accsettings == cortana[0]:
            os.system("start " + accsettings)
            import Start

        if accsettings == cortana[1]:
            os.system("start " + accsettings)
            import Start

        if accsettings == cortana[2]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == cortana[3]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == cortana[4]:
            os.system("start " + accsettings)
            import Start

    def devi():
        #Settings page	URI
        #AutoPlay	ms-settings:autoplay
        #Bluetooth	ms-settings:bluetooth
        #Connected Devices	ms-settings:connecteddevices
        #Default camera	ms-settings:camera (Behavior deprecated in Windows 10, version 1809 and later)
        #Camera settings	ms-settings:camera (Behavior introduced in Windows 11, build 22000 and later) Append the query string parameter cameraId set to the Uri-escaped symbolic link name of a camera device to directly launch the settings for that camera. For more information, see Launch the camera settings page.
        #Mouse & touchpad	ms-settings:mousetouchpad (touchpad settings only available on devices that have a touchpad)
        #Pen & Windows Ink	ms-settings:pen
        #Printers & scanners	ms-settings:printers
        #Touch	ms-settings:devices-touch
        #Touchpad	ms-settings:devices-touchpad (only available if touchpad hardware is present)
        #Text Suggestions	ms-settings:devicestyping-hwkbtextsuggestions)
        #Typing	ms-settings:typing
        #USB	ms-settings:usb
        #Wheel	ms-settings:wheel (only available if Dial is paired)
        #Your phone	ms-settings:mobile-devices

        devices = ["ms-settings:autoplay", "ms-settings:bluetooth", "ms-settings:connecteddevices", "ms-settings:camera", "ms-settings:mousetouchpad", "ms-settings:pen", "ms-settings:printers", "ms-settings:devices-touch", "ms-settings:devices-touchpad", "ms-settings:devicestyping-hwkbtextsuggestions", "ms-settings:typing", "ms-settings:usb", "ms-settings:wheel", "ms-settings:mobile-devices"]
        a = ["[00]: AutoPlay", "[01]: Bluetooth", "[02]: Connected Devices", "[03]: Default camera", "[04]: Camera settings", "[05]: Mouse & touchpad", "[06]: Pen & Windows Ink", "[07]: Printers & scanners", "[08]: Touch", "[09]: Touchpad", "[10]: Text Suggestions", "[11]: Typing", "[12]: USB", "[13]: Wheel", "[14]: Your phone"]
        print(*a, sep = "\n" )
        print("\n")

        accsettings = devices[int(input("Enter a Number: "))]

        if accsettings == devices[0]:
            os.system("start " + accsettings)
            import Start

        if accsettings == devices[1]:
            os.system("start " + accsettings)
            import Start

        if accsettings == devices[2]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == devices[3]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == devices[4]:
            os.system("start " + accsettings)
            import Start

        if accsettings == devices[5]:
            os.system("start " + accsettings)
            import Start

        if accsettings == devices[6]:
            os.system("start " + accsettings)
            import Start

        if accsettings == devices[7]:
            os.system("start " + accsettings)
            import Start

        if accsettings == devices[8]:
            os.system("start " + accsettings)
            import Start

        if accsettings == devices[9]:
            os.system("start " + accsettings)
            import Start

        if accsettings == devices[10]:
            os.system("start " + accsettings)
            import Start

        if accsettings == devices[11]:
            os.system("start " + accsettings)
            import Start

        if accsettings == devices[12]:
            os.system("start " + accsettings)
            import Start

        if accsettings == devices[13]:
            os.system("start " + accsettings)
            import Start

        if accsettings == devices[14]:
            os.system("start " + accsettings)
            import Start

    def ease():
        #Settings page	URI
        #Audio	ms-settings:easeofaccess-audio
        #Closed captions	ms-settings:easeofaccess-closedcaptioning
        #Color filters	ms-settings:easeofaccess-colorfilter
        #Display	ms-settings:easeofaccess-display
        #Eye control	ms-settings:easeofaccess-eyecontrol
        #Fonts	ms-settings:fonts
        #High contrast	ms-settings:easeofaccess-highcontrast
        #Keyboard	ms-settings:easeofaccess-keyboard
        #Magnifier	ms-settings:easeofaccess-magnifier
        #Mouse	ms-settings:easeofaccess-mouse
        #Mouse pointer & touch	ms-settings:easeofaccess-mousepointer
        #Narrator	ms-settings:easeofaccess-narrator
        #ms-settings:easeofaccess-narrator-isautostartenabled
        #Speech	ms-settings:easeofaccess-speechrecognition
        #Text cursor	ms-settings:easeofaccess-cursor
        #Visual Effects	ms-settings:easeofaccess-visualeffects

        easee = ["ms-settings:easeofaccess-audio", "ms-settings:easeofaccess-closedcaptioning", "ms-settings:easeofaccess-colorfilter", "ms-settings:easeofaccess-display", "ms-settings:easeofaccess-eyecontrol", "ms-settings:fonts", "ms-settings:easeofaccess-highcontrast", "ms-settings:easeofaccess-keyboard", "ms-settings:easeofaccess-magnifier", "ms-settings:easeofaccess-mouse", "ms-settings:easeofaccess-mousepointer", "ms-settings:easeofaccess-narrator", "ms-settings:easeofaccess-speechrecognition", "ms-settings:easeofaccess-cursor", "ms-settings:easeofaccess-visualeffects"]
        a = ["[00]: Audio", "[01]: Closed captions", "[02]: Color filters", "[03]: Default camera", "[04]: Display", "[05]: Eye control", "[06]: Fonts", "[07]: High contrast", "[08]: Keyboard", "[09]: Magnifier", "[10]: Mouse", "[11]: Mouse pointer & touch", "[12]: Narrator", "[13]: Speech", "[14]: Text cursor", "[15]: Visual Effects"]
        print(*a, sep = "\n" )
        print("\n")

        accsettings = easee[int(input("Enter a Number: "))]

        if accsettings == easee[0]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == easee[1]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == easee[2]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == easee[3]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == easee[4]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == easee[5]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == easee[6]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == easee[7]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == easee[8]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == easee[9]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == easee[10]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == easee[11]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == easee[12]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == easee[13]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == easee[14]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == easee[15]:
            os.system("start " + accsettings)
            import Start
     
    def extr():
        #Extras
        #Settings page	URI
        #Extras	ms-settings:extras (only available if "settings apps" are installed, for example, by a 3rd party)

        extr = ["ms-settings:extras"]
        a = ["[00]: Extras"]
        print(*a, sep = "\n" )
        print("\n")

        accsettings = extr[int(input("Enter a Number: "))]

        if accsettings == extr[0]:
            os.system("start " + accsettings)
            import Start
        
    def game():
        #Gaming
        #Settings page	URI
        #Game bar	ms-settings:gaming-gamebar
        #Game DVR	ms-settings:gaming-gamedvr
        #Game Mode	ms-settings:gaming-gamemode
        #Playing a game full screen	ms-settings:quietmomentsgame
        #TruePlay	ms-settings:gaming-trueplay (As of Windows 10, version 1809 (10.0; Build 17763), this feature is removed from Windows)

        game = ["ms-settings:gaming-gamebar", "ms-settings:gaming-gamedvr", "ms-settings:gaming-gamemode", "ms-settings:quietmomentsgame", "ms-settings:gaming-trueplay"]
        a = ["[00]: Game bar", "[01]: Game DVR", "[02]: Game Mode", "[03]: Playing a game full screen", "[04]: TruePlay"]
        print(*a, sep = "\n" )
        print("\n")

        accsettings = game[int(input("Enter a Number: "))]

        if accsettings == game[0]:
            os.system("start " + accsettings)
            import Start

        if accsettings == game[1]:
            os.system("start " + accsettings)
            import Start

        if accsettings == game[2]:
            os.system("start " + accsettings)
            import Start

        if accsettings == game[3]:
            os.system("start " + accsettings)
            import Start

        if accsettings == game[4]:
            os.system("start " + accsettings)
            import Start

    def home():
        #Home page
        #Settings page	URI
        #Default browser settings	ms-settings:defaultbrowsersettings
        #Audio and speech	ms-settings:holographic-audio
        #Environment	ms-settings:privacy-holographic-environment
        #Headset display	ms-settings:holographic-headset
        #Uninstall	ms-settings:holographic-management
        #Startup and desktop	ms-settings:holographic-startupandesktop

        home = ["ms-settings:easeofaccess-audio", "ms-settings:easeofaccess-closedcaptioning", "ms-settings:easeofaccess-colorfilter", "ms-settings:easeofaccess-display", "ms-settings:easeofaccess-eyecontrol", "ms-settings:fonts", "ms-settings:easeofaccess-highcontrast", "ms-settings:easeofaccess-keyboard", "ms-settings:easeofaccess-magnifier", "ms-settings:easeofaccess-mouse", "ms-settings:easeofaccess-mousepointer", "ms-settings:easeofaccess-narrator", "ms-settings:easeofaccess-speechrecognition", "ms-settings:easeofaccess-cursor", "ms-settings:easeofaccess-visualeffects"]
        a = ["[00]: Audio", "[01]: Closed captions", "[02]: Color filters", "[03]: Default camera", "[04]: Display", "[05]: Eye control", "[06]: Fonts", "[07]: High contrast", "[08]: Keyboard", "[09]: Magnifier", "[10]: Mouse", "[11]: Mouse pointer & touch", "[12]: Narrator", "[13]: Speech", "[14]: Text cursor", "[15]: Visual Effects"]
        print(*a, sep = "\n" )
        print("\n")

        accsettings = home[int(input("Enter a Number: "))]

        if accsettings == home[0]:
            os.system("start " + accsettings)
            import Start

    def netw():
        #Network and internet
        #Settings page	URI
        #Advanced settings	ms-settings:network-advancedsettings
        #Airplane mode	ms-settings:network-airplanemode
        #ms-settings:proximity
        #Cellular & SIM	ms-settings:network-cellular
        #Dial-up	ms-settings:network-dialup
        #DirectAccess	ms-settings:network-directaccess (only available if DirectAccess is enabled)
        #Ethernet	ms-settings:network-ethernet
        #Manage known networks	ms-settings:network-wifisettings
        #Mobile hotspot	ms-settings:network-mobilehotspot
        #Proxy	ms-settings:network-proxy
        #VPN	ms-settings:network-vpn
        #Wi-Fi	ms-settings:network-wifi (only available if the device has a wifi adapter)
        #Wi-Fi provisioning	ms-settings:wifi-provisioning

        network = [
            "ms-settings:network-advancedsettings",
            "ms-settings:network-airplanemode #ms-settings:proximity",
            "ms-settings:network-cellular",
            "ms-settings:network-dialup",
            "ms-settings:network-directaccess", #(only available if DirectAccess is enabled)
            "ms-settings:network-ethernet",
            "ms-settings:network-wifisettings",
            "ms-settings:network-mobilehotspot",
            "ms-settings:network-proxy",
            "ms-settings:network-vpn",
            "ms-settings:network-wifi", #(only available if the device has a wifi adapter)
            "ms-settings:wifi-provisioning"
            ]
        a = [
            "[00]: Advanced settings",
            "[01]: Airplane mode",
            "[02]: Cellular & SIM",	
            "[03]: Dial-up",
            "[04]: DirectAccess",
            "[05]: Ethernet",
            "[06]: Manage known networks",
            "[07]: Mobile hotspot",
            "[08]: Proxy",
            "[09]: VPN",
            "[10]: Wi-Fi",
            "[11]: Wi-Fi provisioning"
            ]

        print(*a, sep = "\n" )
        print("\n")

        accsettings = network[int(input("Enter a Number: "))]

        if accsettings == network[0]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == network[1]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == network[2]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == network[3]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == network[4]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == network[5]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == network[6]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == network[7]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == network[8]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == network[9]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == network[10]:
            os.system("start " + accsettings)
            import Start
        
        if accsettings == network[11]:
            os.system("start " + accsettings)
            import Start
        