from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.login_view, name="login"), 
    path("home/", views.home, name="home"), 
    path("database/", views.database, name="database"),
    path("view/", views.view, name="view"),
    path("attendance/", views.attendance, name="attendance"),
    path("delete-student/<int:student_id>/", views.delete_student, name="delete_student"),
    path("update-student/<int:student_id>/", views.update_student, name="update_student"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"), 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
