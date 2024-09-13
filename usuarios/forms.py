from django import forms
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'cpf', 'telefone']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')

        if password:
            user.set_password(password)  # Criptografa a senha antes de salvar

        if commit:
            user.save()

        return user