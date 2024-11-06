
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserRegistrationform


def register(request):
    """
    Function for user registration.

    The request method 'POST' is checking that the form was submitted.

    Args:
        The HTTP request.

    Returns:
        HttpResponse: Rendered HTML response for registration page or redirect to home
    """

    if request.method == 'POST':
        # Form instance with the data submitted
        form = UserRegistrationform(request.POST)
        #Checks if form is valid
        if form.is_valid():
            #Saves the valid form data to the databasse
            form.save()
            #Gets the username from the form data
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('Login')
    else:
        #Creates an empty form if the request method is not Post
        form = UserRegistrationform()
    
    #Renders the registration form with the form instance
    return render(request, 'register.html', {'form': form})

