from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    teste = [
        {'nome': 'João', 'idade': 20},
    ]
    return render(request, 'app/index.html', {'teste': teste})
    