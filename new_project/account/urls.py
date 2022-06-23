from django.urls import path
from.views import register, login
from django.contrib.auth import views as auth_views

app_name = "account"


urlpatterns = [
    path("register/", register, name="register_view"),
    path("login/", auth_views.LoginView.as_view(template_name="account/login.html"), name="login_view"),
    path("logout/", auth_views.LogoutView.as_view(template_name="account/logout.html"), name="logout_view")

]
