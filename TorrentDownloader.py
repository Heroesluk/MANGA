import requests
from bs4 import BeautifulSoup

link = 'https://nyaa.si/?f=0&c=1_2&q=Tate'



def reklest(link):
    NyaaCode = requests.get(link)
    NyaaText = NyaaCode.text
    NyaaParsed = BeautifulSoup(NyaaText, 'lxml')
    return NyaaParsed
NyaaParsed = reklest(link) #Gets Parsed code of the site


def linkslist(NyaaParsed):
    LinkList = []
    LinkFixed = []

    for link in NyaaParsed.find_all('a'):
        LinkList.append(link.get('href'))

    for i in LinkList:
        if 'torrent' in str(i):
            LinkFixed.append(i)

    return LinkFixed
LinkFixed = linkslist(NyaaParsed) #Gets all torrent links as list


def episodelists(NyaaParsed):
    EpisodeList = []
    for link in NyaaParsed.find_all('a'):
        temp = link.get('title')
        if temp == None:
            pass
        elif 'English-translated' in temp:
            pass
        elif 'comment' in temp:
            pass
        else:
            EpisodeList.append(temp)

    return EpisodeList
EpisodeList = episodelists(NyaaParsed) #Gets all torrent names as list

def druk():
    a = 0
    for i in EpisodeList:
        print(i, LinkFixed[a])

        a = a + 1
    print '\n'
druk()



def uzupelnij():
    ListaSezonu = ['Tate no Yuusha no Nariagari - 15', 'Carole & Tuesday - 02', 'RobiHachi - 02', 'Sarazanmai - 02']

    with open('anime.txt', 'wb') as f:
        for item in ListaSezonu:
            f.write("%s\n" % item)



with open('anime.txt', 'r') as f:
    content = f.readlines()
    content = [x.strip() for x in content]




print('\n')







new = 'Tate no Yuusha no Nariagari - 15'


def sprawdzanie(EpisodeList):
    a=0 #a = index torrenta
    # i = nazwa odcinka
    for i in EpisodeList:
        if new in i and 'HorribleSubs' in i:
            return i,a
        a = a + 1

    for i in EpisodeList:
        if new in i and 'Erai-raws' in i:
            return i,a
        a = a + 1

    for i in EpisodeList:
        if new in i:
            return i,a
        a = a + 1

try:
    epizod, a = sprawdzanie(EpisodeList)
    print(epizod, LinkFixed[4])
except:
    print('brak nowego odcinka')













