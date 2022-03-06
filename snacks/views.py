from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Snack
from django.urls import reverse_lazy

# Create your views here.


class SnackListView(ListView):
    template_name = "snack-list.html"
    model = Snack


class SnackDetailView(DetailView):
    template_name = "snack-detail.html"
    model = Snack


class SnackCreateView(CreateView):
    template_name = "snack-create.html"
    model = Snack
    fields = ["title", "purchaser", "description"]


class SnackUpdateView(UpdateView):
    template_name = "snack-update.html"
    model = Snack
    fields = ["title", "purchaser", "description"]


class SnackDeleteView(DeleteView):
    template_name = "snack-delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")
