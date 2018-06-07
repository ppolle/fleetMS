from django.shortcuts import render
from .models import Sacco, Super_list

# Create your views here.
def dashboard(request):
    '''
    View function to dsplay all that a user will be interacting with fromm the onset of the app.
    '''
    sacco = Sacco.objects.all()
    return render(request, 'all/dashboard.html', {"sacco": sacco})
