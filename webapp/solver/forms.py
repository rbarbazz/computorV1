from django import forms

class EquForm(forms.Form):
	equation = forms.CharField(widget=forms.TextInput(attrs={'max_length' : 1000, 'class' : 'form-control', 'required' : True}))