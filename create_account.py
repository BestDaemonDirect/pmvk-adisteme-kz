import secrets, string
import django 
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
django.setup()

from django.contrib.auth.models import User
from core.models import TeacherProfile
from django.db import IntegrityError, transaction


def generate_password(length=14):
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))



def create_account(username, password, first_name, last_name, email, phone, address, is_admin):
    if User.objects.filter(username=username).exists():
        print(f"Такой пользователь с {username} уже существует.")
        return
    
    if User.objects.filter(email=email).exists():
        print(f"Такой пользователь с такой почтой {email} уже существует.")
        return

    try: 
        with transaction.atomic():

            user_instance = User.objects.create_user(username=username, email=email, password=password,
                first_name=first_name, last_name=last_name, is_staff=True, is_superuser=is_admin
            )


            TeacherProfile.objects.create(user=user_instance, is_admin=is_admin, phone=phone, address=address)

    except IntegrityError:
        print(f"{username}: возникла ошибка при создание аккаунта.")
        return

    print(f"Пароль: {password} - Логин: {username}")


accounts = [
    {
        "username": "admin", "password": generate_password(),
        "first_name": "Александр", "last_name": "Иванов",
        "email": "admin@example.com", "phone": "+77001234567", "address": "Атырау",
        "is_admin": True,
    },
    {
        "username": "teacher1", "password": generate_password(),
        "first_name": "Дмитрий", "last_name": "Соколов",
        "email": "teacher1@example.com", "phone": "+77001234568", "address": "Атырау",
        "is_admin": False,
    },
    {
        "username": "teacher2", "password": generate_password(),
        "first_name": "Мария", "last_name": "Петрова",
        "email": "teacher2@example.com", "phone": "+77001234569","address": "Атырау",
        "is_admin": False,
    },
    {
        "username": "teacher3", "password": generate_password(),
        "first_name": "Иван", "last_name": "Кузнецов",
        "email": "teacher3@example.com", "phone": "+77001234560", "address": "Атырау",
        "is_admin": False,
    },
]

for account in accounts:
    create_account(**account)
    



