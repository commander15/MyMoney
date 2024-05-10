from django.urls import path

from .views import *

urlpatterns = [
    path('', home),
    path('register', registerUser, name="register"),
    path('dashboard', dashboard, name="dashboard"),
    path('expenses', showExpenses, name="expenses"),
    path('expenses/add', addExpense, name="add_expense"),
    path('expenses/<int:id>/show', showExpense, name="show_expense"),
    path('expenses/<int:id>/edit', editExpense, name="edit_expense"),
    path('expenses/<int:id>/delete', deleteExpense, name="delete_expense"),
    path('expenses/<int:expenseId>/items/add', addExpenseItem, name="add_expense_item"),
    path('expenses/<int:expenseId>/items/<int:itemId>/edit', editExpenseItem, name="edit_expense_item"),
    path('expenses/<int:expenseId>/items/<int:itemId>/delete', deleteExpenseItem, name="delete_expense_item"),
]