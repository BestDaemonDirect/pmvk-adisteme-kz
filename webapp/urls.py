"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from core import views

urlpatterns = [
    path("", views.landing),
    path("logout/", views.logout_user, name="logout"),

    
    # Teacher
    path("dashboard-teacher/", views.dashboard_teacher, name="dashboard-teacher"),
    path("dashboard-teacher/edit-profile", views.teacher_edit_profile, name="teacher-edit-profile"),
    path("dashboard-teacher/add-info/", views.teacher_add_info, name="teacher-add-info"),
    path("dashboard-teacher/edit-info/<int:info_id>/", views.teacher_edit_info, name="teacher-edit-info"),
    path("dashboard-teacher/delete-info/<int:info_id>/", views.teacher_delete_info, name="teacher-delete-info"),


    # Admin
    path("dashboard-admin/", views.dashboard_admin, name="dashboard-admin"),
    path("dashboard-admin/add-teacher-profile/", views.admin_add_teacher_profile, name="add-teacher-profile"),
    path("dashboard-admin/get-teacher-profile/<int:teacher_id>/", views.admin_get_teacher_profile, name="get-teacher-profile"),
    path("dashboard-admin/set-teacher-password/<int:teacher_id>/", views.admin_set_teacher_password, name="set-teacher-password"),
    path("dashboard-admin/edit-teacher-profile/<int:teacher_id>", views.admin_edit_teacher_profile, name="edit-teacher-profile"),
    path("dashboard-admin/delete-teacher-profile/<int:teacher_id>/", views.admin_delete_teacher_profile, name="delete-teacher-profile"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )