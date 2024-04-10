from django.shortcuts import render

def index(request):
  
  projects = [
    {
      'title': 'Prescriptech',
      'description': 'An electronic prescription-issuing and consultation system.',
      'images': [
        'healthcare-provider-login.jpg',
        'healthcare-provider-registration.jpg',
        'new-consultation.jpg',
        'patient-overview-santos.jpg',
        'pharmacy-backup-code.jpg',
        'prescription-editor.jpg',
      ]
    },
  ]
  
  return render(request, "main/index.html", {'projects': projects})