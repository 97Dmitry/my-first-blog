from django import forms
from .models import Author

class Autor_form(forms.ModelForm):

    class Meta():
        model = Author
        fields = ('author', 'email', 'real_firstname', 'real_lastname')