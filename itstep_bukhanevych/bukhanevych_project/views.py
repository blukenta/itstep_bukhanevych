from django.shortcuts import render, redirect
from .models import TodoItem, update_todo_item
from .forms import FormWithCaptcha, TodoForm
from django_ratelimit.decorators import ratelimit

@ratelimit(key='user_or_ip', rate='10/m')
def home(request):
    items = TodoItem.objects.all()
    return render(request, "home.html", {"todos": items, "captcha": FormWithCaptcha(), "add_todo": TodoForm()})

@ratelimit(key='user_or_ip', rate='10/m')
def todos(request):
    return render(request, "todos.html" )

@ratelimit(key='user_or_ip', rate='10/m')
def change(request):
    if request.method == "POST":
        id = request.POST.get("id", None)
        value = request.POST.get("checkbox_value_"+id, None)
        if value == "True":
            value = True
        else:
            value = False
        update_todo_item(id, value)
        return redirect("home")
        

    return redirect("home")

@ratelimit(key='user_or_ip', rate='10/m')
def add_todo(request):
    if request.method == "POST":
        form = FormWithCaptcha(request.POST)
        if form.is_valid():
            print("VALID.")
            print(form.cleaned_data["captcha"])
            form = TodoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("home")
        else:
            print("INVALID.")
            return redirect("home")
        
