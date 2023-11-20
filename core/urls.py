from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from core.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("wods/", include("wods.urls", namespace="wods")),
]

if settings.CURRENT_ENVIRONMENT == "DEV":
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
        path("__debug__/", include("debug_toolbar.urls")),
    ]
