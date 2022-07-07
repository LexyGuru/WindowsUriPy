import modul
import os
import logo


list = [
    "modul.accounts.acc()",
    "modul.accounts.app()"
    ]
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
    "",
    "[20]: EXIT"
    ]
print(*a, sep = "\n" )
print("\n")

accsettings = list[int(input("Enter a Number: "))]

if accsettings ==  list[0]:
    modul.accounts.acc()

if accsettings ==  list[1]:
    modul.accounts.app()


