from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SearchReq
from .forms import SearchReqForm


# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def create(request):
    error = ''
    if request.method == "POST":
        form = SearchReqForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacans/')
        else:
            error = 'Форма была неверной'





    form = SearchReqForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'main/index.html', data)