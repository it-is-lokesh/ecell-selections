from django.shortcuts import render, redirect
from django.http import HttpResponse
from mastersheet.models import Round2database
from slot.models import database
from django.conf import settings
# Create your views here.


def adminLogin(request):
    return render(request, 'adminLogin.html')


def schedule(request):
    if request.method == 'POST':
        username = request.POST.get('interviewer')
        password = request.POST.get('password')
        if password == settings.PASSWORD:
            remaining = Round2database.objects.filter(taken='False').exclude(slot='False')
            completed = Round2database.objects.filter(taken='True')
            notReg = Round2database.objects.filter(slot='False')
            selected = Round2database.objects.filter(selected='Yes')
            context = {'remaining': remaining, 'completed': completed,
                    'error': False, 'interviewer': username, 'notReg': notReg, 'selected': selected}
            return render(request, 'schedule.html', context)
        else:
            context = {'error': True}
            return render(request, 'adminLogin.html', context)
    elif request.method == 'GET':
        interviewer = request.GET.get('interviewer')
        taken = request.GET.get('taken')
        remarks = request.GET.get('remarks')
        selected = request.GET.get('selected')
        if selected == None:
            selected = 'No'
        else:
            selected = 'Yes'
        Round2database.objects.filter(roll=taken).update(taken='True', selected=selected, remarks=remarks, interviewer=interviewer)
        remaining = Round2database.objects.filter(taken='False').exclude(slot='False')
        completed = Round2database.objects.filter(taken='True')
        notReg = Round2database.objects.filter(slot='False')
        selected = Round2database.objects.filter(selected='Yes')
        context = {'remaining': remaining, 'completed': completed,
                    'error': False, 'interviewer': interviewer, 'notReg': notReg, 'selected': selected}
        return render(request, 'schedule.html', context)
        

        
    
