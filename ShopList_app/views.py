from django.shortcuts import render, redirect
from .models import List
from .models import Item
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NewListForm

# Create your views here.

def home(request):
        all_lists_names = List.objects.all()
        all_item_names = Item.objects.all()
        return render(request, 'ShopList_app/home.html', {'all_names': all_lists_names, 'all_items' : all_item_names})

def addNewList(request):
        new_lists = List(list_name = request.POST['new_list'])
        new_lists.save()
        return HttpResponseRedirect('/')

def deleteList(request, list_id):
        list_to_delete = List.objects.get(id = list_id)
        list_to_delete.delete()
        return HttpResponseRedirect('/')

def displayItem(request):
        list = request.GET.get('list_id',None)
        item_list = List.objects.filter( id = list )
        all_lists_names = List.objects.all()
        items = Item.objects.filter(item_list_id=list),
        return render(request, 'ShopList_app/home.html', {'all_names': all_lists_names, 'all_items': items, 'items_list': item_list})

def addNewItem(request):
        new_item = Item(item_name = request.POST['new_item'])
        new_item.save()
        return HttpResponseRedirect('/')