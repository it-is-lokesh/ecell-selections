from django.shortcuts import render
from slot.models import database
from mastersheet.models import Round2database
from django.core.mail import EmailMessage
from slot.forms import slotForm
from django.conf import settings
from django.template.loader import render_to_string
# import pandas as pd

# Create your views here.

def bookSlot(request):
    success = False
    bookingsSlot1d1 = database.objects.filter(slot='17/1/2022 at 6:00 PM')
    bookingsSlot2d1 = database.objects.filter(slot='17/1/2022 at 6:30 PM')
    bookingsSlot3d1 = database.objects.filter(slot='17/1/2022 at 7:00 PM')
    bookingsSlot4d1 = database.objects.filter(slot='17/1/2022 at 7:30 PM')
    bookingsSlot5d1 = database.objects.filter(slot='17/1/2022 at 8:30 PM')
    bookingsSlot6d1 = database.objects.filter(slot='17/1/2022 at 9:00 PM')
    bookingsSlot7d1 = database.objects.filter(slot='17/1/2022 at 9:30 PM')
    bookingsSlot8d1 = database.objects.filter(slot='17/1/2022 at 10:00 PM')
    bookingsSlot1d2 = database.objects.filter(slot='18/1/2022 at 6:00 PM')
    bookingsSlot2d2 = database.objects.filter(slot='18/1/2022 at 6:30 PM')
    bookingsSlot3d2 = database.objects.filter(slot='18/1/2022 at 7:00 PM')
    bookingsSlot4d2 = database.objects.filter(slot='18/1/2022 at 7:30 PM')
    bookingsSlot5d2 = database.objects.filter(slot='18/1/2022 at 8:30 PM')
    bookingsSlot6d2 = database.objects.filter(slot='18/1/2022 at 9:00 PM')
    bookingsSlot7d2 = database.objects.filter(slot='18/1/2022 at 9:30 PM')
    bookingsSlot8d2 = database.objects.filter(slot='18/1/2022 at 10:00 PM')
    if request.method == 'POST':
        roll = request.POST.get('roll')
        slot = request.POST.get('slot')
        file = request.POST.get('file')
        Round2database.objects.filter(roll=roll).update(slot=slot, file=file)
        temp1 = Round2database.objects.filter(roll=roll)
        temp2 = database.objects.filter(roll=roll)
        if len(temp1) == 1:
            if len(temp2) == 0:
                bookingDetails = database(name=temp1[0].name, roll=roll, slot=slot, file=file)
                bookingDetails.save()
                success = True
                body = render_to_string(
                    'email.html', {'name': temp1[0].name, 'dateTime': slot, 'file': file})
                email = EmailMessage(
                    'ECell Round 3 Selections | Meeting Link',
                    body,
                    settings.EMAIL_HOST_USER,
                    [temp1[0].email, 'sailokesh.gorantla@ecell-iitkgp.org'],
                )
                email.fail_silently = False
                email.send()
            elif len(temp2) == 1:
                database.objects.filter(roll=roll).update(slot=slot, file=file)
                success = True
                body = render_to_string(
                    'email.html', {'name': temp1[0].name, 'dateTime': slot, 'file': file})
                email = EmailMessage(
                    'ECell Round 3 Selections | Meeting Rescheduled',
                    body,
                    settings.EMAIL_HOST_USER,
                    [temp1[0].email, 'sailokesh.gorantla@ecell-iitkgp.org'],
                )
                email.fail_silently = False
                email.send()
        elif len(temp1)==0:
            context = {'error': True}
            return render(request, 'index.html', context)

    context = {'success': success,
               'slot1d1': not (len(bookingsSlot1d1) < 6),
               'slot2d1': not (len(bookingsSlot2d1) < 6),
               'slot3d1': not (len(bookingsSlot3d1) < 6),
               'slot4d1': not (len(bookingsSlot4d1) < 6),
               'slot5d1': not (len(bookingsSlot5d1) < 6),
               'slot6d1': not (len(bookingsSlot6d1) < 6),
               'slot7d1': not (len(bookingsSlot7d1) < 6),
               'slot8d1': not (len(bookingsSlot8d1) < 6),
               'slot1d2': not (len(bookingsSlot1d2) < 6),
               'slot2d2': not (len(bookingsSlot2d2) < 6),
               'slot3d2': not (len(bookingsSlot3d2) < 6),
               'slot4d2': not (len(bookingsSlot4d2) < 6),
               'slot5d2': not (len(bookingsSlot5d2) < 6),
               'slot6d2': not (len(bookingsSlot6d2) < 6),
               'slot7d2': not (len(bookingsSlot7d2) < 6),
               'slot8d2': not (len(bookingsSlot8d2) < 6)}
    # df = pd.read_csv('slot/TaskRound.csv')
    # df = df.to_numpy()
    # for i in range(1, len(df)):
    #     name = df[i][0]
    #     roll = df[i][1]
    #     email = df[i][2]
    #     number = df[i][3]
    #     round2Dataset = Round2database(
    #         name=name, roll=roll, email=email, number=number)
    #     round2Dataset.save()
    return render(request, 'index.html', context)

