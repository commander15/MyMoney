from django.contrib.auth.models import User
from django.db import models

class Expense(models.Model):
    label = models.CharField("label", max_length=30)
    date = models.DateField("date")
    time = models.TimeField("time")
    budget = models.FloatField("budget")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.label

    @property
    def amount(self):
        amount = 0.0
        for item in self.items.all():
            amount += item.amount
        return amount


class ExpenseItem(models.Model):
    name = models.CharField("name", max_length=20)
    amount = models.FloatField("amount", default=0.0)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name="items")

    def __str__(self) -> str:
        return self.name