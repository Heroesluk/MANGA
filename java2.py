import json
import re
import os

def extract(raw_data): #works inside one file
    pattern = re.compile(
        r'\'lap\': (\d), \'car\': (\d), \'sectors\': (\[(?:\d+,*\s*)*]), \'time\': ([-\d]\d+), \'cuts\': (\d), \'tyre\': \'([a-zA-Z]+)')

    values = (re.findall(pattern, str(raw_data))) #Find all lap data in the file
    ###print('found', len(values),'laps') ####CHECK LAPS###

    if len(values)==0:
        return

    else:
        keys = ['lap_number', 'car', 'sectors', 'time', 'cuts', 'tyre']  # Keys for dict
        list_of_valkeys = []  # empty list for lap data dictionaries
        for i in values:  # values - EX: ('0', '0', '[48425, 31667, 20453]', '-1', '1', 'SM')
            if i[1] != '0':  # ignores the lap data, if it isn't the players "0" car
                pass
            else:
                if int(i[3]) < 100:  # ignores lap data, if time of lap is less then one second
                    pass
                else:
                    list_of_valkeys.append(dict(
                        zip(keys, i)))  # creates dict out of lap data and keys and add it to the list of lap-data-dicts

        ###print(len(list_of_valkeys), 'laps out of', len(values), 'were the player ones') CHECK LAPS###
       ####print('\n')###

        return list_of_valkeys


list_of_valkeys = []
for file in os.listdir('C:\\Users\DOMOWY\AppData\Local\AcTools Content Manager\Progress\Sessions'):
    x = (os.path.join('C:\\Users\DOMOWY\AppData\Local\AcTools Content Manager\Progress\Sessions',file))
    read = open(x,encoding="utf8")
    y = json.load(read)
    raw_data = y['sessions'][0] ###UP TO THIS WORKS
    ###print(file) #### print FILES

    new_list = extract(raw_data)
    if new_list is None:
        pass
    else:
        list_of_valkeys = list_of_valkeys + extract(raw_data)  # sums the lap-dicts from all files




print(len(list_of_valkeys))
