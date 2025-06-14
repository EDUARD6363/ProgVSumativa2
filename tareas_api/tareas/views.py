from django.shortcuts import render

from rest_framework import generics
from .models import Tarea
from .serializers import TareaSerializer

class ListaTareas(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class DetalleTarea(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
