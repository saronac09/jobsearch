# Generated by Django 4.0.5 on 2022-09-23 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_employeeform'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='employess',
            field=models.TextField(default='Null'),
        ),
        migrations.AddField(
            model_name='register',
            name='salary',
            field=models.TextField(default='Null'),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
