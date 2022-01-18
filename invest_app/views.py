from datetime import datetime
from django.contrib import messages
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from invest_app.models import Stock, Transaction, Sector
from rest_framework import mixins
from rest_framework import generics
from invest_app.serializers import (
    SectorSerializer,
    StockInvestmentSerializer,
    StockSerializer,
)
from rest_framework import (
    filters,
    mixins,
    permissions,
    response,
    serializers,
    status,
    viewsets,
)
from django.db.models import Q
from django.core.paginator import Paginator
from user_profile.models import UserProfile


def SectorD(request):
    """
    List all Sectors, or create a new sector
    """
    context = {"sources": Sector.objects.all()}
    if request.method == "POST":
        sector = request.POST.get("sector_name")
        sources = Sector()
        sources.sector_name = sector
        sources.created_at = datetime.now()
        sources.save()
        messages.info(request, f"Sector is Added {sources}")
        return redirect("add_sector")

    return render(request, "invest_app/add_sector.html", context)


def EditSector(request, pk):
    """
    List all Sectors, or create a new sector
    """
    if request.method == "POST":
        sector = request.POST.get("sector_name")
        sources = Sector.objects.get(id=pk)
        sources.sector_name = sector
        sources.created_at = datetime.now()
        sources.save()
        messages.info(request, "Sector updated")
        return redirect("add_sector")
    context = {"sources": Sector.objects.all(), "values": Sector.objects.get(id=pk)}
    return render(request, "invest_app/edit_sector.html", context)


def DeleteSector(request, pk):
    """
    List all Sectors, or create a new sector
    """
    if request.method == "GET":
        sources = Sector.objects.get(id=pk)
        sources.delete()
        messages.info(request, "Sector deleted")
        return redirect("add_sector")


def StockD(request):
    """
    List all Sectors, or create a new sector
    """
    context = {"sources": Stock.objects.all(), "sectors": Sector.objects.all()}

    if request.method == "POST":
        stock = request.POST.get("stock_name")
        sector_value = request.POST.get("sector")
        stock_symbol = request.POST.get("stock_symbol")
        isin = request.POST.get("isin")
        created_at = request.POST.get("created_at")
        sources = Stock()
        sources.user = request.user
        sources.sector = Sector.objects.get(id=sector_value)
        sources.stock_name = stock
        sources.stock_symbol = stock_symbol
        sources.isin = isin
        sources.created_at = created_at if created_at else datetime.now()
        sources.save()
        messages.info(request, f"Sector is Added {sources}")
        return redirect("add_stock")

    return render(request, "invest_app/add_stock.html", context)


def EditStock(request, pk):
    """
    List all Sectors, or create a new sector
    """
    if request.method == "POST":
        stock = request.POST.get("stock_name")
        sector_value = request.POST.get("sector")
        stock_symbol = request.POST.get("stock_symbol")
        isin = request.POST.get("isin")
        created_at = request.POST.get("created_at")
        sources = Stock.objects.get(pk=pk)
        sources.user = request.user
        sources.sector = Sector.objects.get(id=sector_value)
        sources.stock_name = stock
        sources.stock_symbol = stock_symbol
        sources.isin = isin
        sources.created_at = created_at if created_at else datetime.now()
        sources.save()
        messages.info(request, "Stock updated")
        return redirect("add_stock")
    context = {
        "sources": Stock.objects.all(),
        "values": Stock.objects.get(id=pk),
        "sectors": Sector.objects.all(),
    }
    return render(request, "invest_app/edit_stock.html", context)


def DeleteStock(request, pk):
    """
    List all Sectors, or create a new sector
    """
    if request.method == "GET":
        sources = Stock.objects.get(id=pk)
        sources.delete()
        messages.info(request, "Stock deleted")
        return redirect("add_stock")


def stock_page(request):

    filter_context = {}
    base_url = f""
    date_from_html = ""
    date_to_html = ""

    incomes = Transaction.objects.filter(user=request.user).order_by("-invested_date")

    try:

        if "date_from" in request.GET and request.GET["date_from"] != "":
            date_from = datetime.strptime(request.GET["date_from"], "%Y-%m-%d")
            filter_context["date_from"] = request.GET["date_from"]
            date_from_html = request.GET["date_from"]

            if "date_to" in request.GET and request.GET["created_at"] != "":

                date_to = datetime.strptime(request.GET["date_to"], "%Y-%m-%d")
                filter_context["date_to"] = request.GET["date_to"]
                date_to_html = request.GET["date_to"]
                incomes = incomes.filter(
                    Q(date__gte=date_from) & Q(date__lte=date_to)
                ).order_by("-date")

            else:
                incomes = Transaction.filter(date__gte=date_from).order_by(
                    "-invested_date"
                )

        elif "date_to" in request.GET and request.GET["created_at"] != "":

            date_to_html = request.GET["created_at"]
            date_to = datetime.strptime(request.GET["date_to"], "%Y-%m-%d")
            filter_context["date_from"] = request.GET["date_to"]
            incomes = incomes.filter(date__lte=date_to).order_by("-invested_date")

    except:
        messages.error(request, "Something went wrong")
        return redirect("stocks")

    base_url = f"?date_from={date_from_html}&date_to={date_to_html}&"
    paginator = Paginator(incomes, 5)
    page_number = request.GET.get("page")
    page_incomes = Paginator.get_page(paginator, page_number)

    if UserProfile.objects.filter(user=request.user).exists():
        currency = UserProfile.objects.get(user=request.user).currency
    else:
        currency = "INR - Indian Rupee"

    return render(
        request,
        "invest_app/stocks.html",
        {
            "currency": currency,
            "page_incomes": page_incomes,
            "incomes": incomes,
            "filter_context": filter_context,
            "base_url": base_url,
        },
    )


def add_stock_page(request):
    context = {"sources": Stock.objects.all()}
    if request.method == "POST":
        stock = request.POST.get("stock")
        market_choice = request.POST.get("market_choice")
        qauntity = request.POST.get("qauntity")
        invested_amount = request.POST.get("invested_amount")
        last_profit = request.POST.get("last_profit")
        last_closed = request.POST.get("last_closed")
        interest_rate = request.POST.get("interest_rate")
        plan_of_investment_date = request.POST.get("plan_of_investment_date")
        stock_details = Transaction()
        stock_details.stock = Stock.objects.get(stock_name=stock)
        stock_details.user = request.user
        stock_details.market_choice = market_choice
        stock_details.qauntity = qauntity
        stock_details.interest_rate = interest_rate
        stock_details.last_closed = last_closed
        stock_details.last_profit = last_profit
        stock_details.invested_amount = invested_amount
        stock_details.invested_date = datetime.now()
        stock_details.plan_of_investment_date = plan_of_investment_date

        stock_details.save()

    return render(request, "invest_app/stocktranscation.html", context)


"""'

API for REST Framework

"""


class SectorView(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        permit = self.get_object()
        serializer = self.get_serializer(data=request.data, instance=permit)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return response.Response(serializer.data)


class StockView(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        permit = self.get_object()
        serializer = self.get_serializer(data=request.data, instance=permit)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return response.Response(serializer.data)


class StockPortfolioView(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = Transaction.objects.all()
    serializer_class = StockInvestmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        permit = self.get_object()
        serializer = self.get_serializer(data=request.data, instance=permit)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return response.Response(serializer.data)
