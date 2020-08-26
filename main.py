import feedparser
import requests
import json
import time

webhook='https://maker.ifttt.com/trigger/nuevo_cap/with/key/mmgAHPsC2HCTjn4T204ejMGZNImJ-9yg6KpBItbeyzn'

def createDict():
    animes=dict()
    with open('season.txt','r') as file:
        lines = file.readlines()
        for line in  lines:
            animes.update({line.rstrip():0})
    return animes
def checkNew(animeDict):
    jkanime = feedparser.parse('https://feeds.feedburner.com/jkanime')
    content = list()
    for i in range(len(jkanime.entries)):
        entrada=jkanime.entries[i].title
        content.append(entrada.split(' - ')[0])
    for titulo in animeDict.keys():
        if titulo in content and animeDict[titulo]==0:
            animeDict[titulo]=1
            notify(titulo)
        if titulo not in content and animeDict[titulo]==1:
            animeDict[titulo]=0
            



     
def notify(title):
    data = {'value1':title}  # Dict de datos que se envian
    try:
        r = requests.get(url=webhook, params=data)
        r.raise_for_status
    except requests.HTTPError as err:
        print(err)


if __name__ == "__main__":
    animeDict=createDict()
    while True:
        checkNew(animeDict)
        time.sleep(50)
        print('repito')
        

    
