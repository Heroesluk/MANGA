import json
import re

x = open('G:\lapy\plik.json')
y = json.load(x)
raw_data = y['sessions'][0]
print(raw_data)

pattern = re.compile(r'\'lap\': \d, \'car\': \d, \'sectors\': \[\d+, \d+, \d+\], \'time\': [-\d]\d+, \'cuts\': \d, \'tyre\': \'[a-zA-Z]+')

values = (re.findall(pattern, str(raw_data)))

for i in values:
    print(i)
print(len(values))



#{"lap":1,"car":0,"sectors":[57161],"time":-1,"cuts":1,"tyre":"SM"}
#"lap":4,"car":0,"sectors":[28546,18049,20529],"time":67124,"cuts":0,"tyre":"SM"}








