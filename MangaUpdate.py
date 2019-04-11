import requests


def Manga(wat):
    list = requests.get(wat)
    list = list.text

    list = list.splitlines()

    a = 0
    for i in list:
        if a == 1:
            chapter = i #Creates string with most recent chapter
            break
        if i == '<div class="row">': #Finds if it's line right before line with chapter(always inicialize right before first conditonal
            a = 1

    val = chapter.find('title')
    chapter = chapter[val + 7:]  # Strips string from left side html

    val = chapter.find('>')
    return chapter[:val - 1] # Strips string from right side html, amd returns it


MangaList = ['https://manganelo.com/manga/domestic_na_kanojo', 'https://manganelo.com/manga/kaguyasama_wa_kokurasetai_tensaitachi_no_renai_zunousen', 'https://manganelo.com/manga/gotoubun_no_hanayome', 'https://mangakakalot.com/manga/pt918921' ]
ChapterList = []
for i in MangaList:
    ChapterList.append(Manga(i))

for i in ChapterList:
    print(i)











