from django.db import models

class Data(models.Model):
	ip = models.CharField(max_length=20)

	