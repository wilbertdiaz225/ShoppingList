from django.shortcuts import render, redirect
from .models import List
from .models import Item
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NewListForm

# Create your views here.

current_id = 0,

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

def displayItem(request, list_id):
        all_lists_names = List.objects.all()
        global current_id
        current_id = list_id
        items = Item.objects.filter(item_list_id = current_id),
        print(items)
        return render(request, 'ShopList_app/home.html', {'all_names': all_lists_names, 'all_items': items})

def addNewItem(request):
        new_item = Item(item_name = request.POST['new_item'])
        global current_id
        new_item.item_list_id = current_id
        new_item.save()
        return HttpResponseRedirect('/')