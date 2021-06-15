from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages #import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("/") #login/
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm

    context={"register_form":form}
    template = 'registration/register.html'
    return render(request, template, context)
