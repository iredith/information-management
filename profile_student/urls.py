from django.urls import path
from . import views


app_name = "profile" 
urlpatterns = [
    path("", views.index, name="index"),
    path("signup/signup.html", views.signup_student, name="signup_stud"),
    path("signin/signin.html", views.signin_student, name="signin_stud"),
    path("default/index.html", views.default_index, name="def_index"),
    path("default/display/display.html", views.display_prof, name="display"),
    path("logout", views.logout_view, name="logout_view"),
    path("company_Person/Cp.html", views.company_person, name="companyperson"),
    path("company_Person/signin_cp/signin.html", views.signin_company, name="comp_signin"), 
    path("company_Person/signup_cp/signup.html", views.signup_company, name="comp_signup"),
    path("faculty_incharge", views.faculty_incharge, name="fac_in"),
    path("student_incharge", views.student_incharge, name="stu_in"),
    path("candidates", views.candi, name="cand"),
    path("default/candi", views.default_index_candi, name="def_c"),
    
]