import os

Path =  "C:\Users\DOMOWY\Desktop\manga\Bokura no Hentai"
ListOfChapters = (os.listdir(Path))
count = 0
for chapters in ListOfChapters:

    PagesPath = os.path.join(Path, chapters)

    for pages in os.listdir(PagesPath):

        paf = os.path.join(PagesPath, pages)
        NewPaf = str(count) + '.jpg'
        NewPath = os.path.join(Path, NewPaf)
        os.rename(paf, NewPath )
        count = count + 1

