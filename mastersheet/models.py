from django.db import models

# Create your models here.

class Round2database(models.Model): 
    name = models.CharField(max_length=20, default=False, blank=True)
    roll = models.CharField(max_length=9, default=False, blank=True)
    number = models.CharField(max_length=14, default="Null", blank=False)
    email = models.EmailField(default=False, blank=False)
    slot = models.CharField(max_length=20, default="", blank=True)
    file = models.URLField()
    interviewer = models.CharField(max_length=30, default="", blank=True)
    remarks = models.CharField(max_length=50, blank=True, default="None")
    taken = models.CharField(max_length=10, blank=True, default="No")
    selected = models.CharField(max_length=10, blank=True, default="No")

    def __str__(self):
        return self.roll