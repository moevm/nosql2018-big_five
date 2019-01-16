import requests
import bs4
from bs4 import BeautifulSoup

import os
import csv
import json
import codecs
from analiz import Ui_Form1  # импорт нашего сгенерированного файла
from table_group import Ui_Form2  # импорт нашего сгенерированного файла
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from glv import Ui_MainWindow  # импорт нашего сгенерированного файла
from table import Ui_Form  # импорт нашего сгенерированного файла
import sys
from pymongo import DESCENDING as DESCENDING
from pymongo import MongoClient
from pymongo.database import Database as MongoDatabase
from pymongo.collection import Collection as MongoCollection

client = MongoClient('mongodb://127.0.0.1:27017/')
# client = MongoClient("localhost", 27017)
db = client['test']
kr = 0
collection_stud = db['users']
collection_stud.delete_many({})
list_all = []
colom_all = []
col1  = []
colr = []
coliv = []
coliu = []
colp = []
colz = []
col2 = []
col3 = []
colavg = []
coliz = []
colizvn = []
for_sort = []
index2 = 0


class analiz(QtWidgets.QMainWindow):
    def __init__(self):
        super(analiz, self).__init__()
        self.ui = Ui_Form1()
        self.ui.setupUi(self)
        self.ui.view1.clicked.connect(self.start1)
        self.ui.view2.clicked.connect(self.start2)

        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox_sort1.setCurrentIndex(0)

    def start2(self):
        if self.ui.comboBox_group.currentIndex() == 0:
            _group = '5381'
        elif self.ui.comboBox_group.currentIndex() == 1:
            _group = '5383'

        colavg = []
        #k = db.users.aggregate({"names": {'$avg': 'group'}})
        pipe = [{'$match': {'groupp': _group}}, {'$group': {'_id': None, 'avg1': {'$avg': '$inrover'}, 'avg2': {'$avg': '$passivn'}, 'avg3': {'$avg': '$podchin'}, 'avg4': {'$avg': '$zamknut'}, 'avg5': {'$avg': '$izbegvpet'}, 'avg6': {'$avg': '$izbegvnim'}, 'avg7': {'$avg': '$obosob'}, 'avg8': {'$avg': '$ravnodush'}, 'avg9': {'$avg': '$sopern'}, 'avg10': {'$avg': '$podozrit'}, 'avg11': {'$avg': '$neponimanie'}, 'avg12': {'$avg': '$samouvaz'}, 'avg13': {'$avg': '$impulsiv'}, 'avg14': {'$avg': '$neakkurat'}, 'avg15': {'$avg': '$otsutnastoy'}, 'avg16': {'$avg': '$bezotvet'}, 'avg17': {'$avg': '$impulsivn2'}, 'avg18': {'$avg': '$bespechn'}, 'avg19': {'$avg': '$emocust'}, 'avg20': {'$avg': '$bezzabotn'}, 'avg21': {'$avg': '$rasslablen'}, 'avg22': {'$avg': '$emockomfort'}, 'avg23': {'$avg': '$samodost'}, 'avg24': {'$avg': '$emocstabiln'}, 'avg25': {'$avg': '$praktich'}, 'avg26': {'$avg': '$konservatizm'}, 'avg27': {'$avg': '$realist'}, 'avg28': {'$avg': '$otsutartist'}, 'avg29': {'$avg': '$nechuvstvit'}, 'avg30': {'$avg': '$rigidnost'}}}]
        pipe_min = [{'$match': {'groupp': _group}}, {'$group': {'_id': None, 'avg1': {'$min': '$inrover'}, 'avg2': {'$min': '$passivn'}, 'avg3': {'$min': '$podchin'}, 'avg4': {'$min': '$zamknut'}, 'avg5': {'$min': '$izbegvpet'}, 'avg6': {'$min': '$izbegvnim'}, 'avg7': {'$min': '$obosob'}, 'avg8': {'$min': '$ravnodush'}, 'avg9': {'$min': '$sopern'}, 'avg10': {'$min': '$podozrit'}, 'avg11': {'$min': '$neponimanie'}, 'avg12': {'$min': '$samouvaz'}, 'avg13': {'$min': '$impulsiv'}, 'avg14': {'$min': '$neakkurat'}, 'avg15': {'$min': '$otsutnastoy'}, 'avg16': {'$min': '$bezotvet'}, 'avg17': {'$min': '$impulsivn2'}, 'avg18': {'$min': '$bespechn'}, 'avg19': {'$min': '$emocust'}, 'avg20': {'$min': '$bezzabotn'}, 'avg21': {'$min': '$rasslablen'}, 'avg22': {'$min': '$emockomfort'}, 'avg23': {'$min': '$samodost'}, 'avg24': {'$min': '$emocstabiln'}, 'avg25': {'$min': '$praktich'}, 'avg26': {'$min': '$konservatizm'}, 'avg27': {'$min': '$realist'}, 'avg28': {'$min': '$otsutartist'}, 'avg29': {'$min': '$nechuvstvit'}, 'avg30': {'$min': '$rigidnost'}}}]
        pipe_max = [{'$match': {'groupp': _group}}, {'$group': {'_id': None, 'avg1': {'$max': '$inrover'}, 'avg2': {'$max': '$passivn'}, 'avg3': {'$max': '$podchin'}, 'avg4': {'$max': '$zamknut'}, 'avg5': {'$max': '$izbegvpet'}, 'avg6': {'$max': '$izbegvnim'}, 'avg7': {'$max': '$obosob'}, 'avg8': {'$max': '$ravnodush'}, 'avg9': {'$max': '$sopern'}, 'avg10': {'$max': '$podozrit'}, 'avg11': {'$max': '$neponimanie'}, 'avg12': {'$max': '$samouvaz'}, 'avg13': {'$max': '$impulsiv'}, 'avg14': {'$max': '$neakkurat'}, 'avg15': {'$max': '$otsutnastoy'}, 'avg16': {'$max': '$bezotvet'}, 'avg17': {'$max': '$impulsivn2'}, 'avg18': {'$max': '$bespechn'}, 'avg19': {'$max': '$emocust'}, 'avg20': {'$max': '$bezzabotn'}, 'avg21': {'$max': '$rasslablen'}, 'avg22': {'$max': '$emockomfort'}, 'avg23': {'$max': '$samodost'}, 'avg24': {'$max': '$emocstabiln'}, 'avg25': {'$max': '$praktich'}, 'avg26': {'$max': '$konservatizm'}, 'avg27': {'$max': '$realist'}, 'avg28': {'$max': '$otsutartist'}, 'avg29': {'$max': '$nechuvstvit'}, 'avg30': {'$max': '$rigidnost'}}}]

        k = db.users.aggregate(pipeline=pipe)
        for userb in k:
            col4 = colavg.append((userb.get('avg1'), userb.get('avg2'), userb.get('avg3'), userb.get('avg4'), userb.get('avg5'), userb.get('avg6'), userb.get('avg7'), userb.get('avg8'), userb.get('avg9'), userb.get('avg10'), userb.get('avg11'), userb.get('avg12'), userb.get('avg13'), userb.get('avg14'), userb.get('avg15'), userb.get('avg16'), userb.get('avg17'), userb.get('avg18'), userb.get('avg19'), userb.get('avg20'), userb.get('avg21'), userb.get('avg22'), userb.get('avg23'), userb.get('avg24'), userb.get('avg25'), userb.get('avg26'), userb.get('avg27'), userb.get('avg28'), userb.get('avg29'), userb.get('avg30')))

        k = db.users.aggregate(pipeline=pipe_min)
        for userb in k:
            col4 = colavg.append((userb.get('avg1'), userb.get('avg2'), userb.get('avg3'), userb.get('avg4'), userb.get('avg5'), userb.get('avg6'), userb.get('avg7'), userb.get('avg8'), userb.get('avg9'), userb.get('avg10'), userb.get('avg11'), userb.get('avg12'), userb.get('avg13'), userb.get('avg14'), userb.get('avg15'), userb.get('avg16'), userb.get('avg17'), userb.get('avg18'), userb.get('avg19'), userb.get('avg20'), userb.get('avg21'), userb.get('avg22'), userb.get('avg23'), userb.get('avg24'), userb.get('avg25'), userb.get('avg26'), userb.get('avg27'), userb.get('avg28'), userb.get('avg29'), userb.get('avg30')))

        k = db.users.aggregate(pipeline=pipe_max)
        for userb in k:
            col4 = colavg.append((userb.get('avg1'), userb.get('avg2'), userb.get('avg3'), userb.get('avg4'), userb.get('avg5'), userb.get('avg6'), userb.get('avg7'), userb.get('avg8'), userb.get('avg9'), userb.get('avg10'), userb.get('avg11'), userb.get('avg12'), userb.get('avg13'), userb.get('avg14'), userb.get('avg15'), userb.get('avg16'), userb.get('avg17'), userb.get('avg18'), userb.get('avg19'), userb.get('avg20'), userb.get('avg21'), userb.get('avg22'), userb.get('avg23'), userb.get('avg24'), userb.get('avg25'), userb.get('avg26'), userb.get('avg27'), userb.get('avg28'), userb.get('avg29'), userb.get('avg30')))

        self.diff_window = mywindowTable_sort(colavg)
        self.diff_window.setWindowTitle('Таблица')
        self.diff_window.show()


    def start1(self):
        if self.ui.comboBox_sort1.currentIndex() == 0:
            sort_ = 1
        elif self.ui.comboBox_sort1.currentIndex() == 1:
            sort_ = -1
        if self.ui.comboBox.currentIndex() == 0:
            kriterii = 'inrover'
            b = db.users.find().sort(kriterii, sort_)
            if sort_ == 1:
             for userb in b:
                col5 = coliv.append((userb.get('name'), userb.get('groupp'), userb.get('inrover'), userb.get('passivn'), userb.get('podchin'), userb.get('zamknut'), userb.get('izbegvpet'), userb.get('izbegvnim'), userb.get('obosob'), userb.get('ravnodush'), userb.get('sopern'), userb.get('podozrit'), userb.get('neponimanie'), userb.get('samouvaz'), userb.get('impulsiv'), userb.get('neakkurat'), userb.get('otsutnastoy'), userb.get('bezotvet'), userb.get('impulsivn2'), userb.get('bespechn'), userb.get('emocust'), userb.get('bezzabotn'), userb.get('rasslablen'), userb.get('emockomfort'), userb.get('samodost'), userb.get('emocstabiln'), userb.get('praktich'), userb.get('konservatizm'), userb.get('realist'), userb.get('otsutartist'), userb.get('nechuvstvit'), userb.get('rigidnost')))
             for_sort = coliv

            elif sort_ == -1:
                for userb in b:
                    col5 = coliu.append((userb.get('name'), userb.get('groupp'), userb.get('inrover'), userb.get('passivn'), userb.get('podchin'), userb.get('zamknut'), userb.get('izbegvpet'), userb.get('izbegvnim'), userb.get('obosob'), userb.get('ravnodush'), userb.get('sopern'), userb.get('podozrit'), userb.get('neponimanie'), userb.get('samouvaz'), userb.get('impulsiv'), userb.get('neakkurat'), userb.get('otsutnastoy'), userb.get('bezotvet'), userb.get('impulsivn2'), userb.get('bespechn'), userb.get('emocust'), userb.get('bezzabotn'), userb.get('rasslablen'), userb.get('emockomfort'), userb.get('samodost'), userb.get('emocstabiln'), userb.get('praktich'), userb.get('konservatizm'), userb.get('realist'), userb.get('otsutartist'), userb.get('nechuvstvit'), userb.get('rigidnost')))
                for_sort = coliu


        elif self.ui.comboBox.currentIndex() == 1:
            kriterii = 'passivn'
            с = db.users.find().sort(kriterii, sort_)
            for userс in с:
                col5 = colr.append((userс.get('name'), userс.get('groupp'), userс.get('inrover'), userс.get('passivn'), userс.get('podchin'), userс.get('zamknut'), userс.get('izbegvpet'), userс.get('izbegvnim'), userс.get('obosob'), userс.get('ravnodush'), userс.get('sopern'), userс.get('podozrit'), userс.get('neponimanie'), userс.get('samouvaz'), userс.get('impulsiv'), userс.get('neakkurat'), userс.get('otsutnastoy'), userс.get('bezotvet'), userс.get('impulsivn2'), userс.get('bespechn'), userс.get('emocust'), userс.get('bezzabotn'), userс.get('rasslablen'), userс.get('emockomfort'), userс.get('samodost'), userс.get('emocstabiln'), userс.get('praktich'), userс.get('konservatizm'), userс.get('realist'), userс.get('otsutartist'), userс.get('nechuvstvit'), userс.get('rigidnost')))
            print(colr)
            for_sort = colr
        elif self.ui.comboBox.currentIndex() == 2:
            kriterii = 'podchin'
            с = db.users.find().sort(kriterii, sort_)
            for userp in с:
                col5 = colp.append((userp.get('name'), userp.get('groupp'), userp.get('inrover'), userp.get('passivn'), userp.get('podchin'), userp.get('zamknut'), userp.get('izbegvpet'), userp.get('izbegvnim'), userp.get('obosob'), userp.get('ravnodush'), userp.get('sopern'), userp.get('podozrit'), userp.get('neponimanie'), userp.get('samouvaz'), userp.get('impulsiv'), userp.get('neakkurat'), userp.get('otsutnastoy'), userp.get('bezotvet'), userp.get('impulsivn2'), userp.get('bespechn'), userp.get('emocust'), userp.get('bezzabotn'), userp.get('rasslablen'), userp.get('emockomfort'), userp.get('samodost'), userp.get('emocstabiln'), userp.get('praktich'), userp.get('konservatizm'), userp.get('realist'), userp.get('otsutartist'), userp.get('nechuvstvit'), userp.get('rigidnost')))
            for_sort = colp

        elif self.ui.comboBox.currentIndex() == 3:
            kriterii = 'zamknut'
            с = db.users.find().sort(kriterii, sort_)
            for userp in с:
                col5 = colz.append((userp.get('name'), userp.get('groupp'), userp.get('inrover'), userp.get('passivn'), userp.get('podchin'), userp.get('zamknut'), userp.get('izbegvpet'), userp.get('izbegvnim'), userp.get('obosob'), userp.get('ravnodush'), userp.get('sopern'), userp.get('podozrit'), userp.get('neponimanie'), userp.get('samouvaz'), userp.get('impulsiv'), userp.get('neakkurat'), userp.get('otsutnastoy'), userp.get('bezotvet'), userp.get('impulsivn2'), userp.get('bespechn'), userp.get('emocust'), userp.get('bezzabotn'), userp.get('rasslablen'), userp.get('emockomfort'), userp.get('samodost'), userp.get('emocstabiln'), userp.get('praktich'), userp.get('konservatizm'), userp.get('realist'), userp.get('otsutartist'), userp.get('nechuvstvit'), userp.get('rigidnost')))
            for_sort = colz

        elif self.ui.comboBox.currentIndex() == 4:
            kriterii = 'izbegvpet'
            с = db.users.find().sort(kriterii, sort_)
            for userp in с:
                col5 = coliz.append((userp.get('name'), userp.get('groupp'), userp.get('inrover'), userp.get('passivn'), userp.get('podchin'), userp.get('zamknut'), userp.get('izbegvpet'), userp.get('izbegvnim'), userp.get('obosob'), userp.get('ravnodush'), userp.get('sopern'), userp.get('podozrit'), userp.get('neponimanie'), userp.get('samouvaz'), userp.get('impulsiv'), userp.get('neakkurat'), userp.get('otsutnastoy'), userp.get('bezotvet'), userp.get('impulsivn2'), userp.get('bespechn'), userp.get('emocust'), userp.get('bezzabotn'), userp.get('rasslablen'), userp.get('emockomfort'), userp.get('samodost'), userp.get('emocstabiln'), userp.get('praktich'), userp.get('konservatizm'), userp.get('realist'), userp.get('otsutartist'), userp.get('nechuvstvit'), userp.get('rigidnost')))
            print(coliz)
            for_sort = coliz

        elif self.ui.comboBox.currentIndex() == 5:
            kriterii = 'izbegvnim'
            с = db.users.find().sort(kriterii, sort_)
            for userp in с:
                col5 = colizvn.append((userp.get('name'), userp.get('groupp'), userp.get('inrover'), userp.get('passivn'), userp.get('podchin'), userp.get('zamknut'), userp.get('izbegvpet'), userp.get('izbegvnim'), userp.get('obosob'), userp.get('ravnodush'), userp.get('sopern'), userp.get('podozrit'), userp.get('neponimanie'), userp.get('samouvaz'), userp.get('impulsiv'), userp.get('neakkurat'), userp.get('otsutnastoy'), userp.get('bezotvet'), userp.get('impulsivn2'), userp.get('bespechn'), userp.get('emocust'), userp.get('bezzabotn'), userp.get('rasslablen'), userp.get('emockomfort'), userp.get('samodost'), userp.get('emocstabiln'), userp.get('praktich'), userp.get('konservatizm'), userp.get('realist'), userp.get('otsutartist'), userp.get('nechuvstvit'), userp.get('rigidnost')))
            print(colizvn)
            for_sort = colizvn

        self.diff_window = mywindowTable(for_sort)
        self.diff_window.setWindowTitle('Таблица')
        self.diff_window.show()



class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.importButton.clicked.connect(self.importButton_onClick)
        self.ui.tablButton.clicked.connect(self.tablButton_onClick)
        self.ui.analizButton.clicked.connect(self.analizButton_onClick)
        self.ui.exportButton.clicked.connect(self.exportButton_onClick)

    def importButton_onClick(self):
        with open('file.json', 'w') as f:  # очистка json файла
            del f
        kolv = 0
        global l_list
        with open('nosql.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for col in reader:
                # print(col[0], ":", col[1], ":", col[2])
                url = col[2]

                l_list = write_json_all(url)
                db.users.save({'name': col[0],
                               'groupp': col[1],
                               'url': col[2],
                               'inrover': l_list[0], 'passivn': l_list[1], 'podchin': l_list[2], 'zamknut': l_list[3],
                               'izbegvpet': l_list[4], 'izbegvnim': l_list[5],
                               'obosob': l_list[6], 'ravnodush': l_list[7], 'sopern': l_list[8], 'podozrit': l_list[9],
                               'neponimanie': l_list[10], 'samouvaz': l_list[11],
                               'impulsiv': l_list[12], 'neakkurat': l_list[13], 'otsutnastoy': l_list[14],
                               'bezotvet': l_list[15], 'impulsivn2': l_list[16], 'bespechn': l_list[17],
                               'emocust': l_list[18], 'bezzabotn': l_list[19], 'rasslablen': l_list[20],
                               'emockomfort': l_list[21], 'samodost': l_list[22], 'emocstabiln': l_list[23],
                               'praktich': l_list[24], 'konservatizm': l_list[25], 'realist': l_list[26],
                               'otsutartist': l_list[27], 'nechuvstvit': l_list[28], 'rigidnost': l_list[29]})
                person_ = person(col, l_list)
                kolv+=1
                # posts.insert(person_)
                write_json(person_)
        a = db.users.find()
        for user in a:
            print(user)


    def exportButton_onClick(self):
        x = json.loads(open('file.json').read())
        f = csv.writer(open("output.csv", "w"))
        f.writerow(["name", "groupp", "inrover", "passivn", "podchin", "zamknut", "izbegvpet", "izbegvnim", "obosob", "ravnodush", "sopern", "podozrit", "neponimanie", "samouvaz", "impulsiv", "neakkurat", "otsutnastoy", "bezotvet", "impulsivn2", "bespechn", "emocust", "bezzabotn", "rasslablen", "emockomfort", "samodost", "emocstabiln", "praktich", "konservatizm", "realist", "otsutartist", "nechuvstvit", "rigidnost"])
        for x in x:
            f.writerow([x["name"],
                        x["groupp"],
                        x["inrover"],
                        x["passivn"],
                        x["podchin"],
                        x["zamknut"],x["izbegvpet"], x["izbegvnim"], x["obosob"], x["ravnodush"], x["sopern"], x["podozrit"], x["neponimanie"], x["samouvaz"], x["impulsiv"], x["neakkurat"], x["otsutnastoy"], x["bezotvet"], x["impulsivn2"], x["bespechn"], x["emocust"], x["bezzabotn"], x["rasslablen"], x["emockomfort"], x["samodost"], x["emocstabiln"], x["praktich"], x["konservatizm"], x["realist"], x["otsutartist"], x["nechuvstvit"], x["rigidnost"]])
        #write_csv(read_json('file.json'), 'output.csv')


    def tablButton_onClick(self):
            col3 = tablefull1(db)
            self.diff_window = mywindowTable(col3)
            self.diff_window.setWindowTitle('Таблица')
            self.diff_window.show()


    def analizButton_onClick(self):
        self.diff_window = analiz()
        self.diff_window.setWindowTitle('Анализ')
        self.diff_window.show()



class mywindowTable_sort(QtWidgets.QMainWindow):
    def __init__(self, colavg):
        super(mywindowTable_sort, self).__init__()
        self.ui = Ui_Form2()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnCount(30)
        self.ui.tableWidget.setRowCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(["интроверсия", "пассивность", "подчиненность", "замкнутость", "избегание впечатлений", "избегание внимания", "обособленность", "равнодушие", "соперничество", "подозрительность", "непонимание", "самоуважение", "импульсивность", "неаккуратность", "отсутствие настойчивости", "безответственность", "импульсивность", "беспечность", "эмоц. устойчивость", "беззаботность", "расслабленность", "эмоц. комфортность", "самодостаточность", "эмоц. стабильность", "практичность", "консерватизм", "реалистичность", "отсутствие артистичности", "нечувствительность", "ригидность"])
        self.ui.tableWidget.setVerticalHeaderLabels(["Средний", "Минимальный", "Максимальный"])


        row = 0
        for tup in colavg:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1


class mywindowTable(QtWidgets.QMainWindow):
    def __init__(self, col4):
        super(mywindowTable, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnCount(32)
        self.ui.tableWidget.setRowCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Имя", "Группа", "интроверсия", "пассивность", "подчиненность", "замкнутость", "избегание впечатлений", "избегание внимания", "обособленность", "равнодушие", "соперничество", "подозрительность", "непонимание", "самоуважение", "импульсивность", "неаккуратность", "отсутствие настойчивости", "безответственность", "импульсивность", "беспечность", "эмоц. устойчивость", "беззаботность", "расслабленность", "эмоц. комфортность", "самодостаточность", "эмоц. стабильность", "практичность", "консерватизм", "реалистичность", "отсутствие артистичности", "нечувствительность", "ригидность"])
        #self.ui.tableWidget.setItem(0, 1, QTableWidgetItem('text'))
        #col3 = tablefull1(db)
        #print(col4)
        row = 0
        for tup in col4:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1


def read_json(filename):
    return json.loads(open(filename).read())

def write_csv(data,filename):
    with open(filename) as outf:
        writer = csv.DictWriter(outf, data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)



def tablefull1(db): #для создания списка
    #b = db.users.find().sort('inrover', 1)
    b = db.users.find()
    for userb in b:
        col2 = tablefull(userb)
    return col2

def tablesort(b): #для создания списка
    for userb in b:
        col4 = tablefull(userb)
    return col4

def tablefull(d):  #для создания списка
    col2.append((d.get('name'), d.get('groupp'), d.get('inrover'), d.get('passivn'), d.get('podchin'), d.get('zamknut'), d.get('izbegvpet'), d.get('izbegvnim'), d.get('obosob'), d.get('ravnodush'), d.get('sopern'), d.get('podozrit'), d.get('neponimanie'), d.get('samouvaz'), d.get('impulsiv'), d.get('neakkurat'), d.get('otsutnastoy'), d.get('bezotvet'), d.get('impulsivn2'), d.get('bespechn'), d.get('emocust'), d.get('bezzabotn'), d.get('rasslablen'), d.get('emockomfort'), d.get('samodost'), d.get('emocstabiln'), d.get('praktich'), d.get('konservatizm'), d.get('realist'), d.get('otsutartist'), d.get('nechuvstvit'), d.get('rigidnost')))
    return col2


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


    #name3_list = b.find(class_='stdTbl')    #парсинг названия характеристики
    #name3_list_items = name3_list.find_all('a')

    l_list = []

    for name in name_list_items:
        names = name.contents[0]

        if (names < '9' or names == '9') and (names > '1' or names == '1'):
            l_list.append(names)
    i = 0
    while i < 30:
        l_list[i] = int(l_list[i])
        i += 1
    print(l_list)
    return l_list

def person(column, l_list):     #формирование коллекции
    person = {
        'name': column[0],
        'groupp': column[1],
        'url': column[2],
        'inrover': l_list[0], 'passivn': l_list[1], 'podchin': l_list[2], 'zamknut': l_list[3], 'izbegvpet': l_list[4], 'izbegvnim': l_list[5],
        'obosob':l_list[6], 'ravnodush': l_list[7], 'sopern': l_list[8], 'podozrit': l_list[9], 'neponimanie': l_list[10], 'samouvaz': l_list[11],
        'impulsiv': l_list[12], 'neakkurat': l_list[13], 'otsutnastoy': l_list[14], 'bezotvet': l_list[15], 'impulsivn2': l_list[16], 'bespechn': l_list[17],
        'emocust': l_list[18], 'bezzabotn': l_list[19],'rasslablen': l_list[20], 'emockomfort': l_list[21], 'samodost': l_list[22], 'emocstabiln': l_list[23],
        'praktich': l_list[24], 'konservatizm': l_list[25], 'realist': l_list[26], 'otsutartist': l_list[27], 'nechuvstvit': l_list[28], 'rigidnost': l_list[29],
    }

    return person


def main():
  app = QtWidgets.QApplication([])
  application = mywindow()
  application.show()

  sys.exit(app.exec())



if __name__ == '__main__':
    main()