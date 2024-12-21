from django.shortcuts import render
from .models import Header, Education, About, Experience, Skill, Project, SocialNetwork

# Create your views here.
def home_page(request):
    header=Header.objects.last()
    educations=Education.objects.all()
    about=About.objects.all()
    experiences=Experience.objects.all()
    skills=Skill.objects.all()
    projects=Project.objects.all()
    socials=SocialNetwork.objects.all()
    for experience in experiences:
        experience.description=experience.description.strip().split("\n")
    return render(request, 'index.html',{"header":header,"educations":educations, "about":about, "experiences":experiences, "skills":skills, "projects":projects, "socials":socials})
