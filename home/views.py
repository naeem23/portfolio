from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from .models import TitleSubtitle, Home, About, Skill, Service, Project, Feedback, FollowMe
from .forms import ProjectForm, ContactForm

def home(request):
    title_subtitle = TitleSubtitle.objects.filter(id=1)
    home_query = Home.objects.filter(id=1)
    about = About.objects.filter(id=1)
    skills = Skill.objects.all().order_by('skills')
    service = Service.objects.all().order_by('id')[:3]
    projects = Project.objects.all().order_by('-id')[:3]
    feedbacks = Feedback.objects.all().order_by('-id')[:3]
    follow_me = FollowMe.objects.filter(id=1)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = ContactForm()

    context = {
        'title': title_subtitle,
        'home': home_query,
        'about': about,
        'skill': skills,
        'service': service,
        'project': projects,
        'feedback': feedbacks,
        'follow': follow_me,
        'form': form
    }

    return render(request, 'home/index.html', context)


def portfolio(request):
    title_subtitle = TitleSubtitle.objects.filter(id=1)
    projects = Project.objects.all().order_by('-id')

    context = {
        'title': title_subtitle,
        'project': projects
    }

    return render(request, 'home/portfolio.html', context)

def project(request, slug):
    instance = get_object_or_404(Project, slug=slug)
    context = {
        'i': instance,
    }
    return render(request, 'home/project.html', context)
