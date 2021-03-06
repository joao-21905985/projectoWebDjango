# Generated by Django 3.2.3 on 2021-06-04 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('apelido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('telemovel', models.CharField(blank=True, max_length=9)),
                ('birth', models.DateField()),
                ('criado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
