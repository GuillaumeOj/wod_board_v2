from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from wods.forms import WodForm
from wods.models import Wod


class WodListView(LoginRequiredMixin, ListView):
    model = Wod
    context_object_name = "wods"
    template_name = "wods/list.html"

    def get_queryset(self):
        return Wod.objects.filter(user=self.request.user)


class WodCreateView(LoginRequiredMixin, CreateView):
    model = Wod
    form_class = WodForm
    template_name = "wods/create.html"
    success_url = reverse_lazy("home")

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.object = None
        form = self.get_form()
        if not form.is_valid():
            return self.form_invalid(form)

        wod = form.save(commit=False)
        wod.user = request.user
        wod.save()

        self.object = wod

        return HttpResponseRedirect(self.get_success_url())
