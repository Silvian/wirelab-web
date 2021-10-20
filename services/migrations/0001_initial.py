# Generated by Django 3.2.8 on 2021-10-12 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebhookConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Webhook configuration', max_length=50)),
                ('api_key', models.CharField(default='secret key', max_length=255)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]