from django.db import models

class Data(models.Model):
	ip = models.CharField(max_length=20)
	continente = models.CharField(max_length=30,null=True,blank = True)
	country = models.CharField(max_length=80,null=True,blank = True)
	city = models.CharField(max_length=100,null=True,blank = True)
	latitude = models.CharField(max_length=100,null=True,blank = True)
	longitude = models.CharField(max_length=100,null=True,blank = True)
	localitation = models.CharField(max_length=100,null=True,blank = True)


	