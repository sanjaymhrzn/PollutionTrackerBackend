from django.db import models

# Create your models here.
class PollutionData(models.Model):
    date = models.DateField(null=False,blank=False)
    air_quality_index = models.IntegerField(default=1,null=True,blank=False)
    water_quality_index = models.IntegerField(default=1,null=True,blank=False)
    ph_level = models.FloatField(default=1.0,null=True,blank=False)
    temperature = models.FloatField(default=1.0,max_length=120,null=True,blank=False)

    def __str__(self):
        return f"Pollution Data - {self.date}"
