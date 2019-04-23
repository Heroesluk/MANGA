import requests
from bs4 import BeautifulSoup

def anime():
    episodes = []
    links = []

    with open('anime.txt', 'r') as f:
        content = f.readlines()
        content = [x.strip() for x in content]

    for new in content:
        link = 'https://nyaa.si/?f=0&c=1_2&q=' + str(new)

        def reklest(link):
            NyaaCode = requests.get(link)
            NyaaText = NyaaCode.text
            NyaaParsed = BeautifulSoup(NyaaText, 'lxml')
            return NyaaParsed
        NyaaParsed = reklest(link)  # Gets Parsed code of the site



        def linkslist(NyaaParsed):
            LinkList = []
            LinkFixed = []

            for link in NyaaParsed.find_all('a'):
                LinkList.append(link.get('href'))

            for i in LinkList:
                if 'torrent' in str(i):
                    LinkFixed.append(i)

            return LinkFixed
        LinkFixed = linkslist(NyaaParsed)  # Gets all torrent links as list



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
        EpisodeList = episodelists(NyaaParsed)  # Gets all torrent names as list

        def druk():
            a = 0
            for i in EpisodeList:
                print(i, LinkFixed[a])

                a = a + 1
            print '\n'

        def sprawdzanie(EpisodeList):
            a = 0  # a = index torrenta
            # i = nazwa odcinka
            for i in EpisodeList:
                if new in i and 'HorribleSubs' in i:
                    return i, a
                a = a + 1

            for i in EpisodeList:
                if new in i and 'Erai-raws' in i:
                    return i, a
                a = a + 1

            for i in EpisodeList:
                if new in i:
                    return i, a
                a = a + 1



        try:
            epizod, a = sprawdzanie(EpisodeList)

            episodes.append(epizod)
            links.append(LinkFixed[a])

        except:
            print('brak nowego odcinka')

    return episodes, links


anime, lista = anime()

def animedownload(anime, lista):
    a = 0
    for i in lista:
        print(i, anime[a])
        torent = requests.get('https://nyaa.si' + str(i))
        with open(str(anime[a]) + '.torrent', 'wb') as f:
            f.write(torent.content)
        a = a + 1

animedownload(anime, lista)























