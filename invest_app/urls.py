from invest_app.views import (
    DeleteStock,
    EditStock,
    SectorView,
    StockD,
    StockView,
    SectorD,
    EditSector,
    DeleteSector,
    stock_page,
    StockPortfolioView,
    add_stock_page,
)
from .routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter(trailing_slash=False)

router.register(r"sector", SectorView, basename="sector")
router.register(r"stock", StockView, basename="stock")
router.register(r"stock-portfolio", StockPortfolioView, basename="stock_portfolio")
#

urlpatterns = [
    path("", include(router.urls)),
    # Templating purpose
    path("add-sector/", SectorD, name="add_sector"),
    path("edit-sector/<int:pk>/", EditSector, name="edit_sector"),
    path("delete-sector/<int:pk>/", DeleteSector, name="delete_sector"),
    path("add-stock/", StockD, name="add_stock"),
    path("edit-stock/<int:pk>/", EditStock, name="edit_stock"),
    path("delete-stock/<int:pk>/", DeleteStock, name="delete_stock"),
    path("stocks/", stock_page, name="stocks"),
    path("add-stocks/", add_stock_page, name="add_stocks_details"),
]
