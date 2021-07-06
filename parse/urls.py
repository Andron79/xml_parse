from django.contrib import admin
from django.urls import path

from app.views import T_ProceduresView, ParserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', T_ProceduresView.as_view()),
    path('parse/', ParserView.as_view())
]
