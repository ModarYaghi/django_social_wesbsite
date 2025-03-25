from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm

# Create your views here.
#


def user_login(request):
    """
    Handle user login via an HTTP POST request.

    When the request method is POST, this function validates the submitted login form,
    attempt to authenticate the user with the provided credentials, and logs the user in
    if the credentials are correct and the account is active. If the user is not
    authenticated or the account is disabled, an appropriate HTTP response is returned.

    For GET requests, an empty login form is rendered.

    Parameters:
        request (HttpRequest): The HTTP request object containing user data and metadata.

    Returns:
        HttpResponse: An HTTP response object that either indicates the login status or
        renders the login page.
    """

    if request.method == "POST":
        # Instantiate the login form with POST data.
        form = LoginForm(request.POST)

        if form.is_valid():
            # Extract validated data from the form.
            cd = form.cleaned_data
            # Attempt to authenticate the user using the provided username and password.
            user = authenticate(
                request,
                username=cd["username"],
                password=cd["password"],
            )

            if user is not None:
                # check if the user's account is active.'
                if user.is_active:
                    # Log the user in.
                    login(request, user)
                    return HttpResponse("Authenticated successfully")

                else:
                    # Return a response indicating the account is disabled.
                    return HttpResponse("disabled account")

            else:
                # Return a response indicating invalid login credentials.
                return HttpResponse("Invalid login")

    else:
        # If the request method is not POST, create an empty login form.
        form = LoginForm()

    # Render the login template witht he form context.
    return render(request, "account/login.html", {"form": form})
