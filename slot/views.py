from django.shortcuts import render
from slot.models import database
from mastersheet.models import Round2database
from django.core.mail import EmailMessage
from slot.forms import slotForm
from django.conf import settings
from django.template.loader import render_to_string
import pygsheets
import pandas as pd


gc = pygsheets.authorize(service_file='slot/creds.json')
# gc = pygsheets.authorize(service_file='creds.json')

# Create empty dataframe
df = pd.DataFrame()

# Create your views here.

def bookSlot(request):
    success = False
    bookingsSlot1d1 = 0
    bookingsSlot2d1 = 0
    bookingsSlot3d1 = 0
    bookingsSlot4d1 = 0
    bookingsSlot5d1 = 0
    bookingsSlot6d1 = 0
    bookingsSlot7d1 = 0
    bookingsSlot8d1 = 0
    bookingsSlot1d2 = 0
    bookingsSlot2d2 = 0
    bookingsSlot3d2 = 0
    bookingsSlot4d2 = 0
    bookingsSlot5d2 = 0
    bookingsSlot6d2 = 0
    bookingsSlot7d2 = 0
    bookingsSlot8d2 = 0
    sh = gc.open('PI R1 Mastersheet')
    wks = sh[0]
    w=wks.get_all_records()

    for i in range(len(w)):
        if(w[i]['slot'] == '17/1/2022 at 6:00 PM'):
            bookingsSlot1d1 += 1
        if(w[i]['slot'] == '17/1/2022 at 6:30 PM'):
            bookingsSlot1d1 += 1
        if(w[i]['slot'] == '17/1/2022 at 7:00 PM'):
            bookingsSlot1d1 += 1
        if(w[i]['slot'] == '17/1/2022 at 7:30 PM'):
            bookingsSlot1d1 += 1
        if(w[i]['slot'] == '17/1/2022 at 8:30 PM'):
            bookingsSlot1d1 += 1
        if(w[i]['slot'] == '17/1/2022 at 9:00 PM'):
            bookingsSlot1d1 += 1
        if(w[i]['slot'] == '17/1/2022 at 9:30 PM'):
            bookingsSlot1d1 += 1
        if(w[i]['slot'] == '17/1/2022 at 10:00 PM'):
            bookingsSlot1d1 += 1

        if(w[i]['slot'] == '18/1/2022 at 6:00 PM'):
            bookingsSlot1d2 += 1
        if(w[i]['slot'] == '18/1/2022 at 6:30 PM'):
            bookingsSlot1d2 += 1
        if(w[i]['slot'] == '18/1/2022 at 7:00 PM'):
            bookingsSlot1d2 += 1
        if(w[i]['slot'] == '18/1/2022 at 7:30 PM'):
            bookingsSlot1d2 += 1
        if(w[i]['slot'] == '18/1/2022 at 8:30 PM'):
            bookingsSlot1d2 += 1
        if(w[i]['slot'] == '18/1/2022 at 9:00 PM'):
            bookingsSlot1d2 += 1
        if(w[i]['slot'] == '18/1/2022 at 9:30 PM'):
            bookingsSlot1d2 += 1
        if(w[i]['slot'] == '18/1/2022 at 10:00 PM'):
            bookingsSlot1d2 += 1

    if request.method == 'POST':
        roll = request.POST.get('roll')
        slot = request.POST.get('slot')
        file = request.POST.get('file')
        entry=[]
        for i in range(len(w)):
            if(w[i]['roll'] == roll):
                entry = w[i]
                flag = entry['slot']
                print(flag)
                locationSlot = 'E' + str(i+2)
                locationFile = 'F' + str(i+2)
                # print(bookingsSlot1d1, entry['email'])
                wks.update_value(locationSlot, slot)
                wks.update_value(locationFile, file)
                entry['slot'] = slot
                entry['file'] = file
                break        
        
        if len(entry) == 10:
            if flag != 'FALSE':
                success = True
                body = render_to_string(
                    'email.html', {'name': entry['name'], 'dateTime': slot, 'file': file})
                email = EmailMessage(
                    'ECell Round 3 Selections | Meeting Link',
                    body,
                    settings.EMAIL_HOST_USER,
                    [entry['email'], 'sailokesh.gorantla@ecell-iitkgp.org', 'shubham.chaurasiya@ecell-iitkgp.org', 'vaibhav.mohite@ecell-iitkgp.org'],
                )
                email.fail_silently = False
                email.send()
            else:
                entry['slot'] = slot
                entry['file'] = file
                success = True
                body = render_to_string(
                    'email.html', {'name': entry['name'], 'dateTime': slot, 'file': file})
                email = EmailMessage(
                    'ECell Round 3 Selections | Meeting Link',
                    body,
                    settings.EMAIL_HOST_USER,
                    [entry['email'], 'sailokesh.gorantla@ecell-iitkgp.org', 'shubham.chaurasiya@ecell-iitkgp.org', 'vaibhav.mohite@ecell-iitkgp.org'],
                )
                email.fail_silently = False
                email.send()
        else:
            context = {'error': True}
            return render(request, 'index.html', context)

    context = {'success': success,
               'slot1d1': not (bookingsSlot1d1 < 6),
               'slot2d1': not (bookingsSlot2d1 < 6),
               'slot3d1': not (bookingsSlot3d1 < 6),
               'slot4d1': not (bookingsSlot4d1 < 6),
               'slot5d1': not (bookingsSlot5d1 < 6),
               'slot6d1': not (bookingsSlot6d1 < 6),
               'slot7d1': not (bookingsSlot7d1 < 6),
               'slot8d1': not (bookingsSlot8d1 < 6),
               'slot1d2': not (bookingsSlot1d2 < 6),
               'slot2d2': not (bookingsSlot2d2 < 6),
               'slot3d2': not (bookingsSlot3d2 < 6),
               'slot4d2': not (bookingsSlot4d2 < 6),
               'slot5d2': not (bookingsSlot5d2 < 6),
               'slot6d2': not (bookingsSlot6d2 < 6),
               'slot7d2': not (bookingsSlot7d2 < 6),
               'slot8d2': not (bookingsSlot8d2 < 6)}
    # df = pd.read_csv('slot/TaskRound.csv')#df = df.to_numpy()
    # for i in range(1, len(df)):
    #     name = df[i][0]
    #     roll = df[i][1]
    #     email = df[i][2]
    #     number = df[i][3]
    #     round2Dataset = Round2database(
    #         name=name, roll=roll, email=email, number=number)
    #     round2Dataset.save()
    return render(request, 'index.html', context)




# sh = gc.open('PI R1 Mastersheet')
# wks = sh[0]
# w=wks.get_all_records()
# wks.update_value('A100', 'djhf')
# wks.update_value('A101', 'file')