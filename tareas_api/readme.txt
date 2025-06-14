Instrucciones de uso de “tareas_api”

Iniciar el servidor:
python manage.py runserver


Usar Postman para probar los endpoints:
• GET http://127.0.0.1:8000/api/tareas/ - Listar todas las tareas
• POST http://127.0.0.1:8000/api/tareas/ - Crear nueva tarea

  Usar esta dirección en el navegador para Listar las tareas y para agregar
  tareas nuevas

• GET/PUT/DELETE http://127.0.0.1:8000/api/tareas/#/ - Operaciones con tarea
  específica.Usar esta dirección en el navegador, donde # es el id de la 
  tarea a borrar o modificar. Si se encuentra el ID = # se puede borrar la
  tarea con el botón “DELETE” o se puede modificar marcando o desmarcando la
  casilla “Completado” o cambiando el titulo o la descripción haciendo PUT.
  
  OPTIONS muestra el contenido de la tarea y el estado de las variables
  definidas en ellos campos.
  
  En GET se cambia la vista a modo JSON yo a la vista de la API.
