# Generated by Django 3.2.7 on 2021-09-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0005_deposit'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email_id', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('amount', models.IntegerField(verbose_name='Amount (₹)')),
                ('action', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email_id', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('amount', models.IntegerField(verbose_name='Amount (₹)')),
                ('receiver', models.CharField(max_length=30)),
            ],
        ),
    ]
