# Generated by Django 3.2.5 on 2021-07-02 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_procedures',
            name='curator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.t_users'),
        ),
    ]
