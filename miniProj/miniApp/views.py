from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import TimeCardModel
from .forms import TimeCardForm


# Create your views here.
def index(request):
    return render(request, 'miniApp/index.html')


def info(request):
    allTime = TimeCardModel.objects.all()
    return render(request, 'miniApp/infoPage.html', {'allTime': allTime})


def namesInfo(request, id):
    allTheNames = get_object_or_404(TimeCardModel, pk=id)
    return render(request, 'miniApp/namesInfo.html', {'allTheNames': allTheNames})


