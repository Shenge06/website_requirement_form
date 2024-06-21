from django import forms
from .models import Client, Project, Functionality, Content, TimelineBudget, AdditionalComments

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name', 'email', 'phone_number', 
            'company_name', 'company_industry', 
            'current_website'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_industry': forms.TextInput(attrs={'class': 'form-control'}),
            'current_website': forms.URLInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'name': 'Please provide your full name.',
            'email': 'We will use this email to contact you about your website.',
            'phone_number': 'A contact number where we can reach you.',
            'company_name': 'If applicable, provide your company\'s name.',
            'company_industry': 'What industry does your company operate in?',
            'current_website': 'Provide the URL of your existing website, if applicable.',
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'project_type', 'project_description', 
            'design_style_preference', 'color_preferences', 
            'inspiration_websites'
        ]
        widgets = {
            'project_type': forms.Select(attrs={'class': 'form-control'}),
            'project_description': forms.Textarea(attrs={'class': 'form-control'}),
            'design_style_preference': forms.TextInput(attrs={'class': 'form-control'}),
            'color_preferences': forms.TextInput(attrs={'class': 'form-control'}),
            'inspiration_websites': forms.URLInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'project_type': 'E.g., Business, Portfolio, Blog, E-commerce, etc.',
            'project_description': 'Describe your vision for the website and its main goals.',
            'design_style_preference': 'Do you have any specific design styles or color schemes in mind?',
            'color_preferences': 'Specify any color preferences for the website.',
            'inspiration_websites': 'List any websites that inspire your design choices.',
        }

class FunctionalityForm(forms.ModelForm):
    class Meta:
        model = Functionality
        fields = ['key_features', 'special_requirements']
        widgets = {
            'key_features': forms.Textarea(attrs={'class': 'form-control'}),
            'special_requirements': forms.Textarea(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'key_features': 'List the main features your website should have.',
            'special_requirements': 'Specify any special requirements or functionality.',
        }

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['content_provider', 'estimated_pages', 'existing_content']
        widgets = {
            'content_provider': forms.TextInput(attrs={'class': 'form-control'}),
            'estimated_pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'existing_content': forms.Textarea(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'content_provider': 'Who will provide the content for the website?',
            'estimated_pages': 'Estimated number of pages the website will have.',
            'existing_content': 'Details of any existing content to be used.',
        }

class TimelineBudgetForm(forms.ModelForm):
    class Meta:
        model = TimelineBudget
        fields = ['expected_launch_date', 'budget_range']
        widgets = {
            'expected_launch_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'budget_range': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'expected_launch_date': 'When do you need the website to be completed?',
            'budget_range': 'What is your budget for this project?',
        }

class AdditionalCommentsForm(forms.ModelForm):
    class Meta:
        model = AdditionalComments
        fields = ['additional_comments']
        widgets = {
            'additional_comments': forms.Textarea(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'additional_comments': 'Any other information you\'d like to share?',
        }
PROJECT_TYPE_CHOICES = [
    ('business', 'Business'),
    ('portfolio', 'Portfolio'),
    ('blog', 'Blog'),
    ('ecommerce', 'E-commerce'),
    # Add more choices as needed
]

class ProjectForm(forms.Form):
    project_type = forms.ChoiceField(choices=PROJECT_TYPE_CHOICES, label='Project Type')
    project_description = forms.CharField(label='Project Description', widget=forms.Textarea(attrs={'rows': 4}))
    design_style_preference = forms.CharField(label='Design Style Preference', max_length=100)
    color_preferences = forms.CharField(label='Color Preferences', max_length=100)
    inspiration_websites = forms.CharField(label='Inspiration Websites', widget=forms.Textarea(attrs={'rows': 4}))