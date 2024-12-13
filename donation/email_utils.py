from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .tokens import account_activation_token  # Ensure this imports correctly

def send_reset_email(user, request):
    subject = 'Password Reset Requested'
    email_from = 'handit.pvt.ltd@gmail.com'  # Use your actual email
    recipient_list = [user.username]  # Assuming username is the email
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)
    link = request.build_absolute_uri(f'/reset_password/{uid}/{token}/')

    # Create the plain text email content
    text_content = (
        "You requested a password reset. "
        "Please visit the link below to reset your password:\n\n"
        f"{link}\n\n"
        "If you did not request a password reset, please ignore this email."
    )

    # Create the email message without HTML
    email = EmailMessage(subject, text_content, email_from, recipient_list)

    # Send the email
    email.send()
