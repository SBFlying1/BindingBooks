from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .forms import SignUpForm, UserUpdateForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login after sign up
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def profile(request):
    # Simple read-only profile page
    return render(request, "accounts/profile.html")


@login_required
def profile_edit(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Profile updated!")
            return redirect("accounts:profile")
    else:
        user_form = UserUpdateForm(instance=request.user)

    return render(
        request,
        "accounts/profile_edit.html",
        {"user_form": user_form},
    )
