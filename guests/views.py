from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import CheckboxSelectMultiple, CheckboxInput, DateInput
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from funky_sheets.formsets import HotView

from guests import forms
from guests.models import Guest

from wedding_planner.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, send_mass_mail



class UpdateManualGuestListView(HotView, LoginRequiredMixin):
    # Define model to be used by the view
    model = Guest
    # Define template
    template_name = 'guests/hot/update_manual_guests_list.html'
    # Define custom characters/strings for checked/unchecked checkboxes
    checkbox_checked = 'yes'  # default: true
    checkbox_unchecked = 'no'  # default: false
    # Define prefix for the formset which is constructed from Handsontable spreadsheet on submission
    prefix = 'table'
    # Define success URL
    success_url = reverse_lazy('guests:manual_guest_list')
    # Define fields to be included as columns into the Handsontable spreadsheet
    fields = (
        'id',
        'first_name',
        'last_name',
        'email' ,
        'invited_by',
        'save_the_date',
        'invitation',
        'response',
        'attending',
        'children',
        'dietary_restrictions',
        'table_number',
        'gift_description',
        'thank_you_sent',
        'notes',
    )
    # Define extra formset factory kwargs
    factory_kwargs = {
        'widgets': {
            'release_date': DateInput(attrs={'type': 'date'}),
            'genre': CheckboxSelectMultiple(),
            'parents_guide': CheckboxInput(),
        }
    }
    # Define Handsontable settings as defined in Handsontable docs
    hot_settings = {
        'contextMenu': 'true',
        'autoWrapRow': 'true',
        'rowHeaders': 'true',
        'search': 'true',
        'licenseKey': 'non-commercial-and-evaluation',
        # When value is dictionary don't wrap it in quotes
        'headerTooltips': {
            'rows': 'false',
            'columns': 'true'
        },
        # When value is list don't wrap it in quotes
        'dropdownMenu': [
            'remove_col',
            '---------',
            'make_read_only',
            '---------',
            'alignment'
        ]
    }


class ManualGuestListView(UpdateManualGuestListView, LoginRequiredMixin):
    template_name = 'guests/hot/manual_guests_list.html'
    action = 'update'
    button_text = 'Update'

    def get_queryset(self):
        return Guest.objects.all()


#Send Email
@login_required
def send_email(request):
    email = forms.SendEmailForm
    if request.method == 'POST':
        email = forms.SendEmailForm(request.POST)
        subject = 'Save the Date'
        message = 'We are honored to Invite you to our wedding'
        recipient_list = [Guest.objects.values('email')]
        #recipient = str(email['email'].value())
        send_mass_mail(subject, message, EMAIL_HOST_USER, [recipient_list], fail_silently=False)
        return redirect(reverse('guests:manual_guest_list'))
    return render(request, 'guests/send_email.html', {'form': email})
