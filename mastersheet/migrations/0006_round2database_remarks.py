# Generated by Django 3.2.1 on 2022-01-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mastersheet', '0005_round2database_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='round2database',
            name='remarks',
            field=models.CharField(blank=True, default='None', max_length=50),
        ),
    ]
