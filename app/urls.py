from django.urls import path
from . import views
urlpatterns = [
path('',views.student_login,name="student_login"),
path('student_dashboard/',views.student_dashboard,name="student_dashboard"),
path('register/',views.register,name="register"),
path('logout/',views.logout,name="logout"),
path('staff_login/',views.staff_login,name="staff_login"),
path('staff_dashboard/',views.staff_dashboard,name="staff_dashboard"),
path('staff_logout/',views.staff_logout,name="staff_logout"),
path('choose_exam/',views.choose_exam,name="choose_exam"),
path('exam/',views.exam,name="exam"),
path('result/',views.result,name="result"),
path('exam_results/',views.exam_results,name="exam_results"),
path('update_profile/',views.update_profile,name="update_profile"),
path('update_staff_profile/',views.update_staff_profile,name="update_staff_profile"),
path('all_students_result/<int:pk>/',views.all_students_result,name="all_students_result"),
path('students_detail/',views.students_detail,name="students_detail"),
path('category/',views.category,name="category"),
path('material/<int:pk>/',views.material,name="material"),
]


