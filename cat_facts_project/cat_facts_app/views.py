import requests
from django.shortcuts import render
from django.http import JsonResponse

def get_cat_fact():
    url = 'https://cat-fact.herokuapp.com/facts/random'
    response = requests.get(url)
    fact = response.json()['text']
    return fact

def cat_facts(request):
    if request.method == 'POST':
        fact = get_cat_fact()
        return JsonResponse({'fact': fact})
    return render(request, 'cat_facts_project/cat_facts.html')

