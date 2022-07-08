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
            #ms-settings:signinoptions-dynamiclock
        #Sync your settings	ms-settings:sync
        #Windows Hello setup	ms-settings:signinoptions-launchfaceenrollment
            #ms-settings:signinoptions-launchfingerprintenrollment
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
            #ms-settings:maps-downloadmaps (Download maps)
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
        #ms-settings:cortana
        #ms-settings:cortana-talktocortana   

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
