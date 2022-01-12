from tempfile import template
from django.db.models.expressions import F
from django.shortcuts import render
from django.views.generic.edit import CreateView
from invest_app.models import Stock,Transaction,Sector
# Create your views here.

class SectorView(CreateView):
    model = Sector
    fields = ['sector_name',]
    template =  "add_sector.html"

