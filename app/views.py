from django.shortcuts import render,redirect
from django.contrib import messages
from . models import *
import random 
from django.db.models import Sum, Count
from django.db import connection
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings

def student_login(request):
	if request.session.has_key('user_id'):
		return render(request,'student_dashboard.html',{})
	else:
		if request.method == 'POST':
			name=request.POST.get('username')
			pwd=request.POST.get('password')
			user_exist=StudentDetail.objects.filter(university_no=name,password=pwd)
			if user_exist:
				request.session['name']= request.POST.get('username')
				a = request.session['name']
				sess = StudentDetail.objects.only('id').get(university_no=a).id
				request.session['user_id']= sess
				return redirect('student_dashboard')
			else:
				messages.success(request,'Invalid username or Password')
		return render(request,'student_login.html',{})
def student_dashboard(request):
	if request.session.has_key('user_id'):
		return render(request,'student_dashboard.html',{})
	else:
		return render(request,'student_login.html',{})
def register(request):
	if request.method == 'POST':
		Name = request.POST.get('uname')
		Adddress = request.POST.get('address')
		Mobile= request.POST.get('mobile')
		Email = request.POST.get('email')
		Password = request.POST.get('pwd')
		unum = request.POST.get('university_no')
		country = request.POST.get('country')
		city = request.POST.get('city')
		state = request.POST.get('state')
		student_exist = StudentDetail.objects.filter(university_no=unum)
		if student_exist:
			messages.success(request,'Register No Already Exsit')
		else:
			crt = StudentDetail.objects.create(student_name=Name,
			address=Adddress,phone_number=Mobile,password=Password,email_id=Email,university_no=unum,country=country,
			city=city,state=state)
			if crt:
				#recipient_list = [Email]
				#email_from = settings.EMAIL_HOST_USER
				#b = EmailMessage('Successfully Registered','University No:' + unum +  'Password:'+  Password,email_from,recipient_list).send()
				messages.success(request,'Registered Successfully')
	return render(request,'register.html',{})
def logout(request):
    try:
        del request.session['user_id']
        del request.session['name']
    except:
     pass
    return render(request, 'student_login.html', {})
def staff_login(request):
	if request.session.has_key('staff_id'):
		return render(request,'staff_dashboard.html',{})
	else:
		if request.method == 'POST':
			name=request.POST.get('username')
			pwd=request.POST.get('password')
			user_exist=StaffDetail.objects.filter(username=name,password=pwd)
			if user_exist:
				request.session['staff_name']= request.POST.get('username')
				a = request.session['staff_name']
				sess = StaffDetail.objects.only('id').get(username=a).id
				request.session['staff_id']= sess
				return redirect('staff_dashboard')
			else:
				messages.success(request,'Invalid username or Password')
		return render(request,'staff_login.html',{})
def staff_dashboard(request):
	if request.session.has_key('staff_id'):
		return render(request,'staff_dashboard.html',{})
	else:
		return render(request,'staff_login.html',{})
def staff_logout(request):
    try:
        del request.session['staff_id']
        del request.session['staff_name']
    except:
     pass
    return render(request, 'staff_login.html', {})
def choose_exam(request):
	if request.session.has_key('user_id'):
		a = Question_Category.objects.all()
		return render(request,'choose_exam.html',{'a':a})
	else:
		return render(request,'student_login.html',{})
def exam(request):
	if request.session.has_key('user_id'):
			uid = request.session['user_id']
			user_id = StudentDetail.objects.get(id=int(uid))
			cat_id = request.GET.get('category')
			category_id = Question_Category.objects.get(id=int(cat_id))
			category_name = Question_Category.objects.filter(id=int(cat_id))
			question = Quiz_Question.objects.filter(category=category_id)
			r_num =  random.randrange(20, 50, 3)
			num = r_num+int(cat_id)
			if request.method == 'POST':
				question_id = request.POST.getlist('question_id')
				ran_num = request.POST.get('random_num')
				ans = request.POST.getlist('answer')
				length = len(ans)
				for i in range(0,length):
					crt = Answer_Detail.objects.create(question=int(question_id[i]),rand_num=ran_num,ans=ans[i],user_id=user_id,category_id=category_id)
				if crt:
					return redirect('result')
			return render(request,'exam.html',{'question':question,'num':num,'category_name':category_name})
	else:
		return render(request,'student_login.html',{})

def result(request):
	if request.session.has_key('user_id'):
		num = request.POST.get('random_num')
		user_id = request.session['user_id']
		cursor = connection.cursor()
		tt = cursor.execute('''SELECT app_answer_detail.rand_num from app_answer_detail where 
		app_answer_detail.user_id_id= '%d' order by app_answer_detail.id DESC''' % (int(user_id)))
		row_user = cursor.fetchone()
		cat_name = Answer_Detail.objects.filter(rand_num=row_user[0])
		sql = ''' SELECT COUNT(a.ans) from app_quiz_question as q INNER JOIN app_answer_detail as a ON
		q.answer=a.ans where a.rand_num='%s' AND a.user_id_id= '%d' ''' % (row_user[0],int(user_id))
		post = cursor.execute(sql)
		row = cursor.fetchall()
		return render(request,'result.html',{'row':row,'cat_name':cat_name})
	else:
		return render(request,'student_login.html',{})
def exam_results(request):
	if request.session.has_key('user_id'):
		user_id = request.session['user_id']
		cursor = connection.cursor()
		sql = ''' SELECT COUNT(a.ans),c.name from app_quiz_question as q INNER JOIN app_answer_detail as a ON
		q.answer=a.ans INNER JOIN app_question_category as c ON a.category_id_id=c.id where a.user_id_id= '%d' GROUP BY a.rand_num''' % (int(user_id))
		post = cursor.execute(sql)
		row = cursor.fetchall()
		return render(request,'exam_results.html',{'row':row})
	else:
		return render(request,'student_login.html',{})
def update_profile(request):
	if request.session.has_key('user_id'):
		user_id = request.session['user_id']
		user_detail = StudentDetail.objects.filter(id=int(user_id))
		if request.method == 'POST':
			Name = request.POST.get('uname')
			Adddress = request.POST.get('address')
			Mobile= request.POST.get('mobile')
			Email = request.POST.get('email')
			unum = request.POST.get('university_no')
			country = request.POST.get('country')
			city = request.POST.get('city')
			state = request.POST.get('state')
			crt = StudentDetail.objects.filter(id=int(user_id)).update(student_name=Name,
			address=Adddress,phone_number=Mobile,email_id=Email,university_no=unum,country=country,
			city=city,state=state)
			if crt:
				messages.success(request,'Profile Updated Successfully')
		return render(request,'update_profile.html',{'user_detail':user_detail})
	else:
		return render(request,'student_login.html',{})
def update_staff_profile(request):
	if request.session.has_key('staff_id'):
		user_id = request.session['staff_id']
		user_detail = StaffDetail.objects.filter(id=int(user_id))
		if request.method == 'POST':
			Name = request.POST.get('uname')
			Adddress = request.POST.get('address')
			Mobile= request.POST.get('mobile')
			Email = request.POST.get('email')
			unum = request.POST.get('university_no')
			country = request.POST.get('country')
			city = request.POST.get('city')
			state = request.POST.get('state')
			crt = StaffDetail.objects.filter(id=int(user_id)).update(staff_name=Name,
			address=Adddress,phone_number=Mobile,email_id=Email,username=unum,country=country,
			city=city,state=state)
			if crt:
				messages.success(request,'Profile Updated Successfully')
		return render(request,'update_staff_profile.html',{'user_detail':user_detail})
	else:
		return render(request,'staff_login.html',{})
def students_detail(request):
	if request.session.has_key('staff_id'):
		row = StudentDetail.objects.all()
		return render(request,'students_detail.html',{'row':row})
	else:
		return render(request,'staff_login.html',{})
def all_students_result(request,pk):
	if request.session.has_key('staff_id'):
		cursor = connection.cursor()
		sql = ''' SELECT COUNT(a.ans),c.name from app_quiz_question as q INNER JOIN app_answer_detail as a ON
		q.answer=a.ans INNER JOIN app_question_category as c ON a.category_id_id=c.id   where a.user_id_id= '%d' GROUP BY a.rand_num''' %(pk)
		post = cursor.execute(sql)
		row = cursor.fetchall()
		return render(request,'all_students_result.html',{'row':row})
	else:
		return render(request,'staff_login.html',{})

def material(request,pk):
	row = Study_Material.objects.filter(category=pk)
	return render(request,'material.html',{'row':row,'pk':pk})
def category(request):
	row = Question_Category.objects.all()
	return render(request,'category.html',{'row':row})
