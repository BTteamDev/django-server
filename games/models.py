# games/models.py
from django.db import models

class Game(models.Model):
    itemName = models.CharField(max_length=100) # Название [cite: 565]
    price = models.IntegerField()              # Цена [cite: 570]

    def __str__(self):
        return self.itemName