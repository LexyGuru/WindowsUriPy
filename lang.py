import json
import codecs
import os

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

lang = langs['main_list']
acc = langs['acc']
app = langs['apps']


#print(langs['main'][6])



