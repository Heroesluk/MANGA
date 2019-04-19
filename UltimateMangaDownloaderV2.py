import requests
from bs4 import BeautifulSoup

def MangaDownloader():
    print('Podaj link do mangi na MangaKakalot/Manganelo')
    MLink = str(raw_input())
    MLink = MLink[:-1]
    print(MLink)

    def ChapterMangaLinks(MLink):
        def ChapterOnly(MLink):
            a = 0
            ChapOnly = []
            for i in MLink:
                ChapOnly.append(MLink[-a])  # Creates name of the chap list reverted
                if MLink[-a] == '/':
                    break
                a = a + 1

            a = 0
            chap = ChapOnly
            FinalChapt = []
            for i in chap:
                FinalChapt.append(chap[-a])  # Revert it back again
                a = a + 1
            Final = ''.join(FinalChapt[2:])  # Make string from it

            return Final  # For example 'my_girlfriend_is_her_dad'

        ChapterKey = ChapterOnly(MLink)  # For example 'my_girlfriend_is_her_dad'

        MangaCode = requests.get(MLink)  # HTML code of the site
        MangaCode = MangaCode.text  # HTML code of the site

        MangaParsed = BeautifulSoup(MangaCode, 'lxml')

        def chapterLinks(ChapterKey,
                         MangaParsed):  # Finds all links in HTML-code and returns only those with ChapterKey within
            ChapterList = []
            LinkList = []
            for link in MangaParsed.findAll('a'):
                LinkList.append(link.get('href'))

            for i in LinkList:
                if 'chapter' in str(i) and ChapterKey in str(i):
                    ChapterList.append(i)

            return ChapterList

        ChapterLinverted = chapterLinks(ChapterKey, MangaParsed)  # List of links to all chapters

        def chapterList(ChapterLinverted):  # Invertes the list of chapters
            ChapterList = []
            a = 1
            for i in ChapterLinverted:
                ChapterList.append(ChapterLinverted[-a])
                a = a + 1
            return ChapterList

        ChapterList = chapterList(ChapterLinverted)

        return ChapterList, ChapterKey

    ChapterLinks, ChapterKey = ChapterMangaLinks(MLink)  # Returns tulpe with list of Chapters and Chapter key

    # for i in ChapterLinks:
    # print(i)

    def MangaDownload(ChapterLinks, ChapterKey):
        a = 0
        c = 0
        for i in ChapterLinks:
            ChapterCode = requests.get(i)
            ChapterCode = ChapterCode.text

            ChapterParsed = BeautifulSoup(ChapterCode, 'lxml')

            def imagesList(ChapterParsed):
                LinkList = []
                LinkListFixed = []

                for link in ChapterParsed.findAll('img'):
                    LinkList.append(link.get('src'))

                for i in LinkList:
                    if ChapterKey in i:
                        LinkListFixed.append(i)

                return LinkListFixed  # links of all images in chapters

            ChapterImages = imagesList(ChapterParsed)  # links of all images in chapters
            # print(ChapterImages)

            for i in ChapterImages:
                ImageRequest = requests.get(i)

                with open(str(ChapterKey) + ' Chapter ' + str(c) + ' Page ' + str(a) + '.jpg', 'wb') as f:
                    f.write(ImageRequest.content)
                a = a + 1

            print('chapter ' + str(c) + ' skonczony')

            c = c + 1

    MangaDownload(ChapterLinks, ChapterKey)


def MangaUpdate():
    def MangaUpdateCheck():
        def Manga(wat):
            list = requests.get(wat)
            list = list.text

            list = list.splitlines()

            a = 0
            for i in list:
                if a == 1:
                    chapter = i  # Creates string with most recent chapter
                    break
                if i == '<div class="row">':  # Finds if it's line right before line with chapter(always inicialize right before first conditonal
                    a = 1

            val = chapter.find('title')
            chapter = chapter[val + 7:]  # Strips string from left side html

            val = chapter.find('>')
            return chapter[:val - 1]  # Strips string from right side html, amd returns it

        MangaList = ['https://manganelo.com/manga/domestic_na_kanojo',
                     'https://manganelo.com/manga/kaguyasama_wa_kokurasetai_tensaitachi_no_renai_zunousen',
                     'https://manganelo.com/manga/gotoubun_no_hanayome', 'https://mangakakalot.com/manga/pt918921', 'https://manganelo.com/manga/read_one_punch_man_manga_online_free3']
        ChapterList = []
        for i in MangaList:
            ChapterList.append(Manga(i))

        return ChapterList, MangaList

    def MangaUpdateFile():
        ChapterList, MangaList = MangaUpdateCheck()
        ChapterString = "\n".join(ChapterList)
        ChapterString = ChapterString.encode(encoding='UTF-8', errors='strict')

        manga = open("Mangi.txt", "w")
        manga.write(ChapterString)
        manga.close()

    def MangaUpdateFile2():
        ChapterList, MangaList = MangaUpdateCheck()
        ChapterString = "\n".join(ChapterList)
        ChapterString = ChapterString.encode(encoding='UTF-8', errors='strict')

        manga = open("MangiComp.txt", "w")
        manga.write(ChapterString)
        manga.close()
        return MangaList

    MangaList = MangaUpdateFile2()

    manga = open("Mangi.txt", "r")
    CompList = manga.readlines()  # makes list to comparise

    MangaComp = open("MangiComp.txt", "r")
    CompMang = MangaComp.readlines()  # makes list to comparise

    def Comp(CompMang, CompList):
        a = 0
        for i in CompList:
            if i == CompMang[a]:
                print('nie ma nowego chapteru', MangaList[a])
            else:
                print('jest nowy chapter', MangaList[a])
            a = a + 1

    Comp(CompMang, CompList)

    MangaUpdateFile()
    manga.close()


while True:
    print('Choose your poison:  ')
    print('  1 - MangaDownloader')
    print('  2 - MangaUpdateCheck')
    print('  3 - exit')
    choice = input()


    if choice == 1:
        MangaDownloader()

    elif choice == 2:
        MangaUpdate()

    elif choice == 3:
        break

    print('\n' * 16)



