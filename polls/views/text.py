from django import forms
from django.shortcuts import redirect, render
from django.shortcuts import render
from . import forms
from ..models import Forms
from django.http import JsonResponse
import json

# Create your views here.

def index(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
    
    if form.is_valid():
        print("Form validation successful! See console for information:")
        print("Name: "+form.cleaned_data['name'])
        print(form.cleaned_data['start_date'])
        print(form.cleaned_data['end_date'])
        print("Category "+form.cleaned_data['category'])
        Forms.objects.create(name = form.cleaned_data['name'], start_date = form.cleaned_data['start_date'], end_date = form.cleaned_data['end_date'], category = form.cleaned_data['category'],)
        return redirect('/list')

    return render(request, 'form.html', {'form': form})

def submit(request):
    print(request)

def login(request):
    status = 'true'
    data = json.loads(request.body)
    status = 'false'
    if status == 'false':
        return JsonResponse({'error': "User not found"}, status = 423)
    else :
        return JsonResponse({}, status = 200)