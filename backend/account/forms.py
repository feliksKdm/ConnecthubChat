from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account


class RegistrationForm(UserCreationForm):

	class Meta:
		model = Account
		fields = ('username', 'password1', 'password2', )

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)


class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('username', 'password')

	def clean(self):
		if self.is_valid():
			username = self.cleaned_data['username']
			password = self.cleaned_data['password']
			if not authenticate(username=username, password=password):
				raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('username', 'profile_image')


    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)


    def save(self, commit=True):
        account = super(AccountUpdateForm, self).save(commit=False)
        account.username = self.cleaned_data['username']
        account.profile_image = self.cleaned_data['profile_image']
        account.hide_email = self.cleaned_data['hide_email']
        if commit:
            account.save()
        return account











