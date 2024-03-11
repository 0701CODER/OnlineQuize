from django.db import models

class StudentDetail(models.Model):
	student_name = models.CharField('Student Name', max_length=255)
	email_id = models.EmailField('Email Id', max_length=255)
	phone_number = models.CharField('Mobile Number', max_length=50,null=True,blank=True)
	address = models.TextField('Address',null=True,blank=True)
	country = models.CharField('Country', max_length=100,default='India')
	state = models.CharField('State', max_length=100,default='Tamil Nadu')
	city = models.CharField('City', max_length=100,null=True,blank=True)
	university_no = models.CharField('University No', max_length=100, unique=True)
	password = models.CharField('Password',max_length=30)
	def __str__(self):
		return self.student_name
class StaffDetail(models.Model):
	staff_name = models.CharField('Staff Name', max_length=255)
	email_id = models.EmailField('Email Id', max_length=255)
	phone_number = models.CharField('Mobile Number', max_length=50,null=True,blank=True)
	address = models.TextField('Address',null=True,blank=True)
	country = models.CharField('Country', max_length=100,default='India')
	state = models.CharField('State', max_length=100,default='Tamil Nadu')
	city = models.CharField('City', max_length=100,null=True,blank=True)
	username = models.CharField('Username', max_length=100, unique=True)
	password = models.CharField('Password',max_length=30)
	def __str__(self):
		return self.staff_name
class Question_Category(models.Model):
	name = models.CharField('Category Name', max_length=255)
	def __str__(self):
		return self.name
class Study_Material(models.Model):
	category = models.ForeignKey(Question_Category, on_delete=models.CASCADE,null=True)
	title = models.CharField('Title', max_length=255)
	content = models.TextField('Content', max_length=3000)
	def __str__(self):
		return self.title
class Quiz_Question(models.Model):
	category = models.ForeignKey(Question_Category, on_delete=models.CASCADE,null=True)
	question = models.CharField('Question', max_length=255)
	option1 = models.CharField('Option1', max_length=255)
	option2 = models.CharField('Option2', max_length=255)
	option3 = models.CharField('Option3', max_length=255)
	option4 = models.CharField('Option4', max_length=255)
	answer = models.CharField('Answer', max_length=255)
	def __str__(self):
		return self.question
class Answer_Detail(models.Model):
	question = models.IntegerField(null=True)
	rand_num = models.CharField(max_length=255)
	ans = models.CharField('Answer', max_length=255)
	user_id = models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
	category_id = models.ForeignKey(Question_Category, on_delete=models.CASCADE,null=True)
	def __str__(self):
		return self.ans

