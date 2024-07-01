import logging

from openai import OpenAI

from csvgpt.config import Config

logging.getLogger("httpx").setLevel(logging.WARNING)


def ask_chatgpt(text: str, role) -> str:
    chat_gpt = ChatGPT(role)
    chat_gpt.add_user_message(text)
    return chat_gpt.evaluate()


class ChatGPT:
    def __init__(self, role):
        self.simulate = Config.get_instance().get('openai', 'simulate')
        self.client = OpenAI(
            api_key=Config.get_instance().get('openai', 'api_key'),
        )
        self.messages = [{"role": "system",
                          "content": role}]

    def add_user_message(self, message: str):
        self.messages.append({"role": "user", "content": message})

    def evaluate(self):
        if self.simulate:
            return str(self.messages)

        chat_completion = self.client.chat.completions.create(
            messages=self.messages,
            model="gpt-3.5-turbo",
            # model="gpt-4",
        )
        return chat_completion.choices[0].message.content
