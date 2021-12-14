from django.http import HttpResponse
from django.shortcuts import render
from .models import Data


def index(request):
	if request.is_ajax():
		Data(
			latitude = request.GET.get('la'),
			longitude = request.GET.get('lon'),
		).save()
	return render(request,'index.html')

