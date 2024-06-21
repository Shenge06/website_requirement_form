# requirements/views.py

from django.shortcuts import render, redirect
from .forms import ClientForm, ProjectForm, FunctionalityForm, ContentForm, TimelineBudgetForm, AdditionalCommentsForm

def website_requirement_form(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        project_form = ProjectForm(request.POST)
        functionality_form = FunctionalityForm(request.POST)
        content_form = ContentForm(request.POST)
        timeline_form = TimelineBudgetForm(request.POST)
        additional_comments_form = AdditionalCommentsForm(request.POST)

        if (client_form.is_valid() and project_form.is_valid() and functionality_form.is_valid() and 
            content_form.is_valid() and timeline_form.is_valid() and additional_comments_form.is_valid()):
            client_form.save()
            project_form.save()
            functionality_form.save()
            content_form.save()
            timeline_form.save()
            additional_comments_form.save()
            return redirect('success')
    else:
        client_form = ClientForm()
        project_form = ProjectForm()
        functionality_form = FunctionalityForm()
        content_form = ContentForm()
        timeline_form = TimelineBudgetForm()
        additional_comments_form = AdditionalCommentsForm()

    context = {
        'client_form': client_form,
        'project_form': project_form,
        'functionality_form': functionality_form,
        'content_form': content_form,
        'timeline_form': timeline_form,
        'additional_comments_form': additional_comments_form
    }

    return render(request, 'requirements/website_requirement_form.html', context)

def success(request):
    return render(request, 'requirements/success.html')
