# Generated by Django 3.2.8 on 2022-01-13 14:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invest_app', '0007_alter_transaction_invested_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='plan_of_investment_date',
            field=models.DateField(default=django.utils.timezone.localtime),
        ),
    ]
