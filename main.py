from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
history = []
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