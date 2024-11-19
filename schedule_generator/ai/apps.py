from django.apps import AppConfig


class AiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ai'

    def ready(self):
        from gpt4all import GPT4All
        model = GPT4All(model_name='openchat-3.6-8b-20240522-IQ4_XS.gguf', allow_download=False, device='cpu')
        # with model.chat_session():
        #     print(model.generate("!SIM é NÃO?", max_tokens=10, temp=0))
        pass
