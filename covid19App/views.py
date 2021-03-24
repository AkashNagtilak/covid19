from django.shortcuts import render
import requests


def index(request):
    data = True
    result = None
    Countries = None
    globalSummary = None
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()

            globalSummary= json['Global']
            Countries = json['Countries']
            data = False
        except:
            data = True
    return render(request, 'covid19App/index.html',{'globalSummary': globalSummary,'Countries':Countries})
