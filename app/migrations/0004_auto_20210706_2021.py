# Generated by Django 3.2.5 on 2021-07-06 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_t_procedures_curator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_procedures',
            name='purchaseNumber',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='t_procedures',
            name='regNum',
            field=models.CharField(max_length=100),
        ),
    ]
