from django.db import models

# Create your models here.
class CountryData(models.Model):
    country = models.CharField(max_length=100)
    population = models.IntegerField()

    def __str__(self):
        return f'{self.country}--{self.population}'

# models.py를 건들거나 생성을했을때 꼭꼭 must cmder에다가 
#python manage.py makemigrations
#python manage.py migrate 해야한다