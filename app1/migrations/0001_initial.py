# Generated by Django 3.0.4 on 2021-04-06 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=20)),
                ('tage', models.IntegerField()),
                ('tgender', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('sage', models.IntegerField()),
                ('sgender', models.CharField(max_length=2)),
                ('s_t', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Teacher')),
            ],
        ),
    ]
