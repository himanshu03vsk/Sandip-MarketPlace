from django.urls import path
from authenticate import views

urlpatterns = [
    path("dashboard", views.user_dashboard, name="user_dashboard"),
    path("login", views.user_login, name="user_login"),    
    path("register", views.user_reg, name="user_registration"),
    path("logout", views.logout_user, name="logout"),

]