from django.shortcuts import render, redirect, get_object_or_404
from .models import RequestOfferPost, Tag, Event, Organization, Member, Profile
from users.models import User
from .forms import RequestOfferForm, EventForm, OrganizationForm, MemberForm, ProfileForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from registration.backends.simple.views import RegistrationView
from django.urls import reverse_lazy

# Create your views here.

class MyRegistrationView(RegistrationView):
    success_url = reverse_lazy('homepage')

def add_request_offer(request):
    if request.method == 'POST':
        form = RequestOfferForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.image = request.FILES
            post.member = request.user
            post.community = request.user.community
            post.save()
            post.set_tag_names(form.cleaned_data['tag_names'])
            return redirect(to='view_user_posts')
    else:
        form = RequestOfferForm()
    return render(request, 'obodo/add_request_offer.html', {
        'form': form,
    })

def search_posts(request):
    query = request.GET.get('q')

    if query is not None:
        posts = RequestOfferPost.objects.filter(Q(title__icontains=query))
    else:
        posts = None
    
    return render(request, 'obodo/search_posts.html', {
        'query': query,
        'posts': posts,
    })

def view_user_posts(request):
    posts = request.user.posts.all()
    return render(request, 'obodo/view_user_posts.html', {
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
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect(to='view_user_profile', user_pk=user.pk)
    else:
        form = ProfileForm()
    
    return render(request, "obodo/edit_user_profile.html", {
        "form": form,
    })


def view_comments(request, post_pk):
    if request.method == "GET":
        post = get_object_or_404(RequestOfferPost, pk=post_pk)
        comments = post.comments.all().values()
        
        return JsonResponse(list(comments), safe=False)

@ensure_csrf_cookie
def add_comment(request, post_pk):
    post = get_object_or_404(RequestOfferPost, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.original_post = post
            comment.commenter = request.user
            comment.save()
            
            return JsonResponse(comment, status=201)
    #         return redirect(to='post_detail', post_pk=post.pk)
    # else:
    #     form = CommentForm()
    # return render(request, "obodo/add_comment.html", {
    #     "form": form,
    #     "post": post,
    # })


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = Event(event_pic = request.FILES['event_pic'])
            event.host = request.user
            event = form.save()
            return redirect(to='view_user_events')
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

def search_events(request):
    query = request.GET.get('q')

    if query is not None:
        events = Event.objects.filter(Q(event_title__icontains=query))
    else:
        events = None
    
    return render(request, 'obodo/search_events.html', {
        'query': query,
        'events': events,
    })

def view_community_posts(request):
    community = request.user.community
    posts = RequestOfferPost.objects.filter(community = community)

    return render(request, 'obodo/homepage.html', {
        "posts": posts
    })


def add_organization(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST, request.FILES)
        if form.is_valid():
            organization = form.save(commit=False)
            organization.creator = request.user
            form.save()
            return redirect(to='view_organization', organization_pk=organization.pk)
    else:
        form = OrganizationForm()
    return render(request, 'obodo/add_organization.html', {
        "form": form,
    })

def view_organization(request, organization_pk):
    organization = get_object_or_404(Organization.objects.all(), pk=organization_pk)
    return render(request, 'obodo/view_organization.html', {
        'organization': organization,
    })

def browse_organizations(request):
    organizations = Organization.objects.all()
    return render(request, 'obodo/browse_organizations.html', {
        "organizations": organizations
    })

def search_organizations(request):
    query = request.GET.get('q')

    if query is not None:
        organizations = Organization.objects.filter(Q(name__icontains=query))
    else:
        organizations = None
    
    return render(request, 'obodo/search_organizations.html', {
        'query': query,
        'organizations': organizations,
    })

def add_member(request, organization_pk):
    organization = get_object_or_404(Organization.objects.all(), pk=organization_pk)

    if request.method == 'POST':
        form = MemberForm(data=request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.organization = organization
            member.save()
            return redirect(to='view_organization', organization_pk=organization.pk)
    else:
        form = MemberForm()
    
    return render(request, 'obodo/add_member.html', {
        "form": form,
        "organization": organization,
    })

def view_tag(request, tag_name):
    tag = get_object_or_404(Tag, tag=tag_name)
    posts = tag.posts.all()
    
    return render(request, 'obodo/tag_detail.html', {
        'tag': tag,
        'posts': posts,
    })

def list_tags(request):
    tags = Tag.objects.order_by('posts')
    return render(request, 'obodo/list_tags.html', {
        'tags': tags,
    })

def search_tags(request):
    query = request.GET.get('q')

    if query is not None:
        tags = Tag.objects.filter(Q(tag__icontains=query))
    else:
        tags = None
    
    return render(request, 'obodo/search_tags.html', {
        'query': query,
        'tags': tags,
    })

def search_category(request):
    category = request.GET.get('category')

    if category is not None:
        posts = RequestOfferPost.objects.filter(Q(category__icontains=category))
    else:
        posts = None
    
    return render(request, 'obodo/search_category.html', {
        'category': category,
        'posts': posts,
    })