# accounts/utils.py
# from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.core.signing import TimestampSigner
from .models import User
import os


# just for development purpose only.
def send_mail(*args):
    with open(os.path.join(settings.BASE_DIR, "mails.txt"), "w") as file:
        file.write(" ".join(map(str, args)))


signer = TimestampSigner()


def send_verification_email(user: User):
    # Create a token that encodes the user’s primary key
    token = signer.sign(user.pk)

    # Build the verification URL. Ensure SITE_URL is set in settings (e.g., "http://localhost:8000")
    verify_path = reverse('verify-email', kwargs={'token': token})
    verify_url = f"{settings.SITE_URL}{verify_path}"

    subject = 'Verify Your Email Address'
    message = f'Hi {user.first_name},\nVerifications URL:\n{verify_url}'

    print(f"Verify URL: {verify_url}")

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
