from django.urls import path
from .views import home, about, contact
from django.contrib.auth import views as auth_views

app_name = "home"

urlpatterns = [
    path("", home, name="home_view"),
    path("contact.html", contact, name="contact_view"),
    path("about.html", about, name="about_view"),
    path("login/", auth_views.LoginView.as_view(template_name="home/login.html"), name="login")
]
