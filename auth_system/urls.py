from django.urls import path
from auth_system import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path("login/", views.login_user, name = "login"),
    path("log_out/", views.logout_view, name="log-out")
]