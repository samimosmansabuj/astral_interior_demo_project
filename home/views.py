from django.shortcuts import render
from .models import *

def home(request):
    company_information = CompanyInformation.objects.all().first()
    service = OurService.objects.filter(active=True)
    project = OurProject.objects.filter(active=True)
    team = OurTeam.objects.filter(active=True)
    contaxt = {
        'company_information': company_information,
        'service': service,
        'project': project,
        'team': team,
    }
    return render(request, 'home/home.html', contaxt)


def home2(request):
    company_information = CompanyInformation.objects.all().first()
    service = OurService.objects.filter(active=True)
    project = OurProject.objects.filter(active=True)
    team = OurTeam.objects.filter(active=True)
    contaxt = {
        'company_information': company_information,
        'service': service,
        'project': project,
        'team': team,
    }
    return render(request, 'home2.html', contaxt)