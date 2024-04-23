from django.db import models



# Create your models here.



class Location(models.Model):

    name=models.CharField(max_length=50)



class eggsInventory(models.Model):



    device = models.CharField(max_length=50, null=True)

    deviceType  = models.CharField(max_length=50, null=True)

    quantity = models.IntegerField(default=0)

    audit = models.DateField(null=True, blank=True)

    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)



    def __str__(self):

        return self.device