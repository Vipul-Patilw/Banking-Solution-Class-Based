from Bank_Admin_Portal.models import Users_Account
from django import forms
import datetime
from django.core.exceptions import ValidationError
import re
class UserAccountCreateForm(forms.ModelForm):

	class Meta:
		model = Users_Account
		date = datetime.date.today()
		fields = '__all__'
		exclude = ('balance',)
	#	labels = {
#		'first_name': 'First Name',
#		
#		'last_name':'Last Name',
#		
#		'mobile_number':'Mobile Number',
#		
#		'username':'Username',
#			
#		'email':'Email',
#		
#		'gender':'Gender',
#	
#		'birthdate':'Birthdate'
#	}
		widgets = {
				'profile_pic':forms.FileInput(attrs={'id':"profile" , 'onchange':"loadProfile(event)", 'style':"display: none"}),
				'mobile_number':forms.TextInput(attrs={'type':'tel','maxlength':10,'id':'phone','onkeyup':'phoneValidation()'}),
				'account_number':forms.TextInput(attrs={'type':'tel','maxlength':16,'id':'a_num','onkeyup':'account_number_validation()'}),
				'card_number':forms.TextInput(attrs={'type':'tel','maxlength':16,'id':'c_num','onkeyup':'card_number_validation()',}),
				'expired_date':forms.TextInput(attrs={'type':'tel','maxlength':5,'id':'e_date'}),
				'cvv':forms.TextInput(attrs={'type':'tel','maxlength':3,'id':'cvv'}),
				'email':forms.EmailInput(attrs={'type':'email'}),
				'birthdate':forms.DateInput(attrs={'type':'date','max':date}),
				'signature':forms.FileInput(attrs={'id':"signature" , 'onchange':"loadSgnature(event)", 'style':"display: none"})}
	def clean(self):
		mobile_number= self.cleaned_data['mobile_number']
		email = self.cleaned_data['email']
		account_number = self.cleaned_data['account_number']
		card_number = self.cleaned_data['card_number']	
		
		if Users_Account.objects.filter(email=email):
						raise ValidationError({'email':"this email address already registered with us try different email address"})
			
						
		if Users_Account.objects.filter(mobile_number=mobile_number):
						raise ValidationError({'mobile_number':"this Mobile Number is already registered try another"})
						
		if Users_Account.objects.filter(account_number=account_number):
						raise ValidationError({'account_number':"this account number is already registered try another"})
				
		if Users_Account.objects.filter(card_number=card_number):
						raise ValidationError({'card_number':"this account number is already registered try another"})
					
		if len(mobile_number) != 10 and re.search(r"[A-Z]",mobile_number) and re.search(r"[a-z]",mobile_number) and re.search(r"[@_!#$%^&*()?/}{~:]",mobile_number):
				raise ValidationError({'mobile_number':"please enter a valid 10 digit number"})
		if len(account_number) != 16 and re.search(r"[A-Z]",account_number) and re.search(r"[a-z]",account_number) and re.search(r"[@_!#$%^&*()?/}{~:]",account_number):
				raise ValidationError({'account_number':"please enter a valid account number"})
		if len(card_number) != 16 and re.search(r"[A-Z]",card_number) and re.search(r"[a-z]",card_number) and re.search(r"[@_!#$%^&*()?/}{~:]",card_number):
				raise ValidationError({'card_number':"please enter a valid card number"})