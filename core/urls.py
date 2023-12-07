from django.contrib import admin
from django.urls import include, path

from core.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("wods/", include("wods.urls", namespace="wods")),
]
