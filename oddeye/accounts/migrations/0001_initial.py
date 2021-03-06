# Generated by Django 3.0.6 on 2020-06-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OddeyeUsers',
            fields=[
                ('no', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='NO')),
                ('id', models.CharField(max_length=15, verbose_name='아이디')),
                ('password', models.CharField(max_length=15, verbose_name='패스워드')),
                ('following', models.CharField(max_length=1000, verbose_name='팔로잉')),
                ('wish_list', models.CharField(max_length=1000, verbose_name='위시리스트')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
            ],
            options={
                'verbose_name': 'oddeye_users',
                'verbose_name_plural': 'oddeye_users',
                'db_table': 'oddeye_users',
            },
        ),
    ]
