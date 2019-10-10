from django.shortcuts import render, redirect
from .models import NewList
from .forms import NewListForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = NewListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = NewList.objects.all
            return render(request, 'ShopList_app/home.html', {'all_items': all_items})
    else:
        all_items = NewList.objects.all
        return render(request, 'ShopList_app/home.html', {'all_items' : all_items})
