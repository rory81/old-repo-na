from django.test import TestCase
from .models import Project
from datetime import datetime
from dateutil.relativedelta import relativedelta


class TestDjango(TestCase):
    def test_num_days_zero_default(self):
        project = Project.objects.create(title='Testing item')
        self.assertEqual(project.num_days, 0)

    def test_num_raised_zero_default(self):
        project = Project.objects.create(title='Testing item')
        self.assertEqual(project.num_raised, 0)

    def test_num_views_zero_default(self):
        project = Project.objects.create(title='Testing item')
        self.assertEqual(project.num_views, 0)

    def test_default_end_date(self):
        project = Project.objects.create(title='Testing item')
        self.assertEqual(project.end_date.month, (datetime.now()+relativedelta(months=1)).month)

    def test_project_string_method_returns_title(self):
        project = Project.objects.create(title='Testing item')
        self.assertEqual(str(project), 'Testing item')
