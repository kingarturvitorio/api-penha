# Generated by Django 5.1 on 2024-08-19 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=14)),
                ('tplogradouro', models.CharField(max_length=100)),
                ('nres', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=30)),
                ('uf', models.CharField(max_length=2)),
                ('dtnasc', models.DateField(blank=True, null=True)),
                ('dtcadastro', models.DateField(blank=True, null=True)),
                ('processo', models.CharField(max_length=30)),
                ('latres', models.FloatField()),
                ('longres', models.FloatField()),
                ('observacoes', models.CharField(max_length=30)),
                ('status', models.IntegerField()),
            ],
        ),
    ]