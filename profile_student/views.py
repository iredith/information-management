from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, "profile_student/home/index.html")

def signup_student(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["mis"]
        password = request.POST["pass"]
        repass = request.POST["re_pass"]
        agree_terms = request.POST.get("agree_terms",False)
        if agree_terms or repass == password:
            user = User.objects.create_user(username= username, password=password)
            user.save()
            return HttpResponseRedirect(reverse("profile:signin_stud"))
        else:
            return HttpResponseRedirect(reverse("profile:signup_stud"))
            
    if not request.user.is_authenticated:
        return render(request, "profile_student/home/signup/signup.html")
    else:
        return render(request, "profile_student/default/index.html")



def signup_company(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["mis"]
        password = request.POST["pass"]
        repass = request.POST["re_pass"]
        agree_terms = request.POST.get("agree_terms",False)
        if agree_terms or repass == password:
            user = User.objects.create_user(username= username, password=password)
            user.save()
            return HttpResponseRedirect(reverse("profile:comp_signin"))
        else:
            return HttpResponseRedirect(reverse("profile:comp_signup"))
            
    if not request.user.is_authenticated:
        return render(request, "profile_student/home/company_Person/signup_cp/signup.html")
    else:
        return render(request, "profile_student/default/candidate.html")

    #return render(request, "profile_student/home/company_Person/signup_cp/signup.html")



        
def signin_student(request):
    if request.method == "POST":
        username = request.POST["mis"]
        password = request.POST["your_pass"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("profile:def_index"))
        else:
            return HttpResponseRedirect(reverse("profile:signin_stud"))
    else:
        return render(request, "profile_student/home/signin/signin.html")


def signin_company(request):
    if request.method == "POST":
        username = request.POST["mis"]
        password = request.POST["your_pass"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("profile:def_c"))
        else:
            return HttpResponseRedirect(reverse("profile:comp_signin"))
    else:
        return render(request, "profile_student/home/company_Person/signin_cp/signin.html")
    #return render(request, "profile_student/home/company_Person/signin_cp/signin.html")



def default_index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("profile:signin_stud"))
    return render(request, "profile_student/default/index.html", {
        'mis':request.user.username
    })






def display_prof(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("profile:signin_stud"))
    else:
        mis = request.user.username
        student = Student.objects.filter(mis=int(mis))
        if len(student)==0:
            message = "Your profile is not updated in database."
            return render(request, "profile_student/default/display/display.html", {
                "message": message
            })
        else:
            return render(request, "profile_student/default/display/display.html", {
                "student": student
            })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("profile:index"))

def company_person(request):
    return render(request, "profile_student/home/company_Person/Cp.html")

def faculty_incharge(request):
    return render(request, "profile_student/default/Faculty-incharge.html")

def student_incharge(request):
    return render(request, "profile_student/default/Student-incharge.html")

def candi(request):
    return render(request, "profile_student/default/candidate.html")

def default_index_candi(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("profile:comp_signin"))
    
    if request.method=="POST":
        sor = request.POST.get('quantity', 1)
        filt = request.POST["c"]
        if int(filt) == 2:
            students = Student.objects.all()
        else:
            students = Student.objects.filter(stream=int(filt))
        students = students.filter(gpa__gte = float(sor))
        
        return render(request, "profile_student/default/candidate.html", {
            "students" : students 
        })
    else:
        message="There are no students with selected criteria"
        return render(request, "profile_student/default/candidate.html", {
            "message" : message
        })





