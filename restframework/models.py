from django.db import models

# Create your models here.
class Company(models.Model):
	company_type=[
		('IT','IT'),
		('Non-IT','Non-IT'),
		('Manufacturing','Manufacturing')
	]
	company_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	location=models.CharField(max_length=50)
	about=models.TextField()
	company_type=models.CharField(max_length=100,choices=company_type)
	added_data=models.DateTimeField(auto_now=True)
	active=models.BooleanField(default=True)


	def __str__(self):
		return self.name + self.location 


class Employee(models.Model):
	pos=[
		('Manager','Manager'),
		('Software Developer','SDE'),
		('Project Leader','PL')
	]
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	address=models.CharField(max_length=50)
	phone=models.CharField(max_length=10)
	about=models.TextField()
	position=models.CharField(max_length=50,choices=pos)
	company=models.ForeignKey(Company, on_delete=models.CASCADE)

	def __str__(self):
		return self.name + self.position

