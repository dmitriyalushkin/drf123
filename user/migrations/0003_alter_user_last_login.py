# Generated by Django 4.2.9 on 2024-02-04 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата последнего входа'),
        ),
    ]
