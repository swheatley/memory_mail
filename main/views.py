from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

from main.models import CustomUser
from main.forms import ContactForm

# from apiclient.discovery import build
# from apiclient import errors

from django.contrib.auth.decorators import login_required


def index(request):
    context = {}

    return render_to_response('index.html', context, context_instance=RequestContext(request))


def navbar(request):
    context = {}
    return render_to_response('navbar.html', context, context_instance=RequestContext(request))


def dashboard(request):
    context = {}
    return render_to_response('dashboard.html', context, context_instance=RequestContext(request))

# dashboard views


def blog(request):
    context = {}
    return render_to_response('dashboard/blog.html', context, context_instance=RequestContext(request))


def book(request):
    context = {}
    return render_to_response('dashboard/book.html', context, context_instance=RequestContext(request))


def memories(request):
    context = {}
    return render_to_response('dashboard/memories.html', context, context_instance=RequestContext(request))


def upgrade(request):
    context = {}
    return render_to_response('dashboard/upgrade.html', context, context_instance=RequestContext(request))


@login_required
def contact_view(request):
    context = {}

    form = ContactForm()

    context['form'] = form

    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        context['form'] = form
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(' WEBSITE MESSAGE FROM %s' % name,
                      'Message from %s, %s, %s' % (name, email, phone) + '\n\n' + message,
                      email,
                      [settings.EMAIL_HOST_USER],
                      fail_silently=False
                      )
            
            messages.success(request, 'Message has been sent!')
            return HttpResponseRedirect('/message')
        else:
            context['message'] = form.errors
    elif request.method == 'GET':
        form = ContactForm()
        context['form'] = form
       
    return render_to_response('contact_view.html', context, context_instance=RequestContext(request))
