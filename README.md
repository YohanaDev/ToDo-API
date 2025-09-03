ToDo API – Prueba Backend

API REST desarrollada en Django + Django REST Framework para la gestión de tareas, con autenticación por JWT y documentación con Swagger.
Tecnologías usadas:
Python 3
Django
Django REST Framework
Simple JWT (autenticación JWT)
drf-yasg (documentación Swagger)
Instalación y configuración
1. Clonar el repositorio:
   codigo:
   git clone https://github.com/YohanaDev/prueba-backend.git
   cd prueba-backend
2. Crear y activar entorno virtual
   codigo:
   python -m venv venv
    source venv/bin/activate   # Linux / Mac
    venv\Scripts\activate      # Windows
3. Instalar dependencias
   pip install -r requirements.txt
4. Aplicar migraciones
   python manage.py migrate
5. Crear superusuario
   python manage.py createsuperuser
6. Levantar el servidor
   python manage.py runserver

Autenticación (JWT)
Obtener tokens
Endpoint: POST /api/token/
Body:
{
  "username": "TU_USUARIO",
  "password": "TU_PASSWORD"
}
Respuesta:
{
  "refresh": "djdjsdksdhbgygde...",
  "access": "sklsnhdshdnz..."
}
Usar el token access en los requests
Authorization: Bearer TU_TOKEN_ACCESS

Renovar token
Endpoint: POST /api/token/refresh/
Body:
{
  "refresh": "edksdoerdmd..."
}
Documentación Swagger

La API está documentada en Swagger UI.
Después de iniciar el servidor, entra a:
 http://127.0.0.1:8000/swagger/

Endpoints principales

POST /api/token/ → Obtener token JWT
POST /api/token/refresh/ → Refrescar token
GET /api/tasks/ → Listar tareas del usuario autenticado
POST /api/tasks/ → Crear nueva tarea
GET /api/tasks/{id}/ → Detalle de tarea
PUT /api/tasks/{id}/ → Editar tarea
DELETE /api/tasks/{id}/ → Eliminar tarea

Pruebas unitarias
Ejecutar los tests con:
python manage.py test
Los tests cubren:
Creación de tareas
Listado de tareas
Actualización de tareas
Eliminación de tareas
