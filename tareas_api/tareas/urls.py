from django.urls import path
from .views import ListaTareas, DetalleTarea

urlpatterns = [
    path('tareas/', ListaTareas.as_view(), name='lista-tareas'),
    path('tareas/<int:pk>/', DetalleTarea.as_view(), name='detalle-tarea'),
]
