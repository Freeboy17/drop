
# - Import password reset token generator

from django.contrib.auth.tokens import PasswordResetTokenGenerator



# - Password reset token generator method

class UserVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        user_id = user.pk
        ts = timestamp
        is_active = user.is_active
        return f"{user_id}{ts}{is_active}"

user_tokenizer_generate = UserVerificationTokenGenerator()