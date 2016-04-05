# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
import datetime
from docsite.forms import HomeForm
#from docdata.models import LoadProductsFromCSV
from docdata.models import loadPLinux, loadCLinux

def homepage_view(request, command=''):
    messages = []
    if command == 'load_items':
        messages = ['Обновили номенклатуру']
        messages.append(loadPLinux())
    if command == 'load_apls':
        messages = ['Обновили контрагентов']
        messages.append(loadCLinux())
    now = datetime.datetime.now()
    return render_to_response('home.html', {'current_date': now, 'messages': messages})
