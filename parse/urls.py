from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app.views import T_ProceduresView, ParserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', T_ProceduresView.as_view()),
    path('parse/', ParserView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT
                          )
