from django.db import models

class Order(models.Model):
    order_id = models.IntegerField(unique=True, primary_key=True)
    food_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.order_id)
