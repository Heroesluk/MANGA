import subprocess

try:
    subprocess.call(["ebook-convert", 'C:\Users\DOMOWY\Desktop\\fajny\\manga.cbz', 'C:\Users\DOMOWY\Desktop\\fajny\\manga.MOBI' ])
except Exception as e:
    print(e)
