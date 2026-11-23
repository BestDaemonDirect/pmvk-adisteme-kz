from django.core.exceptions import ValidationError



class MaximumLengthValidator:
    def __init__(self, max_length=128):
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise ValidationError(
                f"Пароль не должен превышать {self.max_length} символов.",
                code="password_too_long",
            )

    def get_help_text(self):
        return f"Пароль должен содержать не более {self.max_length} символов."