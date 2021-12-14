from django.http import HttpResponse
from django.shortcuts import render
from .models import Data


def index(request):
	Data(
		ip = request.META.get("REMOTE_ADDR")
	).save()
	return HttpResponse("Hola")

