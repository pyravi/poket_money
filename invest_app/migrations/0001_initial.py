# Generated by Django 3.2.8 on 2022-01-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Goal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(help_text="Goal Name", max_length=150)),
                ("target_amount", models.FloatField(blank=True)),
                (
                    "term",
                    models.IntegerField(
                        choices=[(1, "Long Term"), (2, "Short Term"), (3, "Mid Term")],
                        default=1,
                    ),
                ),
                ("create", models.DateTimeField(auto_now=True, verbose_name="Date")),
                ("last_update", models.DateTimeField(verbose_name="Till Date")),
            ],
        ),
        migrations.CreateModel(
            name="Stock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stock_name", models.CharField(max_length=150)),
                ("stock_symbol", models.CharField(max_length=100)),
                ("invested_amount", models.FloatField()),
                ("qauntity", models.IntegerField()),
                ("interest_rate", models.FloatField()),
                ("actual_amount", models.FloatField()),
                ("expected_amount", models.FloatField()),
                ("invested_date", models.DateField(auto_now_add=True)),
                ("plan_of_investment_date", models.DateField()),
            ],
        ),
    ]
