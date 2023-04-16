from django import forms

class AsociadosForm(forms.Form):
    apellido_familia= forms.CharField(max_length= 40)
    email = forms.EmailField(max_length= 30)
    DNI = forms.CharField(max_length = 8)
    integrantes = forms.CharField(max_length=2)
    mascotas = forms.CharField(max_length= 3)
    def __str__(self):
        return "Ya sos parte de la familia!"
    
class TorneoForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField(max_length= 30)
    DNI = forms.CharField(max_length= 8)
    def __str__(self):
        return f"Ya estas insripto {self.nombre}! En breve te enviaremos toda la información sobre el torneo a tu email!"
    
class TerrenosForm(forms.Form):
    nombre = forms.CharField(max_length= 20)
    apellido = forms.CharField(max_length= 40)
    telefono = forms.CharField(max_length= 12)
    email = forms.EmailField(max_length= 30)
    def __str__(self):
        return f"{self.nombre} pronto te contactaremos para atender tu solicitud y brindarte toda la información disponibe!"
    