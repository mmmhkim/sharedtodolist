from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist.models import Item
from django.contrib import messages
from django.db import connection

def home(request):
    cursor = connection.cursor()
    if request.method == "POST":
        if request.POST.get("task_name"):
            tempSave = Item()
            tempSave.content = request.POST.get("task_name")
            sqlCall = "INSERT INTO todolist_item (content) VALUES (%s)"
            values = [tempSave.content]
            cursor.execute(sqlCall, values)
            allItems = Item.objects.all()
            return render(request, "todolist/home.html", {"todo": allItems})
    else:
            cursor.execute("ALTER TABLE todolist_item AUTO_INCREMENT=0;")
            allItems = Item.objects.all()
            return render(request, "todolist/home.html", {"todo": allItems})

def delete(request, id):
    deleteTask = Item.objects.get(id=id)
    deleteTask.delete()
    cursor = connection.cursor()
    cursor.execute("ALTER TABLE todolist_item AUTO_INCREMENT=0;")
    return redirect("todo-home")

