# Generated by Django 2.0.5 on 2019-07-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escolha', '0005_auto_20190702_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='static/escolha/images/'),
        ),
    ]