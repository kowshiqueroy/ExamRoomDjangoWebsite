# Generated by Django 2.2 on 2021-03-29 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('student_ID', models.IntegerField(default=0)),
                ('email_address', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
