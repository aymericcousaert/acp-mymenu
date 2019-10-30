import smtplib

from django.contrib import admin

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

    def send_email(self, _request, queryset):
        # Create msg object instance
        msg = MIMEMultipart()

        # Setup email parameters
        password = EMAIL_HOST_PASSWORD
        msg['Subject'] = EMAIL_SUBJECT
        msg['From'] = EMAIL_HOST_USER

        # Add the message body
        # TODO: completar esto con la URL autogenerada
        url = self.generate_url
        message = "Hi there Georgie!"
        msg.attach(MIMEText(message, 'plain'))

        # Create server
        server = smtplib.SMTP(EMAIL_HOST + ': ' + str(EMAIL_PORT))

        # Start server
        server.starttls()

        # Login credentials
        server.login(msg['From'], password)

        # Send message
        for client in queryset:
            server.sendmail(msg['From'], client.email, msg.as_string())

        # Shutdown server
        server.quit()

        # TODO: mostrar mensaje de exito por pantalla al admin

    send_email.short_description = "Send email to selected clients with suggestions URL"

    def generate_url(self):
        # TODO: See https://pypi.org/project/django-expiring-token/
        token = secrets.token_urlsafe(20)


# Register your models here

admin.site.register(Product)
admin.site.register(PaymentMethod)
admin.site.register(Category)
admin.site.register(DailySpecial)
admin.site.register(Promotion)
admin.site.register(Client, ClientAdmin)
