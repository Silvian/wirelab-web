# Generated by Django 3.2.8 on 2021-10-26 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='auto',
            field=models.BooleanField(default=False, help_text="Based on sunset times"),
        ),
        migrations.AddField(
            model_name='device',
            name='delay',
            field=models.PositiveIntegerField(blank=True, help_text='Auto delay time in minutes', null=True),
        ),
    ]
