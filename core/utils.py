from django.contrib.auth.password_validation import validate_password as django_validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, get_object_or_404

from .models import TeacherProfile
from functools import wraps

def validate_password(password: str) -> bool:
    try:
        django_validate_password(password)
        return True
    except ValidationError:
        return False




def require_role(is_admin=True):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            teacher_id = request.session.get("id")
            if not teacher_id:
                return redirect("/")

            teacher = get_object_or_404(TeacherProfile, id=teacher_id)

    
            if teacher.is_admin != is_admin:
                if teacher.is_admin:
                    return redirect("dashboard-admin")
                else:
                    return redirect("dashboard-teacher")

            
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
    


require_teacher = require_role(is_admin=False)
require_admin = require_role(is_admin=True)