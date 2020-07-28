from django.shortcuts import render, redirect, get_object_or_404
from .models import RequestOfferPost, Tag, Event, Organization, Member
from users.models import User
from .forms import RequestOfferForm, EventForm, OrganizationForm, MemberForm
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
            post.community = request.user.community
            post.save()
            return redirect(to='view_user_posts')
    else:
        form = RequestOfferForm()
    
    return render(request, 'obodo/add_request_offer.html', {
        'form': form,
    })

def view_user_posts(request):
    posts = request.user.posts.all()
    return render(request, 'obodo/view_user_profile.html', {
        "posts": posts,
    })

def view_all_posts(request):
    posts = RequestOfferPost.objects.all()
    return render(request, 'obodo/landing_page.html', {
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
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect(to='view_user_profile', user_pk=user.pk)
    else:
        form = ProfileForm()
    
    return render(request, 'obodo/add_profile.html', {
        "form": form
    })


def view_user_profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    posts = user.posts.all()
    return render(request, "obodo/view_user_profile.html", {
        "user": user,
        "posts": posts,
    })

def edit_user_profile(request, user_pk):
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(to='view_user_profile', user_pk=user.pk)
    else:
        form = ProfileForm()
    
    return render(request, "obodo/edit_user_profile.html", {
        "form": form,
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
            event = form.save()
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


def view_community_posts(request):
    community = request.user.community
    posts = RequestOfferPost.objects.filter(community = community)

    return render(request, 'obodo/homepage.html', {
        "posts":posts
    })

def add_organization(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST, request.FILES)
        if form.is_valid():
            org = Organization(picture = request.FILES['picture'])
            org.creator = request.user
            org = form.save()
            return redirect(to='view_organization')
    else:
        form = OrganizationForm()
    
    return render(request, 'obodo/add_organization.html', {
        "form": form,
    })

def view_organization(request, org_pk):
    creator = request.user
    community = request.user.community
    organization = get_object_or_404(Organization, pk=org_pk)
    return render(request, 'obodo/view_organization.html', {
        'organization': organization,
        "creator": creator,
        "community": community,
    })
