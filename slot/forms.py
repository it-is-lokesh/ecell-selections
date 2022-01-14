from django import forms
from slot.models import database

class slotForm(forms.Form):
    CHOICES=(('slot1','Slot 1'),
         ('slot2','Slot 2'),
         ('slot3','Slot 3'),
         ('slot4','Slot 4'),
         ('slot5','Slot 5'),
         ('slot6','Slot 6'),
         ('slot7','Slot 7'),
         ('slot8','Slot 8'))
    slot = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = database
        fields = "__all__"

