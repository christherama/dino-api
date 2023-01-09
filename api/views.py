import os

from django.http import Http404, HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from dino.models import Dinosaur
from api.serializers import DinosaurSerializer


def docs(request):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    docs_path = os.path.join(current_dir, "docs/generated-docs.html")
    try:
        with open(docs_path, "r") as f:
            content = f.read()
    except OSError:
        raise Http404("Page not found")
    else:
        return HttpResponse(content)


class DinosaurListView(ListCreateAPIView):
    serializer_class = DinosaurSerializer
    permission_classes = []

    def get_queryset(self):
        return Dinosaur.objects.all()


class DinosaurView(RetrieveAPIView):
    serializer_class = DinosaurSerializer
    permission_classes = []

    def get_queryset(self):
        return Dinosaur.objects.all()
