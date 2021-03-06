# Generated by Django 3.2.8 on 2022-01-11 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("invest_app", "0005_transaction_market_choice"),
    ]

    operations = [
        migrations.AddField(
            model_name="stock",
            name="user",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="auth.user"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="stock",
            name="sector",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="invest_app.sector"
            ),
        ),
    ]
