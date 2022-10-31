import  datetime
from django.contrib.auth.models import User
from bankingSolution.models import SendMoney
def dates(request):
    date=datetime.datetime.now()
    date_without_time = datetime.date.today()
    # moneyrecivedcount = SendMoney.objects.filter(date__icontains=date_without_time).filter(account_number=User.username).all()
    return {'date':date,'date_without_time':date_without_time}#,'moneyrecivedcount':moneyrecivedcount}
