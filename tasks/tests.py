from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task


class TaskAPITestCase(APITestCase):
    def setUp(self):
        # Crear usuario de prueba
        self.user = User.objects.create_user(username="heidy", password="heidy1234")

        # Obtener token de acceso
        response = self.client.post("/api/token/", {
            "username": "heidy",
            "password": "heidy1234"
        })
        self.assertEqual(response.status_code, 200)
        self.token = response.data["access"]

        # Agregar token en headers para futuras peticiones
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

    def test_create_task(self):
        """Probar creación de tarea"""
        data = {"title": "Test tarea", "description": "Probando creación"}
        response = self.client.post("/api/tasks/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Test tarea")

    def test_list_tasks(self):
        """Probar listado de tareas"""
        Task.objects.create(title="Tarea 1", description="Desc", user=self.user)
        Task.objects.create(title="Tarea 2", description="Desc", user=self.user)

        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_task(self):
        """Probar actualización de una tarea"""
        task = Task.objects.create(title="Viejo título", description="Desc", user=self.user)
        data = {"title": "Nuevo título", "description": "Actualizada"}
        response = self.client.put(f"/api/tasks/{task.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Nuevo título")

    def test_delete_task(self):
        """Probar eliminación de una tarea"""
        task = Task.objects.create(title="Eliminar", description="Desc", user=self.user)
        response = self.client.delete(f"/api/tasks/{task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=task.id).exists())
