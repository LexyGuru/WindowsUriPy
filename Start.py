import modul
import os


list = [
    "modul.accounts.acc()",
    "modul.accounts.app()"
    ]
a = [
    "[00]: Accounts Settings page",
    "[01]: Apps Settings page"
    ]
print(*a, sep = "\n" )
print("\n")

accsettings = list[int(input("Enter a Number: "))]

if accsettings ==  list[0]:
    modul.accounts.acc()

if accsettings ==  list[1]:
    modul.accounts.app()


#
#
