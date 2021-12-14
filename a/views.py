from django.http import HttpResponse
from django.shortcuts import render
from .models import Data


def index(request):
	if request.is_ajax():
		print(request.GET['ip'])
		try:
			data = Data.objects.get(ip = request.GET['ip'])
		except Data.DoesNotExist:
			Data(
				ip = request.GET['ip'],
				continente = request.GET['continent_code'],
				country = request.GET['country_name'],
				city = request.GET['city'],
				latitude = request.GET['latitude'],
				longitude = request.GET['longitude'],
				localitation = request.GET['region_name']
			).save()
	return render(request,'index.html')

