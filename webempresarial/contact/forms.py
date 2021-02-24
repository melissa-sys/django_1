from django import forms
# Django me provee los formularios, con campos para ser procesados de la manera que sea necesaria. Así, con Django puedo improtar los valores a continuación. Sustituyo verbose_name por label
# Required es para hacer el campo obligatorio


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Escribe tu nombre'}
    ), min_length=3, max_length=1000)
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Escribe tu email'}
    ), min_length=3, max_length=1000)
    content = forms.CharField(
        label='Contenido', required=True, widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': '3',
                   'placeholder': 'Escribe el mensaje'}
        ), min_length=3, max_length=1000)

# voy a customizar los campos que están creados en el fomulario con los attrs, así añado estilos de bootstrap como si fueran diccionarios
