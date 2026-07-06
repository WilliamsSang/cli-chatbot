from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class ChatBot:
    def __init__(self):
        self.client = OpenAI()
        self.history = [
            {
                "role": "system",
                "content": "你叫小含，是我的 Python 学习助手。请你用温柔耐心的风格跟我说话。请你每次回答我的问题时，不要直接告诉我答案，而是引导我自己理解问题。"
            }
        ]

    def add_message(self, role, content):
        self.history.append({
            "role": role,
            "content": content
        })

    def ask_llm(self):
        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=self.history
        )
        return response.output_text

    def trim_history(self):
        if len(self.history) > 21:
            self.history.pop(1)
            self.history.pop(1)

    def chat(self):
        while True:
            question = input("你: ")

            if question == "exit":
                print("bye!")
                break

            self.add_message("user", question)

            ai_reply = self.ask_llm()

            print("AI:")
            print(ai_reply)

            self.add_message("assistant", ai_reply)

            self.trim_history()


bot = ChatBot()
bot.chat()