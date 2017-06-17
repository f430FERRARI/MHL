from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
    if request.user.is_authenticated():
        return render(request, 'core/home.html') #TODO: Add login context
    else:
        return render(request, 'core/home.html')