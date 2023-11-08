from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    fecha_ingreso = forms.DateField
    numero_serie = forms.IntegerField(null=True, blank=True)
    ubicacion = forms.CharField


    