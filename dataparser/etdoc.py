# -*- coding: utf-8 -*-

from xml.etree.ElementTree import parse

def getAttributes(node):
    attribs = {}
    for a in node.findall(u'Свойство'):
        v = a.find(u'Значение')
        if v is not None:
            attribs[a.attrib[u'Имя']] = v.text
        else:
            attribs[a.attrib[u'Имя']] = ''
    return attribs

def getDocHeader(type,attr,table=[]):
    doc = dict()
    doc['TYPE']=type
    doc['NO']=attr[u'Номер'].strip()
    doc['DATE']=attr[u'Дата'].replace('T',' ').strip().replace('-','.')
    doc['NAME']=attr[u'НаименованиеПокупателя'].strip()
    doc['INN']=attr[u'ИННПокупателя'].strip()
    doc['KPP']=attr[u'КПППокупателя'].strip()
    if u'АдресПокупателя' not in attr:
        doc['ADDRESS']=''
    else:
        doc['ADDRESS']=attr[u'АдресПокупателя'].strip()
    doc['ACC']=attr[u'ВидОплаты'].strip()
    doc['CUR']=attr[u'Валюта'].strip()
    if u'КурсВалюты' not in attr:
        doc['RATE'] = 1.0
    else:
        doc['RATE']=float(attr[u'КурсВалюты'].strip())
    if doc['RATE'] < 1.0:
        doc['RATE'] = 1.0
    doc['SUM']=attr[u'Сумма'].strip()
    if u'НомерСФ' in attr:
        doc['NUMBER']=attr[u'НомерСФ'].strip()
    else:
        doc['NUMBER']='0'
    if u'НомерПП' not in attr:
        doc['PPNUM']='0'
    else:
        doc['PPNUM']=attr[u'НомерПП'].strip()
    if u'НомерСФНаАванс' in attr:
        doc['NUMBER']=attr[u'НомерСФНаАванс'].strip()
    doc['TABLE'] = table
    return doc

def getDistrItem(attr):
    item = dict()
    item['ID'] = attr[u'Артикул'].strip()
    item['DESCR'] = attr[u'Наименование'].strip()
    item['SPEC'] = attr[u'НаименованиеПолное'].strip()
    item['UNITS'] = attr[u'ЕдиницаИзмерения'].strip()
    item['UNIT_CODE'] = attr[u'КодЕдиницыИзмерения'].strip()
    item['QTY'] = attr[u'Количество'].strip()
    item['SUM'] = attr[u'СуммаСНДС'].strip()
    item['NET_WEIGHT'] = attr[u'ВесЕдиницы'].strip()
    item['WIDTH'] = attr[u'Ширина'].strip()
    item['HEIGHT'] = attr[u'Высота'].strip()
    item['PROFIL'] = attr[u'Профиль'].strip()
    item['GTD'] = attr[u'НомерГТД'].strip()
    item['STRANA'] = attr[u'СтранаПроисхождения'].strip()
    item['STOCK'] = attr[u'Склад'].strip()
    return item

def parseData(file_in,docs,items,apls):
    tree = parse(file_in)

    for obj in tree.findall(u'Объект'):
        doc_type = obj.attrib[u'ИмяПравила']
        index = obj.attrib[u'Нпп']

#       Реализация Покупателю

        if doc_type == u'РеализацияПокупателю':
#            print (u'РеализацияПокупателю')
            table = obj.find(u'ТабличнаяЧасть')
            if table is not None:
                i_table = []
                for item in table.findall(u'Запись'):

                    d_item = getDistrItem(getAttributes(item))
                    i_table.append(d_item)

                    if d_item['ID'] not in items:
                        items[d_item['ID']] = {'id':d_item['ID'], 'descr':d_item['DESCR'], 'spec':d_item['SPEC'], 'units':d_item['UNITS'], 'unit_code':d_item['UNIT_CODE'], 'net_weight': d_item['NET_WEIGHT']}

                doc = getDocHeader('SI',getAttributes(obj),i_table)
                docs.append(doc)

                apl_key = doc['INN']+"/"+doc['KPP']
                if apl_key not in apls:
                    apls[apl_key] = {'apl_id':'', 'name':doc['NAME'], 'inn':doc['INN'], 'kpp':doc['KPP'], 'address' : doc['ADDRESS']}

#       Оплата Покупателя
        if doc_type == u'ОплатаПокупателя':
#            print (u'ОплатаПокупателя')
            doc = getDocHeader('CP',getAttributes(obj))
            docs.append(doc)

if __name__ == '__main__':
    import sys

    items = {}
    apls = {}
    docs = []
    fin = open(r'./../../exch_data/exch_data.xml','r')
    parseData(fin,docs,items,apls)
    for doc in docs:
        for item in doc['TABLE']:
            print("@D;%s;%s;%s;%s" % (item['ID'],item['DESCR'],item['QTY'],item['SUM']))
        print("@H;%s;%s;%s;%s;%s;%s;%s;%s" % (doc['TYPE'], doc['NUMBER'], doc['SUM'], doc['CUR'], doc['ACC'], doc['NO'], doc['DATE'], doc['NAME']))
    print("#####")
    for key in items:
        val = items[key]
        print("%s;%s;%s;%s;%sl%s" % (key, val['descr'], val['spec'], val['units'], val['unit_code'], val['net_weight']))
    print("#####")
    for key in apls:
        val = apls[key]
        print("%s;%s;%s;%s;%s" % (val['apl_id'], val['name'], val['inn'], val['kpp'], val['address']))
    fin.close()

