from django.db import models

# Create your models here.
gender=[('','Select Gender'),('male','Male'),('female','Female')]

class SuperUserRegistration(models.Model):
	
	profile_pic = models.ImageField(upload_to= "Admin_Portal/profiles",blank=True)

	first_name = models.CharField(max_length=122)
	
	last_name = models.CharField(max_length=122)
	
	mobile_number= models.CharField(max_length=122)
	
	username= models.CharField(max_length=122)
		
	email= models.CharField(max_length=122)
	
	gender = models.CharField(max_length=122,choices=gender)
	
	class Meta:
		db_table= "Bank_Admin_Portal_user_registration"
		
	def __str__(self):
		return self.first_name 
		
class Staff(models.Model):
	
	first_name = models.CharField(max_length=122)
	
	last_name = models.CharField(max_length=122)
	
	username= models.CharField(max_length=122)
		
	email= models.CharField(max_length=122)
		
	def __str__(self):
		return self.first_name 
		
class Admin(models.Model):
	
	first_name = models.CharField(max_length=122)
	
	last_name = models.CharField(max_length=122)
	
	username= models.CharField(max_length=122)
		
	email= models.CharField(max_length=122)

		
	def __str__(self):
		return self.first_name 

gender=[('','Select Gender'),('male','Male'),('female','Female')]
city=[('','Select City'),('mumbai','Mumbai'),('pune','Pune'),('delhi','Delhi')]	
bank=[('','Select Bank'),('State Bank Of India','State Bank Of India'),('Kotak Mahindra','Kotak Mahindra'),('Bank Of Maharashtra','Bank Of Maharashtra')]		
class Users_Account(models.Model):
	
	holder_name = models.CharField(max_length=122)
	
	bank_name = models.CharField(max_length=122,choices=bank)
	
	mobile_number= models.CharField(max_length=122)
	
	account_number= models.CharField(max_length=122)
	
	card_number= models.CharField(max_length=122)
	expired_date= models.CharField(max_length=122,default='')
	cvv = models.CharField(max_length=122,default='')
	
	email= models.CharField(max_length=122)
	
	gender = models.CharField(max_length=122,choices=gender)
	
	city = models.CharField(max_length=122,choices=city)

	balance = models.FloatField(default=0.00)

	birthdate = models.DateField()
	
	signature = models.ImageField(upload_to= "Admin_Portal/signatures",blank=True)

	profile_pic = models.ImageField(upload_to= "Admin_Portal/users_profiles",blank=True)
	
	def __str__(self):
		return self.holder_name

