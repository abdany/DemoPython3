from django.http import HttpResponse
from django.shortcuts import render
from .models import place, team



def demo(request):
    obj = place.objects.all()
    team1 = team.objects.all()
    return render(request, "index.html", {'result': obj,'team':team1})



# def demo2(request):
#     obj2 = people.objects.all()
#     return render(request, "index.html", {'result2': obj2})


# Create your views here.
