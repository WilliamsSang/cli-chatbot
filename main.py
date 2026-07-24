import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from tools import get_current_time, calculate

load_dotenv()

class ChatBot:
    def __init__(self):
        self.client = OpenAI()

        system_prompt = self.load_system_prompt()

        self.history = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

        self.tools = [ 
    {
    "type": "function",
    "name": "get_current_time",
    "description": "Retrieve the current local date and time.",
    },
    {
    "type": "function",
    "name": "calculate",
    "description": "Calculate a mathematical expression.",
    "parameters": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "The math expression to calculate."
            }
        },
        "required": ["expression"],
        "additionalProperties": False
    }}  ]
        
        self.tool_map = {
    "get_current_time": get_current_time,
    "calculate": calculate,
}
        self.load_history()
    
    def load_system_prompt(self) -> str:
        with open("system_prompt.txt", "r", encoding="utf-8") as file:
            return file.read().strip()
    
    def add_message(self, role, content):
        self.history.append({
            "role": role,
            "content": content
        })

    def save_history(self):
        with open("history.json", "w", encoding="utf-8") as file:
            json.dump(self.history, file, ensure_ascii=False, indent=2)
    
    def load_history(self):
        if os.path.exists("history.json"):
            with open("history.json", "r", encoding="utf-8") as file:
                saved_history = json.load(file)

            self.history.extend(saved_history[1:])
    
    def ask_llm(self):
        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=self.history,
            tools=self.tools,
        )

        for item in response.output:
            if item.type == "function_call":
                tool_function = self.tool_map.get(item.name)

                if tool_function is None:
                    raise ValueError(f"Unknown tool: {item.name}")
                
                arguments = json.loads(item.arguments)

                tool_result = tool_function(**arguments)

                second_input = self.history.copy()

                second_input.extend(response.output)

                second_input.append(
                        {
                            "type": "function_call_output",
                            "call_id": item.call_id,
                            "output": json.dumps(
                                tool_result,
                                ensure_ascii=False
                            ),
                        }
                    )

                final_response = self.client.responses.create(
                        model="gpt-4.1-mini",
                        input=second_input,
                        tools=self.tools,
                    )

                return final_response.output_text

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

            self.save_history()

if __name__ == "__main__":
    bot = ChatBot()
    bot.chat()