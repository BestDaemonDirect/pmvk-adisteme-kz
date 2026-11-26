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
from . import error_views

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
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.contrib import admin

    admin.site.site_header = "PMVK — Управление"
    admin.site.site_title = "PMVK"
    admin.site.index_title = "Панель администратора"

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [path("admin/", admin.site.urls)]
    urlpatterns += [path("http-code/<int:code>/", error_views.preview_error, name="preview-http-code")]


handler100 = error_views.handler100
handler101 = error_views.handler101
handler102 = error_views.handler102
handler103 = error_views.handler103
handler200 = error_views.handler200
handler201 = error_views.handler201
handler202 = error_views.handler202
handler203 = error_views.handler203
handler204 = error_views.handler204
handler205 = error_views.handler205
handler206 = error_views.handler206
handler207 = error_views.handler207
handler208 = error_views.handler208
handler226 = error_views.handler226
handler300 = error_views.handler300
handler301 = error_views.handler301
handler302 = error_views.handler302
handler303 = error_views.handler303
handler304 = error_views.handler304
handler305 = error_views.handler305
handler307 = error_views.handler307
handler308 = error_views.handler308
handler400 = error_views.handler400
handler401 = error_views.handler401
handler402 = error_views.handler402
handler403 = error_views.handler403
handler404 = error_views.handler404
handler405 = error_views.handler405
handler406 = error_views.handler406
handler407 = error_views.handler407
handler408 = error_views.handler408
handler409 = error_views.handler409
handler410 = error_views.handler410
handler411 = error_views.handler411
handler412 = error_views.handler412
handler413 = error_views.handler413
handler414 = error_views.handler414
handler415 = error_views.handler415
handler416 = error_views.handler416
handler417 = error_views.handler417
handler418 = error_views.handler418
handler421 = error_views.handler421
handler422 = error_views.handler422
handler423 = error_views.handler423
handler424 = error_views.handler424
handler425 = error_views.handler425
handler426 = error_views.handler426
handler428 = error_views.handler428
handler429 = error_views.handler429
handler431 = error_views.handler431
handler451 = error_views.handler451
handler500 = error_views.handler500
handler501 = error_views.handler501
handler502 = error_views.handler502
handler503 = error_views.handler503
handler504 = error_views.handler504
handler505 = error_views.handler505
handler506 = error_views.handler506
handler507 = error_views.handler507
handler508 = error_views.handler508
handler510 = error_views.handler510
handler511 = error_views.handler511