from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django import forms

class SignupForm(UserCreationForm):


    lecture_url = forms.CharField(strip=False, required=False)
    github_original = forms.CharField(strip=False, required=False)
    github1 = forms.CharField(strip=False, required=False)
    github2 = forms.CharField(strip=False, required=False)
    github3 = forms.CharField(strip=False, required=False)
    github4 = forms.CharField(strip=False, required=False)
    email = forms.CharField(strip=False, required=False)
    phone = forms.CharField(strip=False, required=False)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields

    def save(self):
        user = super().save()
        profile = Profile.objects.create(
            user = user,
            phone = self.cleaned_data['phone'],
            lecture_url = self.cleaned_data['lecture_url'],
            email = self.cleaned_data['email'],
            github_original = self.cleaned_data['github_original'],
            github1 = self.cleaned_data['github1'],
            github2 = self.cleaned_data['github2'],
            github3 = self.cleaned_data['github3'],
            github4 = self.cleaned_data['github4'],
		)
        return user


from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
        widget=forms.TextInput(attrs={'class': 'mdl-textfield__input', 'type' :'text', 'id' : 'username'}))
    password = forms.CharField(label="Password", max_length=30,
        widget=forms.TextInput(attrs={'class': 'mdl-textfield__input', 'type' :'password', 'id' : 'password'}))
