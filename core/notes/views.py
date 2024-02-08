from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from .models import *


def reg_page(request):
    if request.method == "GET":
        return render(request, "core/reg_page.html")
    else:
        data = request.POST
        username = data.get("username")
        email = data.get("email")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        password1, password2 = data.get("password1"), data.get("password2")
        if len(username) == 0:
            return HttpResponse("<h3>Введите имя пользователя</h3>")
        elif len(first_name) == 0 or len(last_name) == 0:
            return HttpResponse("<h3>Введите полное имя</h3>")
        elif len(email) == 0:
            return HttpResponse("<h3>Введите почту</h3>")
        elif len(password1) == 0 or len(password2) == 0:
            return HttpResponse("<h3>Введите пароль</h3>")
        elif password1 != password2:
            return HttpResponse("<h3>Пароли должны совпадать</h3>")
        else:
            newuser = User()
            newuser.create_user(username=username, first_name=first_name, last_name=last_name, password=password1)
            return redirect(note_page)


def login_page(request):
    if request.method == "GET":
        return render(request, "core/login_page.html")
    else:
        data = request.POST
        try:
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is None:
                return HttpResponse("<h3>Пользователь с таким логином и паролем не найден</h3>")
            login(request, user)
            return redirect(note_page)
        except KeyError:
            return HttpResponse("<h3>Заполните все поля</h3>")


def note_page(request):
    notes = Notes.objects.filter(login=request.user)
    if request.method == 'GET':
        return render(request, 'core/note_page.html', {'notes': notes})
    elif request.method == 'POST':
        data = request.POST
        note = Notes()
        note.create_note(data['note-text'], request.user)
        note.save()
        return redirect(note_page)


def logout_page(request):
    logout(request)
    return redirect(login_page)