from django.contrib import admin
from django.urls import path

from app.views import IndexView, T_ProceduresView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', T_ProceduresView.as_view())
]