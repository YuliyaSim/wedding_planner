from django.forms import ModelForm

from guests.models import Guest


class SendEmailForm(ModelForm):
    class Meta:
        model = Guest
        fields = ('email',)

