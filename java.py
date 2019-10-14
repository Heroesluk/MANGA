import json
import re
import os

def extract(raw_data):
    pattern = re.compile(
        r'\'lap\': (\d), \'car\': (\d), \'sectors\': (\[(?:\d+,*\s*)*]), \'time\': ([-\d]\d+), \'cuts\': (\d), \'tyre\': \'([a-zA-Z]+)')

    values = (re.findall(pattern, str(raw_data)))
    print('found', len(values),'laps')

    keys = ['lap_number', 'car', 'sectors', 'time', 'cuts', 'tyre']
    list_of_valkeys = []
    for i in values:
        if i[1] != '0':
            pass
        else:
            list_of_valkeys.append(dict(zip(keys, i)))

    print(len(list_of_valkeys), 'laps out of', len(values), 'were the player ones')

    for i in list_of_valkeys:
        print(i)

    print('\n')


for file in os.listdir('G:\lapy'):
    x = open(os.path.join('G:\lapy',file))
    y = json.load(x)
    raw_data = y['sessions'][0]
    extract(raw_data)





