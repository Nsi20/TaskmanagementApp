from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APIClient
from .models import Task

class TaskAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
        
        # Create some test tasks
        self.task1 = Task.objects.create(
            user=self.user,
            title='Test Task 1',
            description='Description 1',
            priority='H',
            status='TODO'
        )
        self.task2 = Task.objects.create(
            user=self.user,
            title='Test Task 2',
            description='Description 2',
            priority='M',
            status='IN_PROGRESS'
        )

    def test_list_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)
        # Check that we get a list of tasks directly
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Test Task 1')

    def test_create_task(self):
        data = {
            'title': 'New Task',
            'description': 'New Description',
            'priority': 'L',
            'status': 'TODO'
        }
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(response.data['title'], 'New Task')

    def test_complete_task(self):
        response = self.client.post(f'/api/tasks/{self.task1.id}/complete/')
        self.assertEqual(response.status_code, 200)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.status, 'DONE')
        self.assertEqual(response.data['status'], 'DONE')

    def test_analytics(self):
        response = self.client.get('/api/tasks/analytics/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['total_tasks'], 2)
        self.assertEqual(response.data['completed_tasks'], 0)
