from django import forms

class CelularFormulario(forms.Form):
    fabricante = forms.CharField(max_length=13, label='Fabricante')
    modelo = forms.CharField(max_length=30, label='Modelo')
    color = forms.CharField(max_length=10, label='Color')
    anio = forms.IntegerField(min_value=1973, max_value=2024, label='Año')
    

class BuscarCelular(forms.Form):
    fabricante = forms.CharField(max_length=13, required=False)
    modelo = forms.CharField(max_length=30, required=False)
    color = forms.CharField(max_length=10, required=False)
    