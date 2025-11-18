from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

app_name = "accounts"

urlpatterns = [
    # Sign up (registration)
    path("signup/", views.signup, name="signup"),

    # Login / Logout
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),
     path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="home"),
        name="logout",
    ),

    # Profile pages
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),

    # Password change (for logged-in users)
    path(
        "change_password/",
        auth_views.PasswordChangeView.as_view(
            template_name="registration/change_password.html",
            success_url = reverse_lazy("accounts:password_change_done")
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="registration/password_change_done.html"
        ),
        name="password_change_done",
    ),
    
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),

]
