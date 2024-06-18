# requirement_app/views.py
from django.shortcuts import render
from .forms import WebsiteRequirementForm
from .models import WebsiteRequirement

def requirement_form_view(request):
    if request.method == 'POST':
        form = WebsiteRequirementForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            WebsiteRequirement.objects.create(**form.cleaned_data)
            return render(request, 'requirement_app/form_success.html', {'form_data': form.cleaned_data})
    else:
        form = WebsiteRequirementForm()
    return render(request, 'requirement_app/form.html', {'form': form})
