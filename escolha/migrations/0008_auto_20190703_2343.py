# Generated by Django 2.2.3 on 2019-07-03 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escolha', '0007_foto_codigo_banco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='comentario',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
