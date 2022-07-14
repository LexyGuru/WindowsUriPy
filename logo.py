from sty import fg, bg, ef, rs
from sty import Style, RgbFg

class logos:
    def main_logo(self):
        logocolora = fg(200, 50, 80) + '                                                    (       )    ' + fg.rs
        logocolorb = fg(200, 60, 70) + '   (  (               (                             )\ ) ( /(    ' + fg.rs
        logocolorc = fg(200, 70, 60) + '   )\))(    (         )\ )    (  (         (  (  ( (()/( )\())   ' + fg.rs
        logocolord = fg(200, 80, 50) + '  ((_)()\ ) )\  (    (()/( (  )\))(  (     )\ )( )\ /(_)((_)\    ' + fg.rs
        logocolore = fg(200, 90, 40) + '  _(())\_)(((_) )\ )  ((_)))\((_)()\ )\ _ ((_(()((_(_))__ ((_)   ' + fg.rs
        logocolorf = fg(200, 100, 30) + '  \ \((_)/ /(_)_(_/(  _| |((__(()((_((_| | | |((_(_| _ \ \ / /   ' + fg.rs
        logocolorg = fg(200, 110, 20) + '   \ \/\/ / | |   \)/ _` / _ \ V  V (_-| |_| |  _| |  _/\ V /    ' + fg.rs
        logocolorh = fg(200, 120, 10) + '    \_/\_/  |_|_||_|\__,_\___/\_/\_//__/\___/|_| |_|_|   |_|     ' + fg.rs
        logocolori = fg(200, 130, 0) + '                                                                 ' + fg.rs

        print(logocolora + "\n" + logocolorb + "\n" + logocolorc + "\n" + logocolord + "\n" + logocolore + "\n" + logocolorf + "\n" + logocolorg + "\n" + logocolorh + "\n" + logocolori)
