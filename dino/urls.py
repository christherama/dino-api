from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="admin/login.html")),
    path('accounts/logout/', auth_views.LogoutView.as_view()),
    path("api/", include("api.urls", namespace="api")),
]
