# Generated by Django 2.2.3 on 2019-07-02 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escolha', '0004_auto_20190702_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]