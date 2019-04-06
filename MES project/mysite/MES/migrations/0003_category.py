# Generated by Django 2.1.5 on 2019-01-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MES', '0002_auto_20190118_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ProductID', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=6)),
                ('Description', models.CharField(max_length=255)),
                ('Quantity', models.IntegerField()),
            ],
        ),
    ]