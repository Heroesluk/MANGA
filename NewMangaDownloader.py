import requests
from bs4 import BeautifulSoup
import re
data = requests.get('https://manganelo.com/manga/wv919354')

soup = BeautifulSoup(data.text, 'html.parser')



def chapterlist():  #gets the list of all manga chapters
    chapterlist = []

    for div in soup.find_all('div', {'class': 'chapter-list'}):
        for lista in div.find_all('a'):
            chapterlist.append(lista.get('href'))

    return chapterlist

def invert(listaold): #inverts the list
    lista = []
    b = len(listaold) - 1
    for i in listaold:
        lista.append(listaold[b])
        b = b - 1
    return  lista

def links(lista): #get links to all images in all chapter links
    LinkList = []
    ind = 0
    for i in lista:
        LinkList.append([])
        data2 = requests.get(i)
        soup2 = BeautifulSoup(data2.text, 'html.parser')

        for div in soup2.find_all('div', {'class': 'vung-doc'}):
            for link in div.find_all('img'):
                LinkList[ind].append(link.get('src'))

        ind = ind + 1


    return  LinkList

def download(LinkList): #download all images
    chap = 0

    for i in LinkList:
        chap = chap + 1
        a = 0
        for images in i:
            request = requests.get(images)
            print(images)
            with open('Manga Chapter ' + str(chap) + ' strona ' + str(a) + '.jpg', 'wb') as f:
                f.write(request.content)
            a = a + 1
    print('chapter number ' + str(chap) + 'downloaded')




listaold = chapterlist()

lista = invert(listaold)

print('enter the range of chapters you want to download, ')
print(' e.x input - 22 - > enter - > 50 - > enter  will download every chapter from 22th to 50th')
num1 = input()
num2 = input()
lista = lista[num1-1:num2] #numbers of chapters you want to download

LinkList = links(lista)

download(LinkList)






