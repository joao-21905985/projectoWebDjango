from django.urls import path

from . import views
app_name = "users"
urlpatterns = [
    path('userindex', views.index_view, name="index"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout")
]