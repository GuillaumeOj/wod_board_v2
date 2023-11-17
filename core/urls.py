from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("users.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
