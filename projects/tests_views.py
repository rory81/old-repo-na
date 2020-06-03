from django.test import TestCase
from .models import Project


class TestViews(TestCase):
    def test_get_projects(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/projects_lists.html')

    def test_get_add_project_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/add_project.html')

    def test_get_edit_project_page(self):
        project = Project.objects.create(title='Testing item')
        response = self.client.get(f'/edit/{project.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/edit_project.html')

    def test_can_add_project(self):
        response = self.client.post('/add', {'title': 'only added a Title'})
        self.assertRedirects(response, '/')

    def test_can_delete_project(self):
        project = Project.objects.create(title='Testing item')
        response = self.client.get(f'/delete/{project.id}')
        self.assertRedirects(response, '/')
        existing_projects = Project.objects.filter(id=project.id)
        self.assertEqual(len(existing_projects), 0)

    def test_can_edit_project(self):
        project = Project.objects.create(title='Testing item')
        response = self.client.post(f'/edit/{project.id}', {'title': 'Updated Title'})
        self.assertRedirects(response, '/')
        updated_title = Project.objects.get(id.project.id)
        self.assertEqual(updated_title, 'Updated Title')
