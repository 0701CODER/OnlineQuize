from django.contrib import admin
from .models import *
admin.site.register(Question_Category)
admin.site.register(Quiz_Question)
admin.site.register(StudentDetail)
admin.site.register(Answer_Detail)
admin.site.register(Study_Material)