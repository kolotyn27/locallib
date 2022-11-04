from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def register(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("catalog:index")
    context = {"form": form}
    return render(request, "registration/register.html", context)
