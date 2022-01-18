from django.db import models
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils.timezone import localtime

# Create your models here.


class Sector(models.Model):
    sector_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(default=localtime)

    def __str__(self):
        return self.sector_name

    class Meta:
        verbose_name_plural = "Sectors"


class Stock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=150)
    stock_symbol = models.CharField(max_length=100)
    isin = models.CharField(
        max_length=15,
        help_text=" International Securities Identification Number",
        blank=True,
    )
    created_at = models.DateTimeField(default=localtime)

    def __str__(self):
        return self.stock_name

    class Meta:
        verbose_name_plural = "Stocks"


class Transaction(models.Model):
    """
    Model of Stock plan and amount
    """

    market = ((0, "Sell"), (1, "Buy"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    market_choice = models.IntegerField(choices=market, default=1)
    qauntity = models.IntegerField()
    invested_amount = models.FloatField()
    last_profit = models.FloatField()
    last_closed = models.FloatField()
    interest_rate = models.FloatField()
    invested_date = models.DateTimeField(default=localtime)
    plan_of_investment_date = models.DateField(default=localtime)

    def __str__(self):
        return f"{self.stock_name} invested money : {self.invested_amount} and current amount: {self.actual_amount}"

    @property
    def monthly_interest(self):
        if not self.expected_amount:
            return self.expected_amount * self.interest_rate
        return self.invested_amount * self.interest_rate


class Goal(models.Model):
    duration = ((1, "Long Term"), (2, "Short Term"), (3, "Mid Term"))
    title = models.CharField(max_length=150, help_text="Goal Name", null=False)
    target_amount = models.FloatField(blank=True)
    term = models.IntegerField(choices=duration, default=1)
    create = models.DateTimeField(_("Date"), auto_now=True)
    last_update = models.DateTimeField(
        _("Till Date"), auto_now=False, auto_now_add=False
    )

    def __str__(self) -> str:
        return self.title
