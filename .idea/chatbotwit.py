# chatbot.py

from typing import List, Dict

class Chatbot:
    def __init__(self, system_prompt: str = "You are a helpful assistant."):
        self.system_prompt = system_prompt
        self.history: List[Dict[str, str]] = [
            {"role": "system", "content": self.system_prompt}
        ]

    def _call_model(self, messages: List[Dict[str, str]]) -> str:
        """
        TEMPLATE: Replace this with your actual LLM API call.
        For example, OpenAI, Anthropic, local model, etc.
        """

        # --- PSEUDOCODE EXAMPLE ---
        # from openai import OpenAI
        # client = OpenAI()
        # response = client.chat.completions.create(
        #     model="gpt-4.1-mini",
        #     messages=messages
        # )/
        # return response.choices[0].message.content.strip()
        # ---------------------------
        return "This is a placeholder response. Hook me up to a real model!"

    def reply(self, user_message: str) -> str:
        # Add user message to history
        self.history.append({"role": "user", "content": user_message})

        # Call model with full conversation
        assistant_reply = self._call_model(self.history)

        # Add assistant reply to history
        self.history.append({"role": "assistant", "content": assistant_reply})

        return assistant_reply

if __name__ == "__main__":
    bot = Chatbot(system_prompt="You are a helpful campus resource chatbot.")
    print("Chatbot ready! Type 'quit' to exit.\n")

    while True:
        user_msg = input("You: ")
        if user_msg.lower() in {"quit", "exit"}:
            print("Bot: Bye!")
            break

        response = bot.reply(user_msg)
        print("Bot:", response)
