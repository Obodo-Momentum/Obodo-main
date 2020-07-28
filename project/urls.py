"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from obodo import views as obodo_views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('home/', obodo_views.home, name='homepage'),
    path('obodo/add_request_offer/', obodo_views.add_request_offer, name='add_request_offer'),
    path('obodo/view_user_posts/', obodo_views.view_user_posts, name='view_user_posts'),
    path('obodo/post_detail/<int:post_pk>/', obodo_views.post_detail, name='post_detail'),
    path('obodo/delete_post/<int:post_pk>/', obodo_views.delete_post, name='delete_post'),
    path('', obodo_views.view_all_posts, name='landing_page'),
    path('obodo/view_user_profile/<int:user_pk>/', obodo_views.view_user_profile, name='view_user_profile'),
    path('obodo/add_profile/', obodo_views.add_profile, name='add_profile'),
    path('obodo/edit_user_profile/<int:user_pk>/', obodo_views.edit_user_profile, name='edit_user_profile'),
    path('obodo/add_event/', obodo_views.add_event, name="add_event"),
    path('obodo/view_event_page/<int:event_pk>/', obodo_views.view_event_page, name="view_event_page"),
    path('obodo/view_user_events/', obodo_views.view_user_events, name="view_user_events"),
    path('obodo/view_all_events/', obodo_views.view_all_events, name="view_all_events"),
    path('obodo/view_community_posts/', obodo_views.view_community_posts, name="view_community_posts"),
    path('obodo/view_comments/<int:post_pk>', obodo_views.view_comments, name='view_comments'),
    path('obodo/add_comment/', obodo_views.add_comment, name="add_comment")
]



if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
