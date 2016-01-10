# from main.models import Hairstyle 
from django import forms

from django.core.validators import validate_email

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div
from crispy_forms.bootstrap import FormActions


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True, max_length=15, help_text='Please include a proper telephone number so I can respond to your inquiry, thank you :)')
    email = forms.CharField(required=True, help_text='Please include a proper email address so I can respond to your inquiry, thank you :)' )
    message = forms.CharField(required=True, initial='', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/contact_view/'
        self.helper.layout = Layout(
                Div('name', css_class='col-md-12'),
                Div('email', css_class='col-md-12'),
                Div('phone', css_class='col-md-12'),
                Div('message', css_class='col-md-12'),
            )
        self.helper.layout.append(
            FormActions(
                Submit('submit',  'Submit', css_class="btn-default")
                )
            )
        self.fields['name'].required = True
        self.fields['email'].required = True
        self.fields['phone'].required = False
        
        self.fields['message'].required = True
        

            # require_all_fields = False

