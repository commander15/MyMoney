from typing import Any, Mapping
from django.shortcuts import render as renderView
from django.http.request import *

def render(request: HttpRequest, title: str, subTitle: str, template: str, context: Mapping[str, Any] = None):
    if (context == None):
        context = dict()
    context['title'] = title
    context['sub_title'] = subTitle
    return renderView(request, template, context)

def itemClasses(title: str, currentTitle: str):
    if (title == currentTitle):
        return 'active'
    else:
        return ''

def showLogin(request: HttpRequest):
    return render(request, "Login", "Login", "login.html")

def logIn(request: HttpRequest):
    return showLogin(request)

def dashboard(request: HttpRequest):
    return render(request, "Dashboard", "Dashboard", "base.html")