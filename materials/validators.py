from rest_framework.serializers import ValidationError


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url = value.get(self.field)
        if url and url != 'https://www.youtube.com/':
            raise ValidationError('URLs to third party videos are prohibited')
