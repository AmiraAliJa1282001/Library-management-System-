from django.contrib import admin
from library.models import Student,Book,IssuedBook
# Register your models here.
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(IssuedBook)
