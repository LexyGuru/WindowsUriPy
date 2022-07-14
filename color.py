from sty import fg, bg, ef, rs
from sty import Style, RgbFg


class style():
    CEND = '\33[0m'
    CBOLD = '\33[1m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    CBLINK = '\33[5m'
    CBLINK2 = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

    CBLACKBG = '\33[40m'
    CREDBG = '\33[41m'
    CGREENBG = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG = '\33[46m'
    CWHITEBG = '\33[47m'

    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'

    CGREYBG = '\33[100m'
    CREDBG2 = '\33[101m'
    CGREENBG2 = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2 = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2 = '\33[106m'
    CWHITEBG2 = '\33[107m'


# print(style.CGREY + "Hello, World!")

# foo = fg.red + 'This is red text!' + fg.rs
# bar = bg.blue + 'This has a blue background!' + bg.rs
# baz = ef.italic + 'This is italic text' + rs.italic
# qux = fg(201) + 'This is pink text using 8bit colors' + fg.rs
# qui = fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs


# qui = fg(50, 50, 50) + 'This is red text using 24bit colors.' + fg.rs

# Add custom colors:
# https://i.stack.imgur.com/S8wtO.png

# fg.orange = Style(RgbFg(255, 150, 50))

# buf = fg.orange + 'Yay, Im orange.' + fg.rs

# print(foo, bar, baz, qux, qui, buf, sep='\n')
