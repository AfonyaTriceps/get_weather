# Generated by Django 2.2.19 on 2023-04-12 00:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('weather', '0002_auto_20230412_0350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ('-id',)},
        ),
    ]
