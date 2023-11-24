from django.views.generic import TemplateView

from core.types import HtmxHttpRequest


class HomeView(TemplateView):
    template_name: str = "index_base.html"
    request: HtmxHttpRequest

    def get_template_names(self) -> list[str]:
        if self.request.htmx:
            return ["index_partial.html"]
        return [self.template_name]
