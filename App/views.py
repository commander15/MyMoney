from typing import Any, Mapping
from django.shortcuts import render as renderView, redirect
from django.http import *
from django.contrib.auth.decorators import login_required

from datetime import datetime

from .forms import *
from .models import *

def render(request: HttpRequest, title: str, subTitle: str, template: str, context: Mapping[str, Any] = None):
    if (context == None):
        context = dict()
    
    context['title'] = title
    context['sub_title'] = subTitle

    if ("xtitle" not in context.keys()):
        context['xtitle'] = title

    return renderView(request, template, context)

def home(request: HttpRequest):
    return redirect('dashboard')

def registerUser(request: HttpRequest):
    if (request.method == "GET"):
        return render(request, "Registration", "Resister a new user !", "registration/register.html")
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('login')
        else:
            return HttpResponse(form.errors.as_text())
        
    return HttpResponse("Bad Request")

@login_required
def dashboard(request: HttpRequest):
    expenses = Expense.objects.all();

    context = dict()
    context['expenses'] = expenses
    return render(request, "Dashboard", "Your expenses on a graph !", "dashboard.html", context)

@login_required
def showExpenses(request: HttpRequest):
    context = dict()
    context['expenses'] = Expense.objects.filter(user__id=request.user.id)
    return render(request, "Expenses", "What i've buy ?", "expenses/list.html", context)

@login_required
def addExpense(request: HttpRequest):
    if (request.method == "GET"):
        return render(request, "Add Expense", "New expense ? Let's create it !", "expenses/add.html")
    else:
        form = ExpenseCreationForm(request.POST)
        if (form.is_valid()):
            form.instance.date = datetime.now().date()
            form.instance.time = datetime.now().time()
            form.instance.user_id = request.user.id

            expense = form.save()
            return redirect("edit_expense", id=expense.id)
        
    return HttpResponse("Bad Request !")

@login_required
def showExpense(request: HttpRequest, id: int):
    context = dict()
    context['xtitle'] = "Expenses"
    context['expense'] = Expense.objects.get(id=id)

    expense = context['expense']
    return render(request, expense.label, "Amount: " + str(expense.amount) + " XAF", "expenses/show.html", context)

@login_required
def editExpense(request: HttpRequest, id: int):
    expense = Expense.objects.get(id=id)

    if (request.method == "GET"):
        context = dict()
        context['xtitle'] = "Expenses"
        context['expense'] = expense
        return render(request, expense.label, "Amount: " + str(expense.amount) + " XAF", "expenses/edit.html", context)
    else:
        form = ExpenseCreationForm(request.POST, instance=expense)
        if (form.is_valid()):
            form.save()
            return redirect('expenses')
        
    return HttpResponse("Bad Request !")

@login_required
def deleteExpense(request: HttpRequest, id: int):
    Expense.objects.get(id=id).delete()
    return redirect('expenses')

@login_required
def addExpenseItem(request: HttpRequest, expenseId: int):
    if (request.method == "GET"):
        context = dict()
        context['xtitle'] = "Expenses"
        context['expense'] = Expense.objects.get(id=expenseId)
        return render(request, "Add Expense Item", "New expense item is comming out !", "expenses/items/add.html", context)
    else:
        form = ExpenseItemForm(request.POST)
        if (form.is_valid()):
            form.instance.expense_id = expenseId
            form.save()
            return redirect('edit_expense', id=expenseId)
        
    return HttpResponse("Bad Request !")

@login_required
def editExpenseItem(request: HttpRequest, expenseId: int, itemId: int):
    item = ExpenseItem.objects.get(id=itemId)
    if (request.method == "GET"):
        context = dict()
        context['xtitle'] = "Expenses"
        context['expense'] = Expense.objects.get(id=expenseId)
        context['item'] = item
        return render(request, "Edit Item", "Edit Expense Item !", "expenses/items/edit.html", context)
    else:
        form = ExpenseItemForm(request.POST, instance=item)
        if (form.is_valid()):
            form.save()
            return redirect("edit_expense", id=expenseId)
        
    return HttpResponse("Bad Request !")

@login_required
def deleteExpenseItem(request: HttpRequest, expenseId: int, itemId: int):
    ExpenseItem.objects.get(id=itemId).delete()
    return redirect("edit_expense", id=expenseId)