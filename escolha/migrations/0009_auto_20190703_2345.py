# Generated by Django 2.2.3 on 2019-07-03 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escolha', '0008_auto_20190703_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='codigo_banco',
            field=models.CharField(max_length=200),
        ),
    ]