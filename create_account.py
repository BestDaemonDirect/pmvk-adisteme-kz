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



# Создаем администратора
username = input("Напишите свой юсернэйм: ")
email = input("Напишите свой email: ")
phone = input("Можете вести свой телефон (Опционально): ")
address = input("Можете вести свой адресс (Опционально): ")


# Проверка на дубликат
if User.objects.filter(username=username).exists():
    raise ProcessLookupError(f"Такой пользователь с {username} уже существует.")
if User.objects.filter(email=email).exists():
    raise ProcessLookupError(f"Такой пользователь с такой почтой {email} уже существует.")



password = generate_password(length=15)

try: 
    with transaction.atomic():

        # Создаем экземпляр User
        user_instance = User.objects.create_user(
            username=username, email=email, password=password,
            first_name=username, last_name="Администратор ПВМК", is_staff=True
        )


        # Создаем наш экземпляр TeacherProfile
        teacher_instance = TeacherProfile.objects.create(
            user=user_instance, is_admin=True, phone=phone, address=address
        )

except IntegrityError:
    raise ProcessLookupError("Аккаунт не создан")


print(f"Пароль: {password} - Логин: {username}")






