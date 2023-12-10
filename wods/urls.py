from rest_framework.routers import SimpleRouter

from wods.views import WodViewset

app_name = "wods"

wod_router = SimpleRouter()
wod_router.register(r"", WodViewset)

urlpatterns = wod_router.urls
