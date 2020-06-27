# Generated by Django 3.0.6 on 2020-06-16 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productsembedding'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsEmbedding2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_embedding', models.CharField(max_length=2000, verbose_name='상품 임베딩값')),
                ('product_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Products', verbose_name='상품 ID')),
            ],
            options={
                'verbose_name': '상품 임베딩',
                'verbose_name_plural': '상품 임베딩',
                'db_table': 'products_embedding2',
            },
        ),
        migrations.CreateModel(
            name='ProductsEmbedding1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_embedding', models.CharField(max_length=2000, verbose_name='상품 임베딩값')),
                ('product_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Products', verbose_name='상품 ID')),
            ],
            options={
                'verbose_name': '상품 임베딩',
                'verbose_name_plural': '상품 임베딩',
                'db_table': 'products_embedding1',
            },
        ),
    ]
