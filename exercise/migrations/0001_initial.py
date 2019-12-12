# Generated by Django 3.0 on 2019-12-12 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('habitat', models.CharField(choices=[('TRO', 'Tropical'), ('DES', 'Desert'), ('ARC', 'Arctic'), ('RFR', 'Rainforest'), ('MOD', 'Moderate')], default='MOD', max_length=3)),
            ],
        ),
    ]
