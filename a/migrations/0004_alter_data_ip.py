# Generated by Django 3.2.8 on 2021-12-14 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0003_rename_continent_data_continente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='ip',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
