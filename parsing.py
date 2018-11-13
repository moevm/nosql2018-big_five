import requests
import bs4
from bs4 import BeautifulSoup

import csv
import json
import codecs


def write_json(person):        #запись в json
    try:
        data = json.load(open('file.json'))
    except:
        data = []
    data.append(person)
    with open('file.json','w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def write_json_all(url):       #парсинг страницы
    s = requests.get(url)
    print(s.ok)
    b = bs4.BeautifulSoup(s.text, "html.parser")

    name_list = b.find(class_='stdTbl')
    name_list_items = name_list.find_all(class_='jCell jCellC')
    # print(name_list_items)

    f = csv.writer(open('z-artist-names.csv', 'w'))
    f.writerow(['Name'])

    name3_list = b.find(class_='stdTbl')
    name3_list_items = name3_list.find_all('a')

    l_list = []

    for name in name_list_items:
        names = name.contents[0]

        if (names < '9' or names == '9') and (names > '1' or names == '1'):
            l_list.append(names)
            f.writerow([names])
            # print(names)

    print(l_list)

    return l_list

def person(column, l_list):     #формирование коллекции
    person = {
        'name': column[0],
        'group': column[1],
        'url': column[2],
        'intovers': l_list[0],
        'passivn': l_list[1],
        'podchin': l_list[2],
        'zamknut': l_list[3],
        'izbegvpet': l_list[4],
        'izbegvnim': l_list[5],
        'obosobl': l_list[6],
        'ravnodush': l_list[7],
        'sopern': l_list[8],
        'podozrit': l_list[9],
        'neponimanie': l_list[10],
        'samouvaz': l_list[11],
        'impulsivn': l_list[12],
        'neakkurat': l_list[13],
        'otsutnastoy': l_list[14],
        'bezotvet': l_list[15],
        'impulsivn2': l_list[16],
        'bespechn': l_list[17],
        'emocustoy': l_list[18],
        'bezzabotn': l_list[19],
        'rasslablen': l_list[20],
        'emockomfort': l_list[21],
        'samodost': l_list[22],
        'emocstabiln': l_list[23],
        'praktichn': l_list[24],
        'konservatizm': l_list[25],
        'realist': l_list[26],
        'otsutartist': l_list[27],
        'nechuvstvit': l_list[28],
        'rigidnost': l_list[29],
    }

    return person


def main():
  with open('nosql.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for col in reader:
        print(col[0], ":", col[1], ":", col[2])
        url = col[2]

        l_list = write_json_all(url)

        person_ = person(col, l_list)

        write_json(person_)


if __name__ == '__main__':
    main()