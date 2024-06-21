# requirements/models.py

from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    company_industry = models.CharField(max_length=100)
    current_website = models.URLField(blank=True)

class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    project_type = models.CharField(max_length=50)
    project_description = models.TextField()
    design_style_preference = models.CharField(max_length=100)
    color_preferences = models.TextField()
    inspiration_websites = models.TextField()

class Functionality(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    key_features = models.TextField()
    special_requirements = models.TextField()

class Content(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    content_provider = models.CharField(max_length=50)
    estimated_pages = models.IntegerField()
    existing_content = models.TextField()

class TimelineBudget(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    expected_launch_date = models.DateField()
    budget_range = models.CharField(max_length=50)

class AdditionalComments(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    additional_comments = models.TextField()
