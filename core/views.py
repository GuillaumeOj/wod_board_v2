from typing import Any

from django.views.generic import TemplateView


class WodBoardView(TemplateView):
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data["user"] = self.request.user

        return context_data


class HomeView(WodBoardView, TemplateView):
    template_name: str = "index_base.html"
