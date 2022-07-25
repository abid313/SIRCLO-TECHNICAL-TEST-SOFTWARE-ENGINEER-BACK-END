from django import forms

class CreateNewList(forms.Form):
    date = forms.DateField(label="Tanggal", widget=forms.SelectDateWidget, input_formats=["%Y-%m-%d"])
    max = forms.IntegerField(label="Max")
    min = forms.IntegerField(label="Min")