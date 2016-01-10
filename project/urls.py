"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static
from main import views
from checkout import views 
from django.contrib.auth import views as auth_views
from checkout.views import SubscribeView, SuccessView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^subscribe/$', SubscribeView.as_view(), name='subscribe'),
    url(r'^thank_you/$', SuccessView.as_view(), name='thank_you'),
    # Design Views
    url(r'^$', 'main.views.index', name='index'),
    url(r'^navbar/$', 'main.views.navbar', name='navbar'),
    url(r'^checkout/$', 'checkout.views.checkout', name='checkout'),

    # Aullauth
    # url(r'^accounts/', include('allauth.urls')),

    # Django Registration Redux
    url(r'^accounts/', include('registration.backends.default.urls')),

    # #url(r'^password/change/$',
    #     auth_views.password_change,
    #     name='password_change'),
    # url(r'^password/change/done/$',
    #     auth_views.password_change_done,
    #     name='password_change_done'),
    # url(r'^password/reset/$',
    #     auth_views.password_reset,
    #     name='password_reset'),
    # url(r'^password/reset/done/$',
    #     auth_views.password_reset_done,
    #     name='password_reset_done'),
    # url(r'^password/reset/complete/$',
    #     auth_views.password_reset_complete,
    #     name='password_reset_complete'),
    # url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    #     auth_views.password_reset_confirm,
    #     name='password_reset_confirm'),

    # Forms
    url(r'^contact_view/$', 'main.views.contact_view'),
    
    # Social OAuth
    url('', include('social.apps.django_app.urls', namespace='social')),


    # Stripe Payments
    url(r'^payments/', include('djstripe.urls', namespace="djstripe"))
]
