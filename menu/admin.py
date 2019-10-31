import smtplib

from django.contrib import admin
from django.contrib import messages

# Email packages

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mymenu.settings import EMAIL_HOST_USER
from mymenu.settings import EMAIL_HOST_PASSWORD
from mymenu.settings import EMAIL_PORT
from mymenu.settings import EMAIL_HOST
from mymenu.settings import EMAIL_SUBJECT

# Token packages

import secrets

# Models

from menu.models import Product
from menu.models import PaymentMethod
from menu.models import Category
from menu.models import DailySpecial
from menu.models import Promotion
from menu.models import Client


class ClientAdmin(admin.ModelAdmin):
    actions = ['send_email']

    def send_email(self, request, queryset):
        # Create msg object instance
        msg = MIMEMultipart()

        # Email parameters
        password = EMAIL_HOST_PASSWORD
        msg['Subject'] = EMAIL_SUBJECT
        msg['From'] = EMAIL_HOST_USER

        # Message constants
        message_prefix = "Hola "
        message_suffix = ",\nQueremos saber cómo fue tu experiencia en nuestro restaurante.\n" \
                         "Para ello, te enviamos un link con un formulario de comentarios y/o sugerencias: "
        message_suffix_2 = "\n¡Esperamos recibirte nuevamente!"

        # Create server
        server = smtplib.SMTP(EMAIL_HOST + ': ' + str(EMAIL_PORT))

        # Start server
        server.starttls()

        # Login credentials
        server.login(msg['From'], password)

        # Send message
        for client in queryset:
            # Generate token and store it in database
            token = secrets.token_urlsafe(20)
            client.token = token

            # TODO: corregir la URL para que no sea fijo el localhost y no se muestre el mail
            url = "localhost:8000/form_suggestions/" + client.email + "/" + token

            # Add the message body
            full_message = message_prefix + client.name + message_suffix + url + message_suffix_2
            msg.attach(MIMEText(full_message, 'plain'))

            # Send email
            server.sendmail(msg['From'], client.email, msg.as_string())

        # Shutdown server
        server.quit()

        # Show success message
        messages.add_message(request, messages.SUCCESS, 'Email sent successfully')

    send_email.short_description = "Send email to selected clients with suggestions URL"


# Register your models here

admin.site.register(Product)
admin.site.register(PaymentMethod)
admin.site.register(Category)
admin.site.register(DailySpecial)
admin.site.register(Promotion)
admin.site.register(Client, ClientAdmin)
