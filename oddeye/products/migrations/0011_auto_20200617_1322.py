# Generated by Django 3.0.6 on 2020-06-17 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_productsembedding1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductsEmbedding',
            new_name='ProductsEmbedding3',
        ),
        migrations.AlterModelOptions(
            name='productsembedding3',
            options={'verbose_name': '상품 임베딩3', 'verbose_name_plural': '상품 임베딩3'},
        ),
        migrations.AlterModelTable(
            name='productsembedding3',
            table='products_embedding3',
        ),
    ]
