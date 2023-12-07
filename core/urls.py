from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

from core.routers import InternalAPIRouter
from users.urls import router as user_router

internal_api_router = InternalAPIRouter()
internal_api_router.extend(user_router)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(internal_api_router.urls)),
    path("api/", include("users.urls")),
]

if settings.CURRENT_ENVIRONMENT == "DEV":
    urlpatterns += [
        path("api/docs/", SpectacularAPIView.as_view(), name="api-docs"),
        path(
            "api/docs/redoc-ui",
            SpectacularRedocView.as_view(url_name="api-docs"),
        ),
    ]
