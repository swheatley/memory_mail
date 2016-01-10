from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

# from main.models import CustomUser
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


# # def build_service(credentials):
#     # Build a Gmail service object.

#     # Args:
#     #     credentials: OAuth 2.0 credentials.

#     #   Returns:
#     #     Gmail service object.
 
#     http = httplib2.Http()
#     http = credentials.authorize(http)
#     return build('gmail', 'v1', http=http)


# def ListMessages(service, user, query=''):
#     #   # Gets a list of messages.

#     # Args:
#     #   service: Authorized Gmail API service instance.
#     #   user: The email address of the account.
#     #   query: String used to filter messages returned.
#     #          Eg.- 'label:UNREAD' for unread Messages only.

#     # Returns:
#     #   List of messages that match the criteria of the query. Note that the
#     #   returned list contains Message IDs, you must use get with the
#     #   appropriate id to get the details of a Message.
  
#     try:
#         response = service.users().messages().list(userId=user, q=query).execute()
#         messages = response['messages']

#         while 'nextPageToken' in response:
#             page_token = response['nextPageToken']
#             response = service.users().messages().list(userId=user, q=query, pageToken=page_token).execute()
                                                
#         messages.extend(response['messages'])

#         return messages
#     except errors.HttpError, error:
#         print 'An error occurred: %s' % error
#         if error.resp.status == 401:
#             # Credentials have been revoked.
#             # TODO: Redirect the user to the authorization URL.
#             raise NotImplementedError()


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
