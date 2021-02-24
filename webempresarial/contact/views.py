from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
# Para enviar el correo
from django.core.mail import EmailMessage

# Create your views here.


def contact(request):

    contact_form = ContactForm()
    # Sí y solo sí el método es POST, relleno la plantilla con la info
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():  # Recupero sí y solo sí son correctos
            # me devuleve el valor en la clave name
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Suponemos que todo va bien, redireccionamos
            # Enviamos correo y redireccionamos
            email = EmailMessage(
                "La caffeteira nuevo mensaje de contacto"
                "De{} <{}>\n\nEscribió:\n\n{}".format(
                    name, email, content),
                "no-contestar@inbox.mailtrop.io",
                ['mejiavillamil232@gmail.com'],
                reply_to=[email]
            )

            try:
                # Todo va bien
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                # algo no va bien
                return redirect(reverse('contact')+'?fail')

    return render(request, 'contact/contact.html', {'form': contact_form})
