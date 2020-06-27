# Generated by Django 3.0.6 on 2020-06-16 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('styles', '0008_auto_20200616_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Star_embedding1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('star_embedding', models.CharField(max_length=2000)),
            ],
            options={
                'verbose_name': '스타 임베딩1',
                'verbose_name_plural': '스타 임베딩1',
                'db_table': 'star_embedding1',
            },
        ),
        migrations.CreateModel(
            name='Star_embedding2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('star_embedding', models.CharField(max_length=2000)),
            ],
            options={
                'verbose_name': '스타 임베딩2',
                'verbose_name_plural': '스타 임베딩2',
                'db_table': 'star_embedding2',
            },
        ),
    ]