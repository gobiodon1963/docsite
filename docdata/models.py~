# -*- coding: utf-8 -*-

from django.utils import timezone
from django.db import models
import csv
import time
from dataparser.etdoc import parseData

# Create your models here.

class DocHeader(models.Model):
    doc_type = models.CharField(max_length=40, verbose_name=u'Тип')
    doc_number = models.CharField(max_length=20, verbose_name=u'Номер')
    doc_date = models.DateTimeField(verbose_name=u'Дата')
    apl_name = models.CharField(max_length=250, verbose_name=u'Контрагент')
    apl_inn = models.CharField(max_length=50, verbose_name=u'ИНН')
    apl_kpp = models.CharField(max_length=9, verbose_name=u'КПП')
    apl_address = models.CharField(max_length=250, verbose_name=u'Адрес')
    stock = models.CharField(max_length=50, verbose_name=u'Склад')
    account = models.CharField(max_length=20, verbose_name=u'Р/счет')
    currency = models.CharField(max_length=3, verbose_name=u'Вал')
    rate = models.FloatField(verbose_name=u'Курс валюты', default=1.0)
    total_sum = models.FloatField(verbose_name=u'Сумма')
    pp_number = models.CharField(max_length=10, blank=True, verbose_name=u'№ п\п')
    sf_number = models.CharField(max_length=10, blank=True, verbose_name=u'№ с-ф')
    def __str__(self):
        return '%s' % (self.doc_number)

class DocTable(models.Model):
    header = models.ForeignKey(DocHeader, on_delete=models.CASCADE, verbose_name=u'№ документа')
    art = models.CharField(max_length=20, verbose_name=u'Артикул')
    name = models.CharField(max_length=250, verbose_name=u'Наименование')
    unit_id = models.CharField(max_length=10, verbose_name=u'ед.')
    unit_code = models.CharField(max_length=3, verbose_name=u'Код')
    qty = models.FloatField(default=1, verbose_name=u'Количество')
    item_sum = models.FloatField(verbose_name=u'Сумма')
    item_weight = models.FloatField(verbose_name=u'Вес в кг', default=1.0)
    width = models.IntegerField(verbose_name=u'Ширина')
    height = models.IntegerField(verbose_name=u'Высота')
    gtd = models.CharField(max_length=30, verbose_name=u'ГТД')
    country_code = models.CharField(max_length=2, verbose_name=u'Страна')
    def __str__(self):
        return '%s - %10.2f %s - %s %s' % (self.art, self.qty, self.unit_id, self.gtd, self.country_code)

class Product(models.Model):
    art = models.CharField(max_length=20, verbose_name=u'Артикул')
    name = models.CharField(max_length=250, verbose_name=u'Наименование')
    full_name = models.CharField(max_length=1024, verbose_name=u'Описание',default='')
    unit_id = models.CharField(max_length=10, verbose_name=u'ед.')
    unit_code = models.CharField(max_length=3, verbose_name=u'Код')
    net_weight = models.FloatField(verbose_name=u'Вес в кг', default=1.0)
    need_to_import = models.BooleanField(default=False, verbose_name=u'Нужен импорт')
    def setValues(alist):
        self.art = alist['id']
        self.name = alist['descr']
        self.full_name = alist['spec']
        self.unit_id = alist['units']
        self.unit_code = alist['unit_code']

class Contractor(models.Model):
    apl_id = models.CharField(max_length=20, verbose_name=u'ID')
    name = models.CharField(max_length=250, verbose_name=u'Контрагент')
    inn = models.CharField(max_length=50, verbose_name=u'ИНН')
    kpp = models.CharField(max_length=9, verbose_name=u'КПП', blank=True)
    address = models.CharField(max_length=250, verbose_name=u'Адрес')
    need_to_import = models.BooleanField(default=False, verbose_name=u'Нужен импорт')
    hld = models.CharField(max_length=20, verbose_name=u'Холдинг', default='', blank=True)

class GoodsQty(models.Model):
    art = models.CharField(max_length=20, verbose_name=u'Артикул')
    stock_id = models.CharField(max_length=20, verbose_name=u'Склад')
    gtd = models.CharField(max_length=30, verbose_name=u'ГТД')
    paid = models.BooleanField(default=False, verbose_name=u'Оплачен')
    qty = models.FloatField(default=1, verbose_name=u'Количество')

def LoadGoodsFromCSV(fname):
    start_time = time.time()
    csv.register_dialect('tradecsv', delimiter=';')
    with open(fname) as csvfile:
        reader = csv.DictReader(csvfile,dialect='tradecsv')
        i = 0
        print('Cleaning goods table...')
        GoodsQty.objects.all().delete()
        print('Done.')
        for row in reader:
            g=Product(art=row['id'], stock_id=row['stock_id'], gtd=row['gtd'], paid=row['paid'], qty=row['qty'])
            g.save()
            i += 1
            print(i, art=row['id'], row['stock_id'], row['gtd'], row['paid'], row['qty'])
    return "Создано %d записей за %d секунд" % (i, time.time() - start_time)


def LoadProductsFromCSV(fname):
    start_time = time.time()
#    try:
    csv.register_dialect('tradecsv', delimiter=';')
    with open(fname) as csvfile:
        reader = csv.DictReader(csvfile,dialect='tradecsv')
        i = 0
        for row in reader:
            try:
                p=Product.objects.get(art=row['id'])
            except Product.DoesNotExist:
                p=Product(art=row['id'])
            p.name = row['descr']
            p.full_name = row['spec']
            p.unit_id = row['units']
            p.unit_code = row['unit_code']
            p.net_weight = row['net_weight']
            p.save()
            i += 1
            print(i, row['id'],row['descr'],row['spec'],row['units'],row['unit_code'],row['net_weight'])
    return "Обновлено %d записей за %d секунд" % (i, time.time() - start_time)
#    except Exception as e:
#        print("Ошибка при чтении CSV: ",e.args)
#        return "Ошибка при импорте из CSV"

def getProducts2Import(items):
    result=[]
    for key,val in items.items():
#        print (key, val)
        try:
            p=Product.objects.get(art=key)
        except Product.DoesNotExist:
            p=Product(art=key)
            p.name = val['descr']
            p.full_name = val['spec']
            p.unit_id = val['units']
            p.unit_code = val['unit_code']
            p.net_weight = val['net_weight']
            p.need_to_import = True
            p.save()
            result.append(val)
    return result

def LoadContractorsFromCSV(fname):
    start_time = time.time()
#    try:
    csv.register_dialect('tradecsv', delimiter=';')
    with open(fname) as csvfile:
        reader = csv.DictReader(csvfile,dialect='tradecsv')
        i = 0
        for row in reader:
            try:
                c=Contractor.objects.get(apl_id=row['apl_id'])
            except Contractor.DoesNotExist:
                c=Contractor(apl_id=row['apl_id'])
            c.name = row['name']
            c.inn = row['inn']
            c.kpp = row['kpp']
            c.address = row['address']
            c.save()
            i += 1
            print(i, row['apl_id'],row['inn'],row['kpp'])
    return "Обновлено %d записей за %d секунд" % (i, time.time() - start_time)
#    except Exception as e:
#        print("Ошибка при чтении CSV: ",e.args)
#        return "Ошибка при импорте из CSV"

def getContractors2Import(apls):
    result=[]
    for key,val in apls.items():
        try:
            c=Contractor.objects.get(inn=val['inn'],kpp=val['kpp'])
        except Contractor.DoesNotExist:
            result.append(val)
        except:
            continue
    return result

def loadPLinux():
    return LoadProductsFromCSV(r'./../exch_data/items2.csv')

def loadCLinux():
    return LoadContractorsFromCSV(r'./../exch_data/apls2.csv')

def save2CSV(fname, data_arr, fnames):
    with open(fname, 'w') as csvfile:
        writer=csv.DictWriter(csvfile, delimiter=';', fieldnames=fnames)
        writer.writerow(dict((fn,fn) for fn in fnames))
        for row in data_arr:
            writer.writerow(row)
    pass

def fillAplID(doc):
    doc['APL']=''
    doc['HLD']=''
    qs=Contractor.objects.filter(inn=doc['INN'],kpp=doc['KPP'])
    for q in qs:
        doc['APL']=q.apl_id
        doc['HLD']=q.hld

def fillAccInfo(doc):
    doc['SERIES'] = '???'
    if doc['ACC'] == 'Безналичная':
        doc['ACC'] = 'ДЕСАТ_'+doc['CUR'][:3]
        doc['SERIES'] = '65-'+doc['DATE'][:4]
    if doc['ACC'] == 'Наличная':
        doc['SERIES'] = ''
        doc['ACC'] = 'ПИТЕР_НАЛ'

def fillDocInfo(docs):
    for doc in docs:
        fillAplID(doc)
        fillAccInfo(doc)

def saveDocs2CSV(fname, docs):
    fout=open(fname, 'w')
    for doc in docs:
        if doc['TYPE'] == 'SI':
            for item in doc['TABLE']:
                fout.write("@D;%s;%s;%s;%f;0;0;%s;%s\n" % (item['ID'], item['QTY'], item['QTY'], float(item['SUM'])/float(item['QTY']), item['GTD'], item['STRANA']))
            fout.write("@H;%s;4;%s;%s;%s;%s;%s;%s;%.9e;%d;%s;%.9e;%s;%s;%s;;0;65\n" % (doc['NO'], doc['DATE'], doc['APL'], doc['HLD'], 'PITER_OPEN', doc['ACC'], doc['CUR'][:3], 1.0/doc['RATE'], 0, doc['CUR'][:3], 1.0/doc['RATE'], doc['SUM'], doc['SERIES'], doc['NUMBER']))
    fout.close()

def prepareData():
    items = {}
    apls = {}
    docs = []
    fin = open(r'./../exch_data/exch_data.xml','r')
    parseData(fin,docs,items,apls)
    fin.close()
    save2CSV(r'./../exch_data/new_items.csv', getProducts2Import(items), ['id','descr','spec', 'units', 'unit_code', 'net_weight'])
    save2CSV(r'./../exch_data/new_apls.csv', getContractors2Import(apls), ['apl_id', 'name', 'inn', 'kpp', 'address'])
    fillDocInfo(docs)
    saveDocs2CSV(r'./../exch_data/new_doc.csv', docs)

