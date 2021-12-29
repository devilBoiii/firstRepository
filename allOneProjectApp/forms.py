from django import forms
from allOneProjectApp.models import onePiece

class onePieceForms(forms.ModelForm):
	class Meta:
		model=onePiece
		fields='__all__' # To fetch all the fields of the forms
