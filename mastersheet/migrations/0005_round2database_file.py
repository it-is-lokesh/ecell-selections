# Generated by Django 3.2.1 on 2022-01-11 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mastersheet', '0004_round2database_slot'),
    ]

    operations = [
        migrations.AddField(
            model_name='round2database',
            name='file',
            field=models.URLField(default=False),
            preserve_default=False,
        ),
    ]
