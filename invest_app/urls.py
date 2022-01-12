from django.urls import path
from django.views.generic import TemplateView

from invest_app.views import SectorView

urlpatterns = [path("add-sector/", SectorView.as_view(), name="add_sector")]

