from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('database/',views.database, name="database"),
    path('view/',views.view, name="view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])