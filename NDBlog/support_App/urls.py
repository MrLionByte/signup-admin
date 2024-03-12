from django.urls import path
from . import views

urlpatterns = [

    path("",views.aboutpage,name="aboutpage"),
    path("blogpage/",views.blogpage,name="blogpage"),
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("logout_action/",views.logout_action,name="logout_action"),
    path("terms/",views.terms,name="terms"),
    path("admin_login",views.admin_login,name="admin_login"),
    path("admin_panel/",views.admin_panel,name="admin_panel"),
    path("admin_add/",views.admin_add,name="admin_add"),
    path("admin_edit/",views.admin_edit,name="admin_edit"),
    path("admin_update/",views.admin_update,name="admin_update"),
    path("admin_delete/",views.admin_delete,name="admin_delete"),
    path("admin_logout/",views.admin_logout,name="admin_logout"),

]
