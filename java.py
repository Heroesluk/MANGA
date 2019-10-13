import json
import re

x = open('G:\lapy\plik4.json')
y = json.load(x)
raw_data = y['sessions'][0]
print(raw_data)

pattern = re.compile(r'\'lap\': (\d), \'car\': (\d), \'sectors\': (\[(?:\d+,*\s*)*]), \'time\': ([-\d]\d+), \'cuts\': (\d), \'tyre\': \'([a-zA-Z]+)')

values = (re.findall(pattern, str(raw_data)))
print(len(values))


keys = ['lap_number', 'car', 'sectors', 'time', 'cuts', 'tyre']
list_of_valkeys = []
for i in values:
    if i[1]!='0':
        pass
    else:
        list_of_valkeys.append(dict(zip(keys, i)))




for i in list_of_valkeys:
    print(i)











