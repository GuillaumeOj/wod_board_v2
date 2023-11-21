from django.urls import path

from wods.views import WodCreateView, WodListView

app_name = "wods"
urlpatterns = [
    path("", WodListView.as_view(), name="list"),
    path("create/", WodCreateView.as_view(), name="create"),
]
