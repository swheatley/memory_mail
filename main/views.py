from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

# from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    context = {}

    return render_to_response('index.html', context, context_instance=RequestContext(request))


# #login_required
# def contact_view(request):
#     context = {}

#     form = ContactForm()

#     context['form'] = form

#     if request.method == 'POST':
#         form = ContactForm(request.POST or None)
#         context['form'] = form
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             phone = form.cleaned_data['phone']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']

#             send_mail(' WEBSITE MESSAGE FROM %s' % name,
#                       'Message from %s, %s, %s' % (name, email, phone) + '\n\n' + message,
#                       email,
#                       [settings.EMAIL_HOST_USER],
#                       fail_silently=False
#                       )
            
#             messages.success(request, 'Message has been sent!')
#             return HttpResponseRedirect('/message')
#         else:
#             context['message'] = form.errors
#     elif request.method == 'GET':
#         form = ContactForm()
#         context['form'] = form
       
#     return render_to_response('contact_view.html', context, context_instance=RequestContext(request))
