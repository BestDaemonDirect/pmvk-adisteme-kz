from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.db import IntegrityError, transaction
from django.contrib.auth.models import User

from .utils import validate_password, require_admin, require_teacher
from .models import TeacherProfile, TeacherInformation

# Create your views here.
ADMIN_DIR = "admin/"
TEACHER_DIR = "teacher/"

LANDING = "landing.html"


# Landing and logout
def landing(request: HttpRequest) -> HttpResponse:  
    if request.method.upper() == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            return render(request, LANDING, context={"fail": "Введите имя пользователя или пароль."})

        user_obj = User.objects.filter(username=username).first()
        if not user_obj:
            return render(request, LANDING, context={"fail": "Пользователь не найден."})

        user = authenticate(request, username=user_obj.username, password=password)

        if user:
            try: 
                teacher = TeacherProfile.objects.get(user=user)

                login(request, user)
                request.session["id"] = teacher.id

                if teacher.is_admin:
                    return redirect("dashboard-admin")
                else:
                    return redirect("dashboard-teacher")


            except TeacherProfile.DoesNotExist:
                return render(request, LANDING, context={"fail": "Профиль учителя не найден."})

        else:
            return render(request, LANDING, context={"fail": "Неверный пароль."}) 


        
    return render(request, LANDING)

  
  

def logout_user(request: HttpRequest) -> HttpResponse:
    if "id" in request.session:
        del request.session["id"]

    logout(request)

    return redirect("/")



# Teacher
@require_teacher
def dashboard_teacher(request: HttpRequest) -> HttpResponse:
    return render(request, TEACHER_DIR + "dashboard.html")

@require_teacher
def teacher_add_info(request: HttpRequest) -> HttpResponse:
    return render(request, TEACHER_DIR + "add_info.html")


@require_teacher
def teacher_edit_info(request: HttpRequest) -> HttpResponse:
    return render(request, TEACHER_DIR + "edit_info.html")

@require_teacher
def teacher_delete_info(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hi")




# Admin
@require_admin
def dashboard_admin(request: HttpRequest) -> HttpResponse:
    teachers = TeacherProfile.objects.filter(is_admin=False)

    return render(request, ADMIN_DIR + "dashboard.html", {"teachers": teachers})


@require_admin
def admin_add_teacher_profile(request: HttpRequest) -> HttpResponse:
    if request.method.upper() == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()

        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        address = request.POST.get("address", "").strip()

        if not username or not password:
            return render(request, ADMIN_DIR + "add_teacher_profile.html", {"fail": "Введите имя пользователя или пароль."})

        if User.objects.filter(username=username).exists():
            return render(request, ADMIN_DIR + "add_teacher_profile.html", {"fail": "Такой пользователь уже существует."})

        if not validate_password(password=password):
            return render(request, ADMIN_DIR + "add_teacher_profile.html", 
                          {"fail": "Пароль должен быть не меньше 8 символов и не больше 25 символов"})

        try:
            with transaction.atomic():
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)

                TeacherProfile.objects.create(user=user, phone=phone, address=address, is_admin=False)
        except IntegrityError:
            return render(request, ADMIN_DIR + "add_teacher_profile.html", {"fail": "Не удалось создать аккаунт."})

        return redirect("dashboard-admin")


    return render(request, ADMIN_DIR + "add_teacher_profile.html")


@require_admin
def admin_get_teacher_profile(request: HttpRequest, teacher_id: int) -> HttpResponse:
    teacher = get_object_or_404(TeacherProfile, id=teacher_id)

    context = {"teacher": teacher}

    return render(request, ADMIN_DIR + "get_teacher_profile.html", context)

@require_admin
def admin_set_teacher_password(request: HttpRequest, teacher_id: int) -> HttpResponse:
    teacher = get_object_or_404(TeacherProfile, id=teacher_id)

    if request.method.upper() == "POST":
        password = request.POST.get("password", "").strip()

        if not password:
            return render(request, ADMIN_DIR + "set_teacher_password.html", {"fail": "Введите пароль.", "teacher": teacher})

        if not validate_password(password):
            return render(request, ADMIN_DIR + "set_teacher_password.html", 
                          {"teacher": teacher, "fail": "Пароль должен быть не меньше 8 символов и не больше 25 символов"})

        teacher.user.set_password(password)
        teacher.user.save()

        return redirect("get-teacher-profile", teacher_id=teacher.id)
        
    return render(request, ADMIN_DIR + "set_teacher_password.html", {"teacher": teacher})

@require_admin
def admin_edit_teacher_profile(request: HttpRequest, teacher_id: int) -> HttpResponse:
    teacher = get_object_or_404(TeacherProfile, id=teacher_id)

    if request.method.upper() == "POST":
        username = request.POST.get("username", "").strip()
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()

        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        address = request.POST.get("address", "").strip()

        if not username:
            return render(request, ADMIN_DIR + "edit_teacher_profile.html", 
                          {"teacher": teacher, "fail": "Имя пользователя обязателен."})

        try:
            with transaction.atomic():
                teacher.user.username = username
                teacher.user.first_name = first_name
                teacher.user.last_name = last_name
                teacher.user.email = email

                teacher.user.save()

                teacher.phone = phone
                teacher.address = address
                teacher.save()

        except IntegrityError:
            return render(request, ADMIN_DIR + "edit_teacher_profile.html", 
                          {"teacher": teacher, "fail": "Возникла ошибка при изменениях данных."})

        return redirect("get-teacher-profile", teacher_id=teacher.id)

        
    return render(request, ADMIN_DIR + "edit_teacher_profile.html", {"teacher": teacher})


@require_admin
def admin_delete_teacher_profile(request: HttpRequest, teacher_id: int) -> HttpResponse:
    teacher = get_object_or_404(TeacherProfile, id=teacher_id)

    teacher.user.delete()
    
    return redirect("dashboard-admin")