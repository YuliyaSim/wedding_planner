from django.forms import Form, CharField, EmailField, PasswordInput, TextInput, EmailInput, ChoiceField, RadioSelect, \
    DateField, DateInput, TimeField, TimeInput, ModelForm

from create_wed.models import ContactUs


class SignUpForm(Form):
    username = CharField(widget=TextInput(attrs={
        'class': 'form-control w-75'
    }))
    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control w-75'
    }))
    email = EmailField(label='Email', widget=EmailInput(attrs={
        'class': 'form-control w-75'
    }))
    first_name = CharField(label='First Name', widget=TextInput(attrs={
        'class': 'form-control w-75'
    }))
    last_name = CharField(label='Last Name', widget=TextInput(attrs={
        'class': 'form-control w-75'
    }))



class LoginForm(Form):
    username = CharField(widget=TextInput(attrs={
        'class': 'form-control w-75'
    }))
    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control w-75'
    }))


GENDER_CHOICES = [
    ('Female', 'Female'),
    ('Male', 'Male'),
]


class CreateWeddingForm(Form):
    partner1_gender = ChoiceField(label='Personal', required=True, widget=RadioSelect(
                    attrs={'class': 'Radio'}), choices=(GENDER_CHOICES))
    partner1_email = EmailField(label='Email', widget=EmailInput(attrs={
        'class': 'form-control w-75'}))
    partner2_gender = ChoiceField(label='Partner', required=True, widget=RadioSelect(
                    attrs={'class': 'Radio'}), choices=(GENDER_CHOICES))
    partner2_email =EmailField(label='Email', widget=EmailInput(attrs={
        'class': 'form-control w-75'}))
    wedding_name = CharField(label='Wedding Name', widget=TextInput(attrs={
        'class': 'form-control w-75'}))
    wedding_date = DateField(label='Wedding Date', widget=DateInput(format="%m/%d/%Y"),initial='MM/DD/YYYY')
    wedding_time = TimeField(label='Wedding Time', widget=TimeInput(format='%H:%M'))


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control w-75'}),
            'email': TextInput(attrs={'class': 'form-control w-75'}),
            'message': TextInput(attrs={'class': 'form-control w-75'}),
        }
