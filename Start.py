import modul
import os
import logo

logo.logos.main_logo()
list = [
    "0", #00
    "1", #01
    "2", #02
    "3", #03
    "4", #04
    "5", #05
    "6", #06
    "7", #07
    "8", #08
    "9", #09
    "10", #10
    "11", #11
    "12", #12
    "13", #13
    "14", #14
    "15", #15
    "16", #16
    "17", #17
    "18", #18
    "19",
    "20"
    ]
print("------------------------------------------")
a = [
    "[00]: Accounts Settings page",
    "[01]: Apps Settings page",
    "[02]: Cortana Settings page",
    "[03]: Devices Settings page",
    "[04]: Ease of access Settings page",
    "[05]: Extras Settings page",
    "[06]: Gaming Settings page",
    "[07]: Home page Settings page",
    "[08]: Network and internet Settings page",
    "[09]: Personalization Settings page",
    "[10]: Phone Settings page",
    "[11]: Privacy Settings page",
    "[12]: Surface Hub Settings page",
    "[13]: System Settings page",
    "[14]: Update and security Settings page",
    "[15]: User accounts Settings page",
    "[16]: Control Center Settings page",
    "[17]: Family Group Settings page",
    "[18]: Search Settings page",
    "------------------------------------------",
    "[20]: Exit"
]

print(*a, sep = "\n" )
print("\n")

accsettings = list[int(input("Enter a Number: "))]

if accsettings ==  list[0]:
        modul.accounts.acc()

if accsettings == list[1]:
        modul.accounts.app()

if accsettings == list[2]:
        modul.accounts.cort()

if accsettings == list[3]:
        modul.accounts.devi()

if accsettings == list[4]:
        modul.accounts.ease()

if accsettings == list[5]:
        modul.accounts.extr()
        
if accsettings == list[6]:
        modul.accounts.game()

if accsettings == list[7]:
        modul.accounts.home()
        
if accsettings == list[8]:
        modul.accounts.netw()
        
if accsettings == list[9]:
        print("09")
        exit
        
if accsettings == list[10]:
        print("10")
        exit
        
if accsettings == list[11]:
        print("11")
        exit
        
if accsettings == list[12]:
        print("12")
        exit
        
if accsettings == list[13]:
        print("13")
        exit
        
if accsettings == list[14]:
        print("14")
        exit
        
if accsettings == list[15]:
        print("15")
        exit
        
if accsettings == list[16]:
        print("16")
        exit
        
if accsettings == list[17]:
        print("17")
        exit
        
if accsettings == list[18]:
        print("18")
        exit

if accsettings == list[19]:
        exit

if accsettings == list[20]:
        exit
