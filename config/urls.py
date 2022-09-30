from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('core.urls')),
    path("swagger/main", views.schema_view.with_ui("swagger", cache_timeout=0)),
    path("swagger/yaml", views.schema_view.without_ui(cache_timeout=0)),
    path("swagger/json", views.schema_view.without_ui(cache_timeout=0)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)