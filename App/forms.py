from django.forms import *

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import *

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

class ExpenseCreationForm(ModelForm):
    class Meta:
        model = Expense
        fields = [ 'label', 'budget' ]