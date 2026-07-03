from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

question = input("你：")

response = client.responses.create(
    model="gpt-4.1-mini",
    input=question
)

print("AI：")
print(response.output_text)
print(response.output_text)