from django.http import HttpResponse
from django.shortcuts import render
from .models import Data


def index(request):
	if request.is_ajax():
		try:
			data = Data.objects.get(ip = request.GET['geoplugin_request'])
		except Data.DoesNotExist:
			Data(
				ip = request.GET['geoplugin_request'],
				continente = request.GET['geoplugin_continentName'],
				country = request.GET['geoplugin_countryName'],
				city = request.GET['geoplugin_city'],
				latitude = request.GET['geoplugin_latitude'],
				longitude = request.GET['geoplugin_longitude'],
				localitation = request.GET['region_name']
			).save()
	return render(request,'index.html')

