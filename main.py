from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
history = [
    {
        "role": "system",
        "content": "你叫小含 是我的python学习助手 请你用温柔耐心的风格跟我说话 请你每次回答我的问题的时候不直接告诉我答案而是引导我自己理解问题"
    }
]
def add_message(history, role, content):
    history.append({"role":role, "content":content})
def ask_llm(history):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=history
    )
    return response.output_text
def trim_history(history):
    if len(history) > 21:
        history.pop(1)
        history.pop(1)
def chat():  
    while True:
        question = input("你：")
    
        if question == "exit":
            print("bye!")
            break
        add_message(history, "user", question)
        ai_reply = ask_llm(history)

        print("AI:")
        print(ai_reply)

        add_message(history, "assistant", ai_reply)

        trim_history(history)
chat()