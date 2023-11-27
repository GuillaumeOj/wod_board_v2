from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from core.types import HtmxHttpRequest
from wods.forms import WodForm
from wods.models import Wod


class WodListView(LoginRequiredMixin, ListView):
    model = Wod
    context_object_name = "wods"
    template_name: str = "wods/list_base.html"
    request: HtmxHttpRequest

    def get_template_names(self) -> list[str]:
        if self.request.htmx:
            return ["wods/list_partial.html"]
        return [self.template_name]

    def get_queryset(self):
        return Wod.objects.filter(user=self.request.user)


class WodCreateView(LoginRequiredMixin, CreateView):
    model = Wod
    form_class = WodForm
    template_name: str = "wods/create_base.html"
    success_url = reverse_lazy("home")
    request: HtmxHttpRequest

    def get_template_names(self) -> list[str]:
        if self.request.htmx:
            return ["wods/create_partial.html"]
        return [self.template_name]

    def post(self, request: HtmxHttpRequest, *args, **kwargs) -> HttpResponse:
        self.object = None
        form = self.get_form()
        if not form.is_valid():
            return self.form_invalid(form)

        wod = form.save(commit=False)
        wod.user = request.user
        wod.save()

        self.object = wod

        return HttpResponseRedirect(self.get_success_url())
