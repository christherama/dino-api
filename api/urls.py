from django.urls import path

from api import views

app_name = "api"

urlpatterns = [
    path("docs/", views.docs),
    path("dinosaurs/", views.DinosaurListView.as_view(), name="dinosaurs"),
    path("dinosaurs/<int:pk>/", views.DinosaurView.as_view(), name="dinosaur"),
]
