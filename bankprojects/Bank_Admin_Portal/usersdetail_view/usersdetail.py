from Bank_Admin_Portal.models import Users_Account
from django.views.generic import ListView

class UsersDetail(ListView):
		model = Users_Account
		template_name = 'usersdetail.html'
	#	paginate_by = 10
		context_object_name = 'users_list'
		