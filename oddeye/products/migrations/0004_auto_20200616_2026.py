# Generated by Django 3.0.6 on 2020-06-16 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productsembedding1_productsembedding2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productsembedding1',
            options={'verbose_name': '상품 임베딩1', 'verbose_name_plural': '상품 임베딩1'},
        ),
        migrations.AlterModelOptions(
            name='productsembedding2',
            options={'verbose_name': '상품 임베딩2', 'verbose_name_plural': '상품 임베딩2'},
        ),
    ]
