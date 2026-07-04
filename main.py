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
while True:
    question = input("你：")
    
    if question == "exit":
        print("bye!")
        break
    history.append(
    {
        "role": "user",
        "content": question
    }
)
    response = client.responses.create(
        model="gpt-4.1-mini",
        input= history
    )

    print("AI：")
    print(response.output_text)
    history.append({
    "role": "assistant",
    "content": response.output_text
})