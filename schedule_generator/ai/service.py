# from gpt4all import GPT4All
#         # model = GPT4All(model_name='openchat-3.6-8b-20240522-Q5_K_M.gguf', allow_download=False, device='cpu')
        # model = GPT4All("Meta-Llama-3.1-8B-Instruct-128k-Q4_0.gguf")
        # model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM
        # with model.chat_session():
            # print(model.generate("Onde fica florianópolis?", max_tokens=1, temp=0))

# class AIService:
#     def __init__(self, model: Model):
#         self.model = model

#     def predict(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
#         return self.model.predict(data)