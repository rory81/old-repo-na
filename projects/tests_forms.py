from django.test import TestCase
from .forms import ProjectForm


class TestProjectForm(TestCase):
    def test_project_title_is_required(self):
        form = ProjectForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_project_category_is_required(self):
        form = ProjectForm({'category': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0], 'This field is required.')

    def test_project_description_is_required(self):
        form = ProjectForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')

    def test_project_backers_story_is_required(self):
        form = ProjectForm({'backers_story': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('backers_story', form.errors.keys())
        self.assertEqual(form.errors['backers_story'][0], 'This field is required.')

    def test_project_goal_is_required(self):
        form = ProjectForm({'goal': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('goal', form.errors.keys())
        self.assertEqual(form.errors['goal'][0], 'This field is required.')

    def test_project_end_date_is_required(self):
        form = ProjectForm({'end_date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('end_date', form.errors.keys())
        self.assertEqual(form.errors['end_date'][0], 'This field is required.')

    def test_project_created_by_is_required(self):
        form = ProjectForm({'created_by': ''})
        self.assertFalse(form.is_valid())

    def test_project_created_date_is_required(self):
        form = ProjectForm({'created_date': ''})
        self.assertFalse(form.is_valid())

    def test_project_num_raised_is_required(self):
        form = ProjectForm({'num_raised': ''})
        self.assertFalse(form.is_valid())

    def test_project_num_views_is_required(self):
        form = ProjectForm({'num_views': ''})
        self.assertFalse(form.is_valid())

    def test_project_num_days_is_required(self):
        form = ProjectForm({'num_days': ''})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ProjectForm()
        self.assertEqual(form.Meta.fields, [
            'title',
            'category',
            'description',
            'backers_story',
            'goal',
            'end_date'
        ])
