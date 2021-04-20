from django.apps import AppConfig


class FirstAppConfig(AppConfig):
    name = 'first_app'

    def ready(self):
        import first_app.signals 
