# Generated by Django 3.2.3 on 2021-06-14 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0008_auto_20210613_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmedticket',
            name='date',
            field=models.DateField(auto_now_add=True, default='2020-06-14'),
            preserve_default=False,
        ),
    ]
