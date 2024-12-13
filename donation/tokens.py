from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import timezone

class MyPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        # Use str instead of six.text_type
        return f"{user.pk}{timestamp}{user.is_active}"

# Instantiate your custom token generator
account_activation_token = MyPasswordResetTokenGenerator()
