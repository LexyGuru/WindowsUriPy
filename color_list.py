from sty import fg, ef, rs
import lang


def color_von():
    print(fg(255, 20, 147) + ef.italic + "------------------------------------------" + rs.italic + fg.rs)


def menu_list_color():
    print(fg(0, 255, 250) + ef.italic + lang.lang[0], sep='\n' + rs.italic + fg.rs)
    print(fg(0, 255, 240) + ef.italic + lang.lang[1], sep='\n' + rs.italic + fg.rs)
    print(fg(0, 255, 230) + ef.italic + lang.lang[2], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 220) + ef.italic + lang.lang[3], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 210) + ef.italic + lang.lang[4], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 200) + ef.italic + lang.lang[5], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 190) + ef.italic + lang.lang[6], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 180) + ef.italic + lang.lang[7], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 170) + ef.italic + lang.lang[8], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 160) + ef.italic + lang.lang[9], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 150) + ef.italic + lang.lang[10], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 140) + ef.italic + lang.lang[11], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 130) + ef.italic + lang.lang[12], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 120) + ef.italic + lang.lang[13], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 110) + ef.italic + lang.lang[14], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 90) + ef.italic + lang.lang[15], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 80) + ef.italic + lang.lang[16], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 70) + ef.italic + lang.lang[17], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 60) + ef.italic + lang.lang[18], sep="\n" + rs.italic + fg.rs)
    print(fg(255, 20, 147) + ef.italic + lang.lang[19], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 50) + ef.italic + lang.lang[20], sep="\n" + rs.italic + fg.rs)


def access_list_color():
    print(fg(0, 255, 250) + ef.italic + lang.access[0], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 240) + ef.italic + lang.access[1], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 230) + ef.italic + lang.access[2], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 220) + ef.italic + lang.access[3], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 210) + ef.italic + lang.access[4], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 200) + ef.italic + lang.access[5], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 190) + ef.italic + lang.access[6], sep="\n" + rs.italic + fg.rs)


def apps_list_color():
    print(fg(0, 255, 250) + ef.italic + lang.apps[0], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 240) + ef.italic + lang.apps[1], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 230) + ef.italic + lang.apps[2], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 220) + ef.italic + lang.apps[3], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 210) + ef.italic + lang.apps[4], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 200) + ef.italic + lang.apps[5], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 190) + ef.italic + lang.apps[6], sep="\n" + rs.italic + fg.rs)


def cortana_list_color():
    print(fg(0, 255, 250) + ef.italic + lang.cortana[0], sep='\n' + rs.italic + fg.rs)
    print(fg(0, 255, 240) + ef.italic + lang.cortana[1], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 230) + ef.italic + lang.cortana[2], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 220) + ef.italic + lang.cortana[3], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 210) + ef.italic + lang.cortana[4], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 200) + ef.italic + lang.cortana[5], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 190) + ef.italic + lang.cortana[6], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 180) + ef.italic + lang.cortana[7], sep="\n" + rs.italic + fg.rs)


def devices_list_color():
    print(fg(0, 255, 250) + ef.italic + lang.devices[0], sep='\n' + rs.italic + fg.rs)
    print(fg(0, 255, 240) + ef.italic + lang.devices[1], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 230) + ef.italic + lang.devices[2], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 220) + ef.italic + lang.devices[3], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 210) + ef.italic + lang.devices[4], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 200) + ef.italic + lang.devices[5], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 190) + ef.italic + lang.devices[6], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 180) + ef.italic + lang.devices[7], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 170) + ef.italic + lang.devices[8], sep="\n" + rs.italic + fg.rs)


def easee_list_color():
    print(fg(0, 255, 250) + ef.italic + lang.ease[0], sep='\n' + rs.italic + fg.rs)
    print(fg(0, 255, 240) + ef.italic + lang.ease[1], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 230) + ef.italic + lang.ease[2], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 220) + ef.italic + lang.ease[3], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 210) + ef.italic + lang.ease[4], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 200) + ef.italic + lang.ease[5], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 190) + ef.italic + lang.ease[6], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 180) + ef.italic + lang.ease[7], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 170) + ef.italic + lang.ease[8], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 160) + ef.italic + lang.ease[9], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 150) + ef.italic + lang.ease[10], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 140) + ef.italic + lang.ease[11], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 130) + ef.italic + lang.ease[12], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 120) + ef.italic + lang.ease[13], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 110) + ef.italic + lang.ease[14], sep="\n" + rs.italic + fg.rs)


def extras_list_color():
    print(fg(0, 255, 250) + ef.italic + lang.extras[0], sep='\n' + rs.italic + fg.rs)


def gaming_list_color():
    print(fg(0, 255, 250) + ef.italic + lang.gaming[0], sep='\n' + rs.italic + fg.rs)
    print(fg(0, 255, 240) + ef.italic + lang.gaming[1], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 230) + ef.italic + lang.gaming[2], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 220) + ef.italic + lang.gaming[3], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 210) + ef.italic + lang.gaming[4], sep="\n" + rs.italic + fg.rs)


def home_list_color():
    print(fg(0, 255, 250) + ef.italic + lang.home[0], sep='\n' + rs.italic + fg.rs)
    print(fg(0, 255, 240) + ef.italic + lang.home[1], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 230) + ef.italic + lang.home[2], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 220) + ef.italic + lang.home[3], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 210) + ef.italic + lang.home[4], sep="\n" + rs.italic + fg.rs)
    print(fg(0, 255, 200) + ef.italic + lang.home[5], sep="\n" + rs.italic + fg.rs)


def network_list_color():
    print("")


def percona_list_color():
    print("")
