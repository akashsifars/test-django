from django import forms
from django.shortcuts import redirect, render
from django.shortcuts import render
from . import forms
from ..models import Forms
import datetime

# Create your views here.

def index(request):
    # temp = get_template('form.html')
    # print(temp)
    # return render(request, 'mysite/polls/templates/form.html')
    # return HttpResponse('<html><body><form to="/submit" method="POST"><input type="text" name="first_name" value="" /><input type="text" name="last_name" value="" /><input type="submit" value="Submit" name="submit"></form></body></html>')
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
    
    if form.is_valid():
        print("Form validation successful! See console for information:")
        print("Name: "+form.cleaned_data['name'])
        print(form.cleaned_data['start_date'])
        print(form.cleaned_data['end_date'])
        print("Category "+form.cleaned_data['category'])
        # start_date = datetime.strptime(form.cleaned_data['start_date'], "%m-%d-%Y").date()
        # end_date = datetime.strptime(form.cleaned_data['start_date'], "%m-%d-%Y").date()
        # print(start_date)
        # print(end_date)
        Forms.objects.create(name = form.cleaned_data['name'], start_date = form.cleaned_data['start_date'], end_date = form.cleaned_data['end_date'], category = form.cleaned_data['category'],)
        return redirect('/list')

    return render(request, 'form.html', {'form': form})

def submit(request):
    print(request)