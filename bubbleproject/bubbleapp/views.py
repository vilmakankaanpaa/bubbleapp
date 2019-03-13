from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request, 'bubbleapp/index.html', {})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bubbleapp')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'bubbleapp/req_form.html', args)
