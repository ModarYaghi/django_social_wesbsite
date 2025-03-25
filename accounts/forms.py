from django import forms


class LoginForm(forms.Form):
    """
    A form to authenticate users against the database.

    The PasswordInput widget is ued to render the password
    HTML element. This will include `type="password"` in the
    HTML so that the browser treats it as a password.
    """

    username = forms.CharField()
    password = forms.CharField(widget=forms.passwordInput)
