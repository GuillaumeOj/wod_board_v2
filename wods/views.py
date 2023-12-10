from knox.views import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from wods.models import Wod
from wods.serializers import WodSerializer


class WodViewset(ModelViewSet):
    serializer_class = WodSerializer
    queryset = Wod.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
    #     self.object = None
    #     form = self.get_form()
    #     if not form.is_valid():
    #         return self.form_invalid(form)

    #     wod = form.save(commit=False)
    #     wod.user = request.user
    #     wod.save()

    #     self.object = wod

    #     return HttpResponseRedirect(self.get_success_url())
