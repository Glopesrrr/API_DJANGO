# Generated by Django 4.1.7 on 2023-06-21 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=100)),
                ('dataNascimento', models.DateField()),
            ],
        ),
    ]