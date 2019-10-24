from django.shortcuts import render, redirect
from .models import List
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NewListForm

# Create your views here.

def home(request):
        all_lists_names = List.objects.all()
        return render(request, 'ShopList_app/home.html', {'all_names': all_lists_names})

def addNewList(request):
        new_lists = List(list_name = request.POST['new_list'])
        new_lists.save()
        return HttpResponseRedirect('/')

def deleteList(request, list_id):
        list_to_delete = List.objects.get(id = list_id)
        list_to_delete.delete()
        return HttpResponseRedirect('/')