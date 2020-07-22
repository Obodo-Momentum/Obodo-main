from django.shortcuts import render, redirect, get_object_or_404
from .models import RequestOfferPost, Tag
from users.models import User
from .forms import RequestOfferForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'Obodo/homepage.html')

def add_request_offer(request):
    if request.method == 'POST':
        form = RequestOfferForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect(to='homepage')
    else:
        form = RequestOfferForm()
    
    return render(request, 'Obodo/add_request_offer.html', {
        'form': form,
    })