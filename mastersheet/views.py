from django.shortcuts import render, redirect
from django.http import HttpResponse
from mastersheet.models import Round2database
from slot.models import database
from django.conf import settings

import pygsheets
import pandas as pd


gc = pygsheets.authorize(service_file='slot/creds.json')

# Create your views here.


def adminLogin(request):
    return render(request, 'adminLogin.html')


def schedule(request):
    if request.method == 'POST':
        username = request.POST.get('interviewer')
        password = request.POST.get('password')
        if password == settings.PASSWORD:
            sh = gc.open('PI R1 Mastersheet')
            wks = sh[0]
            w = wks.get_all_records()

            remaining = []
            completed = []
            notReg = []
            selected = []
            now = []
            next = []

            for i in range(len(w)):
                if w[i]['taken'] == '' and w[i]['slot'] != 'FALSE':
                    remaining.append(w[i])
                if w[i]['taken'] == 'True':
                    completed.append(w[i])
                if w[i]['slot'] == 'FALSE':
                    notReg.append(w[i])
                if w[i]['selected'] == 'Yes':
                    selected.append(w[i])
                if w[i]['slot'] == '17/1/2022 at 6:00 PM':
                    now.append(w[i])
                if w[i]['slot'] == '17/1/2022 at 6:30 PM':
                    next.append(w[i])
            context = {'remaining': remaining, 'completed': completed,
                    'error': False, 'interviewer': username, 'notReg': notReg, 'selected': selected, 'now':now, 'next':next}
            return render(request, 'schedule.html', context)
        else:
            context = {'error': True}
            return render(request, 'adminLogin.html', context)
    elif request.method == 'GET':
        sh = gc.open('PI R1 Mastersheet')
        wks = sh[0]
        w = wks.get_all_records()
        interviewer = request.GET.get('interviewer')
        taken = request.GET.get('taken')
        remarks = request.GET.get('remarks')
        selected = request.GET.get('selected')
        if selected == None:
            selected = 'No'
        else:
            selected = 'Yes'

        for i in range(len(w)):
            if w[i]['roll'] == taken:
                locationInterviewer = 'G' + str(i+2)
                locationRemarks = 'H' + str(i+2)
                locationTaken = 'I' + str(i+2)
                locationSelected = 'J' + str(i+2)
                wks.update_value(locationInterviewer, interviewer)
                wks.update_value(locationRemarks, remarks)
                wks.update_value(locationTaken, 'TRUE')
                wks.update_value(locationSelected, 'Yes')
                    
        remaining = []
        completed = []
        notReg = []
        selected = []
        now = []
        next = []

        for i in range(len(w)):
            if w[i]['taken'] == '' and w[i]['slot'] != 'FALSE':
                remaining.append(w[i])
            if w[i]['taken'] == 'True':
                completed.append(w[i])
            if w[i]['slot'] == 'FALSE':
                notReg.append(w[i])
            if w[i]['selected'] == 'Yes':
                selected.append(w[i])
            if w[i]['slot'] == '17/1/2022 at 6:00 PM':
                    now.append(w[i])
            if w[i]['slot'] == '17/1/2022 at 7:00 PM':
                    next.append(w[i])
        context = {'remaining': remaining, 'completed': completed,
                    'error': False, 'interviewer': interviewer, 'notReg': notReg, 'selected': selected, 'now':now, 'next':next}
        return render(request, 'schedule.html', context)
        

        
    
