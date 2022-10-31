from django.contrib import admin
from bankingSolution.models import Lock2, Login
from bankingSolution.models import Sign
from bankingSolution.models import Credit
from bankingSolution.models import Withdraw
from bankingSolution.models import SendMoney
from bankingSolution.models import MobileRecharge
from bankingSolution.models import Operator
from bankingSolution.models import ChangePassword
# Register your models here.
admin.site.register(Login)
admin.site.register(Sign)
admin.site.register(Credit)
admin.site.register(Withdraw)
admin.site.register(SendMoney)
admin.site.register(MobileRecharge)
admin.site.register(Operator)
admin.site.register(ChangePassword)
admin.site.register(Lock2)
