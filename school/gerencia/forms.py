from django import forms
from gerencia.models import ModeloForm

class DjangoForm(forms.ModelForm):   
    
    class Meta:
        model = ModeloForm
        fields = ('nome','email','telefone','descricao')
        
    