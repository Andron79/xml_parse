from django.shortcuts import render
from django.views.generic import TemplateView

from app.models import T_Procedures


class IndexView(TemplateView):
    template_name = 'dashboard.html'
    model = T_Procedures
