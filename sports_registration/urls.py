from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),  # URL для административной панели
    path('', RedirectView.as_view(url='athletes/countries/', permanent=False)),  # Перенаправление на список стран
    path('athletes/', include('athletes.urls')),  # Включение маршрутов приложения athletes
]