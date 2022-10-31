from Bank_Admin_Portal.models import Users_Account
from bankingSolution.models import UserVerificationModel
import re
from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
class UserVerificationForm(forms.ModelForm):
	password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'type':'password','class':'form-control', 'id':'validationCustom03'}))
	
	confirm_password = forms.CharField(label=' Re-enter Password',widget=forms.PasswordInput(attrs={'type':'password','class':'form-control', 'id':'validationCustom03'}))
	
	class Meta:
		model = UserVerificationModel
		fields = '__all__'
		labels = { 
		'account_number': 'Account Nubmber',
		'card_number':'Card Number',
		'expired_date': 'Expired Date',
		'cvv':'Cvv'
		
	}
		widgets = {
				'account_number':forms.TextInput(attrs={'type':'tel','class':'form-control', 'id':'validationCustom01','onkeyup':'account_number_validation()', 'autocomplete':'off'}),
				'card_number':forms.TextInput(attrs={'type':'tel','onkeyup':'card_number_validation()', 'autocomplete':'off','class':'form-control', 'id':'validationCustom02'}),
				'expired_date':forms.TextInput(attrs={'type':'tel', 'autocomplete':'off','class':'form-control', 'id':'validationCustom04'}),
				'cvv':forms.TextInput(attrs={'type':'tel', 'autocomplete':'off','class':'form-control', 'id':'validationCustom05'}),			
			}

	def clean(self):
			account_number= self.cleaned_data['account_number']
			card_number= self.cleaned_data['card_number']
			expired_date = self.cleaned_data['expired_date']
			cvv =  self.cleaned_data['cvv']
			password = self.cleaned_data['password']
			password2 = self.cleaned_data['confirm_password']
			try:
				user_account= Users_Account.objects.get(account_number=account_number)
			except:
				raise ValidationError({'account_number':"The details you entered was incorrect ! please enter your correct bank details"})
			if User.objects.filter(username=account_number):
				raise ValidationError({'account_number':"This account is already created, go to login page to login In"})		
			
			if user_account.card_number==card_number and user_account.expired_date==expired_date and user_account.cvv==cvv:
						pass
			else:
							raise ValidationError({'account_number':"The details you entered was incorrect ! please enter your correct bank details "})
				
			if len(password)>=6 and re.search(r"[A-Z]",password) and re.search(r"[a-z]",password) and re.search(r"[@_!#$%^&*()?/}{~:]",password)and re.search(r"[0-9]",password):
					pass
			else:
					raise ValidationError({'password':"password should be at least 6 character long. contain both uppercase and lowercase character, at least one alpha numeric and one special charecter  (eg:Test@123)"})
			if password != password2:
					raise ValidationError({'confirm_password':"confirm password doesn't matched with the password"})

				
				