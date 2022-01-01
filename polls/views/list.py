from django.shortcuts import render
from ..models import Forms

def list_data(request):
    list = Forms.objects.values()
    set = []
    for data in list:
        dict = {
            'name': data['name'],
            'start_date': data['start_date'],
            'end_date': data['end_date'],
            'category': data['category'],
        }
        set.append(dict)
    return render(request, 'list.html',{'list': set})