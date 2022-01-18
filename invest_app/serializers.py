from django.contrib.auth import models
from django.db.models import fields
from numpy import mod
from rest_framework import serializers
from invest_app.models import Stock, Transaction, Sector


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ["id", "sector_name"]


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ["user", "sector", "stock_name", "stock_symbol", "isin", "created_at"]


class StockInvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "user",
            "stock",
            "market_choice",
            "qauntity",
            "invested_amount",
            "last_profit",
            "last_closed",
            "interest_rate",
            "invested_date",
            "plan_of_investment_date",
        ]
