from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.core.signing import TimestampSigner
from .models import User
import os


signer = TimestampSigner()

def send_verification_email(user: User):
    token = signer.sign(user.pk)

    verify_path = reverse('receive-verification', kwargs={'token': token})
    subject = 'Verify Your Email Address'
    message = f'Hi {user.first_name},\nVerifications URL:\n{verify_path}' # can be upgrade

    print(f"Verify URL: {verify_path}")

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

