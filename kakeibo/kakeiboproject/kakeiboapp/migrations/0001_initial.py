# Generated by Django 4.1 on 2024-07-08 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Koumoku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Koumoku_name', models.CharField(max_length=30, unique=True)),
                ('yosan', models.IntegerField()),
            ],
            options={
                'db_table': 'koumoku',
            },
        ),
        migrations.CreateModel(
            name='Rireki',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('fee', models.IntegerField()),
                ('koumoku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kakeiboapp.koumoku')),
            ],
            options={
                'db_table': 'Rireki',
            },
        ),
    ]
