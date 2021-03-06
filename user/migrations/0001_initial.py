# Generated by Django 3.1 on 2020-08-28 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=129)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('true_name', models.CharField(blank=True, max_length=32, null=True)),
                ('sex', models.CharField(choices=[('man', 'man'), ('woman', 'woman'), ('secret', 'secret')], default='secret', max_length=6)),
                ('birthday', models.DateTimeField(blank=True, null=True)),
                ('tel', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('mail', models.EmailField(blank=True, max_length=64, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('head', models.ImageField(blank=True, max_length=16, null=True, upload_to='')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
