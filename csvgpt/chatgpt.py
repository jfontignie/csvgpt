"""
Module providing chatgpt helper
"""
import logging

from openai import OpenAI

from csvgpt.config import Config

logging.getLogger("httpx").setLevel(logging.WARNING)


def ask_chatgpt(text: str, role) -> str:
    """
    Asks chatgpt with @text
    :param text: The text to ask to chatgpt
    :param role: The role to prepare chatgpt. It can ben empty
    :return: the answer from chatgpt or the query sent if simulation is true
    """
    chat_gpt = ChatGPT(role)
    chat_gpt.add_user_message(text)
    return chat_gpt.evaluate()


class ChatGPT:
    """
    Helper class for chatgpt
    """
    def __init__(self, role):
        """
        :param role: of the gpt to answer
        """
        self.simulate = Config.get_instance().get('openai', 'simulate')
        self.client = OpenAI(
            api_key=Config.get_instance().get('openai', 'api_key'),
        )
        self.messages = [{"role": "system",
                          "content": role}]

    def add_user_message(self, message: str):
        """
        the message to add
        :param message:
        :return: nothing
        """
        self.messages.append({"role": "user", "content": message})

    def evaluate(self):
        """
        :return: the answer of chatgpt or the query sent if simulation is true
        """
        if self.simulate:
            return str(self.messages)

        chat_completion = self.client.chat.completions.create(
            messages=self.messages,
            model="gpt-4o-mini",
            # model="gpt-4",
        )
        return chat_completion.choices[0].message.content
