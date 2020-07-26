from django.shortcuts import render, redirect, get_object_or_404
from .models import RequestOfferPost, Tag, Profile, Event
from users.models import User
from .forms import RequestOfferForm, ProfileForm, EventForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'obodo/homepage.html')

def add_request_offer(request):
    if request.method == 'POST':
        form = RequestOfferForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.image = request.FILES
            post.member = request.user
            post.save()
            return redirect(to='view_user_posts')
    else:
        form = RequestOfferForm()
    
    return render(request, 'obodo/add_request_offer.html', {
        'form': form,
    })

def view_user_posts(request):
    posts = request.user.posts.all()
    return render(request, 'obodo/view_user_posts.html', {
        "posts": posts,
    })

def view_all_posts(request):
    posts = RequestOfferPost.objects.all()
    return render(request, 'obodo/view_all_posts.html', {
        "posts": posts
    })

def post_detail(request, post_pk):
    post = get_object_or_404(RequestOfferPost, pk=post_pk)
    return render(request, "obodo/post_detail.html", {
        "post": post,
    })

def delete_post(request, post_pk):
    post = get_object_or_404(request.user.posts, pk=post_pk)

    if request.method == 'POST':
        post.delete()
        return redirect(to='view_user_posts')
    
    return render(request, 'obodo/delete_post.html', {
        "post": post,
    })

def add_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile(profile_pic = request.FILES['profile_pic'])
            profile.current_user = request.user
            profile.save()
            return redirect(to='view_user_profile', profile_pk=profile.pk)
    else:
        form = ProfileForm()
    
    return render(request, 'obodo/add_profile.html', {
        "form": form
    })

def view_user_profile(request, profile_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    return render(request, "obodo/view_user_profile.html", {
        "profile": profile
    })

def edit_user_profile(request, profile_pk):
    profile = get_object_or_404(request.user.profiles, pk=profile_pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(to='view_user_profile', profile_pk=profile.pk)
    else:
        form = ProfileForm()
    
    return render(request, "obodo/edit_user_profile.html", {
        "form": form,
        "profile": profile,
    })


# def view_post_comment(request, post_pk):
    
#     post = get_object_or_404(RequestOfferPost, pk=post_pk)
#     comments = post.comments.all()

#     return render(request, dataorsmth, {
#         "":.,

#     }
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = Event(event_pic = request.FILES['event_pic'])
            event.host = request.user
            event.save()
            return redirect(to='homepage')
    else:
        form = EventForm()
    
    return render(request, 'obodo/add_event.html', {
        "form": form,
    })

def view_event_page(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    return render(request, 'obodo/view_event_page.html', {
        "event": event
    })

def view_user_events(request):
    events = request.user.events.all()
    return render(request, 'obodo/view_user_events.html', {
        "events": events,
    })

def view_all_events(request):
    events = Event.objects.all()
    return render(request, 'obodo/view_all_events.html', {
        "events": events,
    })
