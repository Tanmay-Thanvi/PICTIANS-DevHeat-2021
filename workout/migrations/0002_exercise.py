# Generated by Django 3.2.8 on 2021-11-14 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
            ],
        ),
    ]