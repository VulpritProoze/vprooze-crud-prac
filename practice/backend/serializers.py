from rest_framework import serializers
from .models import Order 
from datetime import datetime

class OrderSerializer(serializers.ModelSerializer):
    formatted_date = serializers.SerializerMethodField()

    class Meta:
        model = Order 
        fields = ['order_id', 'food_name', 'order_date', 'formatted_date']        
    
    def get_formatted_date(self, obj):
        if obj.order_date:
            return obj.order_date.strftime('%Y-%m-%d %H:%M:%S')
        return None