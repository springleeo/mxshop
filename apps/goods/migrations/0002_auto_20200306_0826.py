# Generated by Django 2.2.8 on 2020-03-06 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_sn',
            field=models.CharField(default='', max_length=50, verbose_name='商品货号'),
        ),
    ]
