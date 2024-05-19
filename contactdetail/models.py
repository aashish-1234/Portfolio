from django.db import models


class contactDetail(models.Model):
    name=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    message=models.TextField()
    subject=models.CharField( max_length=50)

