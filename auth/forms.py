from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from auth.models import CustomUser
from customer.models import Customer
from driver.models import Driver
from payment.models import Card



class CustomerSignupForm (UserCreationForm):

    Preferred_method = forms.ChoiceField(
        choices = Customer.payment_methods,
        widget=forms.RadioSelect,
        required=False
    )
    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.preferred_method = self.Preferred_method  
        return user
    

class DriverSignupForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_driver = True
        user.save() 
        driver = Driver.objects.create(user=user) 
        return user

class CreditCardForm(forms.ModelForm):
    class Meta:
        model = Card  #when user chooses payment with card, its supposed to redirect him to this form then save this form's data along the user data in the Card model