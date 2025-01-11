from django.shortcuts import render
from rest_framework import generics 
from rest_framework.permissions import AllowAny
from .serializers import OrderSerializer 
from .models import Order

def index(request):
    return render(request, 'backend/index.html')

class OrderListCreate(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        print(Order.objects.all())
        return Order.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            print(serializer.validated_data)
        else: 
            print(serializer.errors)

class OrderUpdate(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Order.objects.all() 
    
    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save() 
            print(serializer.validated_data)
        else:
            print(serializer.errors)

class OrderDelete(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Order.objects.all()
    