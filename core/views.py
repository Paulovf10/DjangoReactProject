from django.shortcuts import render, get_object_or_404
from rest_framework.generics import get_object_or_404
from .models import Contact


def index(request):
    context = {}

    return render(request, "home.html", context)
