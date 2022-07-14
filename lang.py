import json
import codecs

hun = "lang/hun.json"
eng = "lang/eng.json"
lang = "lang/lang.json"

json.load(codecs.open(lang, 'r', 'utf-8-sig'))
with open(lang, encoding='utf-8-sig') as f:
    data = json.load(f)

main_lang = data['main_lang']

if main_lang == ['hun']:
    lang = hun

if main_lang == ['eng']:
    lang = eng

json.load(codecs.open(lang, 'r', 'utf-8-sig'))
with open(lang, encoding='utf-8-sig') as f:
    langs = json.load(f)

# language def

lang = langs['main_list']
access = langs['access']
apps = langs['apps']
cortana = langs['cortana']
devices = langs['devices']
ease = langs['ease']
extras = langs['extras']
gaming = langs['gaming']
home = langs['home']
network = langs['network']
personalization = langs['personalization']
phone = langs['phone']
privacy = langs['privacy']
surface = langs['surface']
system = langs['system']
update = langs['update']
user = langs['user']
control = langs['control']
family = langs['family']
search = langs['search']


