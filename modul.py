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
        accs = [
            "ms-settings:workplace",
            "ms-settings:emailandaccounts",
            "ms-settings:otherusers",
            "ms-settings:assignedaccess",
            "ms-settings:signinoptions",
            "ms-settings:sync",
            "ms-settings:signinoptions-launchfaceenrollment",
            "ms-settings:yourinfo",
             "" ]
        a = [
            "[00]: Access work or school",
            "[01]: Email & app accounts",
            "[02]: Family & other people",
            "[03]: Set up a kiosk",
            "[04]: Sign-in options",
            "[05]: Sync your settings",
            "[06]: Windows Hello setup",
            "[07]: Your info"
        ]
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

        apps = [
            "ms-settings:appsfeatures",
            "ms-settings:appsfeatures-app",
            "ms-settings:appsforwebsites",
            "ms-settings:defaultapps",
            "ms-settings:optionalfeatures",
            "ms-settings:maps",
            "ms-settings:startupapps",
            "ms-settings:videoplayback",
             "" ]
        a = [
            "[00]: Apps & Features",
            "[01]: App features",
            "[02]: Apps for websites",
            "[03]: Default apps",
            "[04]: Manage optional features",
            "[05]: Offline Maps",
            "[06]: Startup apps",
            "[07]: Video playback"
        ]
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
        