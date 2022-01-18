from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Goal, Sector, Stock, Transaction
from django.utils.encoding import force_text
from django.db.models import Sum


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("title", "currency_format", "term", "create", "last_update")
    change_list_template = "change_list.html"

    def currency_format(self, obj):
        """
        Similar to 'django.contrib.humanize.intcomma', but with dots.
        """
        val_text = force_text(obj.target_amount)
        try:
            val_new = int(float(val_text))
            val_new = f"{val_new:,}"
        except ValueError as e:
            return ""

        # val_new = val_new.replace(',', ',')
        return val_new

    def get_total(self):
        total = Goal.objects.all().aggregate(tot=Sum("target_amount"))
        return total

    def changelist_view(self, request, extra_context=None):
        my_context = {"total": self.get_total().get("tot")}
        return super(GoalAdmin, self).changelist_view(request, extra_context=my_context)


admin.site.register(Sector)


@admin.register(Transaction)
class StockTransactionAdmin(admin.ModelAdmin):
    list_display = [
        "stock",
        "invested_amount",
        "qauntity",
        "interest_rate",
        "monthly_interest",
        "invested_date",
    ]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ["User_Name", "stock_symbol", "stock_name", "created_at"]

    def User_Name(self, obj):
        return obj.user.get_full_name()
