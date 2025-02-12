from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import update_student


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('database/',views.database, name="database"),
    path('view/',views.view, name="view"),
     path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
     path('update-student/<int:student_id>/', update_student, name="update_student"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])