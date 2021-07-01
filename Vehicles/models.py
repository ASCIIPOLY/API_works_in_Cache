from django.db import models

# Create your models here.
class vehicle_model(models.Model):
    name = models.CharField(max_length=100,unique=True)
    brand = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

 
class vehicle(models.Model):
    km = models.IntegerField()
    plaka = models.CharField(max_length=100,unique=True)
    sase_no =  models.CharField(max_length=100, unique=True)
    renk = models.CharField(max_length=100)
    vehicle_model_id = models.ForeignKey(vehicle_model, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.km} km de {self.vehicle_model_id}'
 