import json
import re

x = open('G:\lapy\plik.json')
y = json.load(x)
raw_data = y['sessions'][0]
print(raw_data)

pattern = re.compile(r'\'lap\': \d, \'car\': \d, \'sectors\': \[(?:\d+,*\s*)+], \'time\': [-\d]\d+, \'cuts\': \d, \'tyre\': \'[a-zA-Z]+')

values = (re.findall(pattern, str(raw_data)))

for i in values:
    print(i)
print(len(values))




