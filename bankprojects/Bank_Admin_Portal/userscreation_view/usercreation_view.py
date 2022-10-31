from Bank_Admin_Portal.models import Users_Account
from django.views.generic.edit import CreateView
from Bank_Admin_Portal.forms import UserAccountCreateForm

class UserAccountCreate(CreateView):

		model = Users_Account
		template_name = 'users_account.html'
		form_class = UserAccountCreateForm	
		success_url = 'home'