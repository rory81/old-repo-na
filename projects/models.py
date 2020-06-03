from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta

CATEGORIES = (
    ('Arts', 'Arts'),
    ('Charity', 'Charity'),
    ('Film', 'Film'),
    ('Food', 'Food'),
    ('Games', 'Games'),
    ('Music', 'Music'),
    ('Publishing', 'Publishing'),
    ('Technology', 'Technology'),
)


class Project(models.Model):
    created_by = models.CharField(max_length=50, null=False)
    created_date = models.DateField(default=datetime.now, null=False)
    title = models.CharField(max_length=90, null=False, blank=False, verbose_name="project title")
    # image = models.ImageField(upload_to="img", null=False, blank=False)
    category = models.CharField(max_length=10, null=False, blank=False, choices=CATEGORIES)
    description = models.CharField(max_length=50000, null=False, blank=False, verbose_name="project description")
    backers_story = models.CharField(max_length=50000, null=False, blank=False, verbose_name="what's in it for the backers?")
    goal = models.IntegerField(default=0, null=False, blank=False)
    end_date = models.DateField(default=datetime.now()+relativedelta(months=1), null=False, blank=False)
    num_raised = models.IntegerField(default=0, null=False)
    num_views = models.IntegerField(default=0, null=False)
    num_days = models.IntegerField(default=0, null=False)

    def __str__(self):
        """
        In the admin view the project will be displayed as "Project Object" unless it is identified differently.
        We can override that standard string method. This string method uses itself as its own argument and return the projects title
        """
        return self.title
