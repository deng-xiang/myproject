from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render

from .models import Project
from .forms import ProjectForm

# Create your views here.
def index(request):
    projects=Project.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ProjectForm()
    context = {
        'projects':projects,
        'form':form,
    }
    return render( request, 'index.html', context=context)