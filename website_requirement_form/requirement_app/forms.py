# requirement_app/forms.py

from django import forms

class WebsiteRequirementForm(forms.Form):
    client_name = forms.CharField(label='Client Name', max_length=100)
    company_name = forms.CharField(label='Company Name', max_length=100)
    email = forms.EmailField(label='Email Address')
    phone_number = forms.CharField(label='Phone Number', max_length=20)
    website_purpose = forms.ChoiceField(
        label='What is the main purpose of the website?',
        choices=[
            ('information', 'Information Sharing'),
            ('ecommerce', 'E-commerce'),
            ('portfolio', 'Portfolio'),
            ('blog', 'Blog'),
            ('other', 'Other'),
        ],
        widget=forms.RadioSelect
    )
    other_purpose_specify = forms.CharField(label='Other purpose', required=False)
    business_description = forms.CharField(
        label='Briefly describe your business and the services/products you offer',
        widget=forms.Textarea
    )
    existing_website_url = forms.URLField(label='Existing website URL', required=False)
    primary_colors = forms.CharField(label='Primary colors', required=False)
    fonts_typography = forms.CharField(label='Fonts or typographic styles', required=False)
    website_examples = forms.CharField(
        label='Examples of websites you like and why',
        widget=forms.Textarea,
        required=False
    )
    existing_content = forms.BooleanField(label='Existing content', required=False)
    content_creation_services = forms.BooleanField(
        label='Content creation services needed',
        required=False
    )
    pages_needed = forms.CharField(
        label='List the pages you need on the website',
        widget=forms.Textarea,
        required=False
    )
    features_needed = forms.MultipleChoiceField(
        label='Specific features needed',
        choices=[
            ('contact_form', 'Contact Form'),
            ('newsletter', 'Newsletter Subscription'),
            ('blog', 'Blog/News Section'),
            ('ecommerce', 'E-commerce functionality'),
            ('user_login', 'User Login/Registration'),
            ('social_media', 'Social Media Integration'),
            ('booking', 'Booking/Appointment System'),
            ('search', 'Search Functionality'),
            ('other_feature', 'Other'),
        ],
        widget=forms.CheckboxSelectMultiple
    )
    other_features_specify = forms.CharField(label='Specify other features', required=False)
    integrations_needed = forms.CharField(
        label='Specific integrations needed',
        required=False
    )
    seo_services = forms.BooleanField(label='SEO services needed', required=False)
    keywords_phrases = forms.CharField(
        label='Keywords or phrases to target',
        required=False
    )
    online_marketing = forms.BooleanField(
        label='Online marketing campaigns planned',
        required=False
    )
    domain_hosting = forms.BooleanField(label='Domain and hosting', required=False)
    setup_assistance = forms.BooleanField(
        label='Assistance with domain and hosting setup',
        required=False
    )
    cms_preference = forms.CharField(
        label='Preferred content management system',
        required=False
    )
    maintenance_updates = forms.BooleanField(
        label='Ongoing maintenance and updates needed',
        required=False
    )
    launch_date = forms.DateField(label='Desired launch date', required=False)
    budget_range = forms.CharField(label='Budget range', required=False)
    additional_information = forms.CharField(
        label='Additional information',
        widget=forms.Textarea,
        required=False
    )

    def clean_website_purpose(self):
        purpose = self.cleaned_data['website_purpose']
        if purpose == 'other' and not self.cleaned_data['other_purpose_specify']:
            raise forms.ValidationError('Please specify the other purpose.')
        return purpose