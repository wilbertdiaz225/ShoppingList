from django.shortcuts import render, redirect
from .models import List
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NewListForm

# Create your views here.

def home(request):
        all_lists = List.objects.all()
        return render(request, 'ShopList_app/home.html', {'all-items': all_lists})

def addNewList(request):
        new_lists = List(list_name = request.POST['new_list'])
        new_lists.save()
        return HttpResponseRedirect('/')