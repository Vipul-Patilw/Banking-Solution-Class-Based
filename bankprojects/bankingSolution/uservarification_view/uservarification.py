from django.views.generic.edit import CreateView
from Bank_Admin_Portal.models import Users_Account
from django.contrib.messages.views import  SuccessMessageMixin
from bankingSolution.forms import UserVerificationForm

from django.contrib.auth.models import User

class UserVerification(CreateView):
#SuccessMessageMixin):
		template_name = 'registration/user_verification.html'
		form_class = UserVerificationForm
	#	success_message = "Welcome<strong> %,<%(first _name) %(last_name) </strong> Your account is created sucsessfully."
		success_url = 'account/login'
		def form_valid(self, form):
			account_number= form.cleaned_data['account_number']
			password= form.cleaned_data['password']
			myuser = User.objects.create_user(account_number,account_number,password)
			#myuser.is_active = False
			myuser.save()
			return super(UserVerification, self).form_valid(form)