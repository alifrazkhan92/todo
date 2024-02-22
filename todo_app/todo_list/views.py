from django.shortcuts import render, redirect
from .models import list
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            all_items = list.objects.all
            messages.success(request, ('Thank you for adding an item into the list.'))
            return render(request, 'home.html', {'all_items':all_items})
    
    else:
        all_items = list.objects.all
        return render(request, 'home.html', {'all_items':all_items})


def about(request):
    context = {'firstname' : 'Ali', 'lastname' : 'Fraz'}
    return render(request, 'about.html', context)


def delete(request, list_id):
    item = list.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('You deleted an item.'))
    return redirect('home')