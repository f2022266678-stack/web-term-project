from django.shortcuts import render
from bio.models import Bio
from education.models import Education
from skills.models import Skill
from experience.models import Experience
from projects.models import Project

# Create your views here.

def home(request):
    # Fetch the first Bio object
    bio = Bio.objects.first()
    
    # Fetch all objects for Education, Skill, Experience, and Project
    educations = Education.objects.all().order_by('-start_date')
    skills = Skill.objects.all().order_by('category', 'name')
    experiences = Experience.objects.all().order_by('-start_date')
    projects = Project.objects.all()
    
    context = {
        'bio': bio,
        'education': educations,
        'skills': skills,
        'experience': experiences,
        'projects': projects,
    }
    
    return render(request, 'home.html', context)
