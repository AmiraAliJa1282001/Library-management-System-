from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.index, name="index"),
    path("student_registration/", views.student_registration, name="student_registration"),
    path("student_login/", views.student_login, name="student_login"),
    path("profile/", views.profile, name="profile"),
    path("change_password/", views.change_password, name="change_password"),
    path("logout/", views.Logout, name="logout"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("student_issued_books/", views.student_issued_books, name="student_issued_books"),


]