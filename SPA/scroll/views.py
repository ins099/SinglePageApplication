from django.shortcuts import render
import time

from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'scroll/index.html')

def post(request):
    # getting start adn end points 
    start = int (request.GET.get("start") or 0)
    end = int (request.GET.get("end") or (start +9) )

    # creating posts 
    data = []
    for i in range(start, end+1):
        data.append(f"Post# {i}")

    time.sleep(1)

#return data to JS 

    return JsonResponse({
         "posts":data
        })