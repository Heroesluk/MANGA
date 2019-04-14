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




MangaDownloader()





























