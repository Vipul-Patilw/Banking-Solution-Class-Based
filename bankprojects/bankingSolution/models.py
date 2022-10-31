
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
gender=[('','Select Gender'),('male','Male'),('female','Female')]
city=[('','Select City'),('mumbai','Mumbai'),('pune','Pune'),('delhi','Delhi')]

class Login(models.Model):
	
	full_name = models.CharField(max_length=122)
	
	bank_name = models.CharField(max_length=122)
	
	mobile_number= models.CharField(max_length=122)
	
	account_number= models.CharField(max_length=122)
	
	card_number= models.CharField(max_length=122)
	
	email= models.CharField(max_length=122)

	password= models.CharField(max_length=122)
	
	gender = models.CharField(max_length=122)
	
	city = models.CharField(max_length=122)

	balance = models.FloatField(default=0.00)

	birthdate = models.DateField()
	
	
	
	def __str__(self):
		return self.full_name
		
class UserVerificationModel(models.Model):
	account_number = models.CharField(max_length=122)
	card_number = models.CharField(max_length=122)
	expired_date = models.CharField(max_length=122)
	cvv = models.CharField(max_length=122)



class Sign(models.Model):
	name  = models.CharField(max_length=122)
	Loginpassword = models.CharField(max_length=122)
	def __str__(self):
		return self.name
	
class Chat(models.Model):
	email  = models.CharField(max_length=122)
	msg = models.CharField(max_length=122)
	    
	    
class Credit(models.Model):
	amount = models.CharField(max_length=122)
	email = models.CharField(max_length=122)
	date = models.CharField(max_length=122,default="")
	def __str__(self):
		return self.amount
		
		
class Withdraw(models.Model):
	amount2 = models.CharField(max_length=122)
	email = models.CharField(max_length=122)
	password = models.CharField(max_length=122)
	date = models.CharField(max_length=122,default="")
	def __str__(self):
		return self.amount2
		
class SendMoney(models.Model):
		note = models.CharField(max_length=122)
		my_account_number = models.CharField(max_length=122)
		account_number= models.CharField(max_length=122)
		confirm_number= models.CharField(max_length=122)
		amount= models.CharField(max_length=122)
		Bank = models.CharField(max_length=122)
		name = models.CharField(max_length=122,default=0)
		email = models.CharField(max_length=122,default="")
		date = models.CharField(max_length=122,default="")
		holder_name = models.CharField(max_length=122,default=0)
		def __str__(self):
			return self.amount

class MobileRecharge(models.Model):
		amount= models.CharField(max_length=122)
		password = models.CharField(max_length=122)
		email = models.CharField(max_length=122)
		date = models.CharField(max_length=122,default="")
		def __str__(self):
			return self.amount
	
class Operator(models.Model):
		operator = models.CharField(max_length=122)
		mobile_number = models.CharField(max_length=122)
		def __str__(self):
			return self.mobile_number

class ChangePassword(models.Model):
		old_password = models.CharField(max_length=122)
		new_password1= models.CharField(max_length=122)
		newpassword2 = models.CharField(max_length=122)

class Balance(models.Model):
	account_number = models.CharField(max_length=122)
	email = models.CharField(max_length=122)
	pin1 = models.CharField(max_length=122)
	
class Lock2(models.Model):
	email = models.CharField(max_length=122)
	pin1 = models.CharField(max_length=122)
	pin2 = models.CharField(max_length=122)
	account_number = models.CharField(max_length=122,default="")


class Lock(models.Model):
	email = models.CharField(max_length=122)
	pin1 = models.CharField(max_length=122)
	
class BankDetails(models.Model):
	email1 = models.CharField(max_length=122)
	pin1 = models.CharField(max_length=122)



class ChangePin(models.Model):
	email = models.CharField(max_length=122)
	old_pin = models.CharField(max_length=122)
	new_pin1 = models.CharField(max_length=122)
	new_pin2 = models.CharField(max_length=122)