from random import choices
from django.db import models
# Create your models here.

class solventForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=1000)
    phone = models.IntegerField()
    state = models.CharField(max_length=40, choices=[(None, 'State'), ('river', 'Rivers')])
    location = models.CharField(max_length=40, choices=[(None, 'Geographical Location'), ('eleme', 'Eleme'),('bolo', 'Bolo'), ('etche', 'Etche'), ('ikwere', 'Ikwere'), ('obio-akpor', 'Obio-Akpor'), ('oyigbo', 'Oyigbo'), ('okrika', 'Okrika')])
    houses = models.CharField(max_length=40, choices=[(None, 'Houses'), ('mini_flats', 'Mini_Flats'), ('ware_house', 'Ware_House'), ('plots_&_land', 'Plots_&_Land'), ('duplex', 'Duplex'), ('office_space', 'Office_Space'), ('terraced_bungalow', 'Terraced_Bungalow'), ('houses', 'House')])
    describe = models.CharField(max_length=64)

    def  __str__(self):
        return self.name