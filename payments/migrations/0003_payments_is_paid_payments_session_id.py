# Generated by Django 5.0.1 on 2024-01-31 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_payments_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='статус оплаты'),
        ),
        migrations.AddField(
            model_name='payments',
            name='session_id',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='id сессии'),
        ),
    ]
