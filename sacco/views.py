from django.shortcuts import render, redirect
from .models import Sacco, Super_list
from .forms import SaccoForm, Super_listForm

# Create your views here.

def dashboard(request):
    '''
    View function to display all that a user will be interacting with fromm the onset of the app.
    '''
    return render(request, 'all/dashboard.html')

# def sacco(request):
#     '''
#     View function to enable one register a new sacco
#     '''
#     current_user = request.user
#     if request.method == 'POST':
#         user_form = SaccoForm(data=request.POST)
#         if user_form.is_valid():
#             post = user_form.save(commit=False)
#             post.user = current_user
#             post.save()
#             return redirect('sacco_home')
#     else:
#         user_form = SaccoForm()
#     return render(request, 'all/sacco.html', {"user_form": user_form})


def superlist(request):
    current_user = request.user
    if request.method == 'POST':
        form = Super_listForm(request.POST)
        if form.is_valid():
            supervisor = form.save(commit=False)
            supervisor.user = current_user
            supervisor.save()
            return redirect('sacco_home')
    else:
        form = Super_listForm()
    return render(request, 'all/supervisor.html', {"form": form})
