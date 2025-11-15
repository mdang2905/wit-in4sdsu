# app.py
from flask import Flask, request, jsonify, render_template
from openai import OpenAI

client = OpenAI()
app = Flask(__name__)

SYSTEM_PROMPT = """
You are a helpful campus basic needs assistant.
You answer clearly and concisely. If you don't know something, say you don't know.
"""

# --- OPTIONAL: we'll plug custom resources in Section 2 ---
CUSTOM_RESOURCES = []  # we'll fill this later


def build_context(user_message: str):
    """
    Simple place to inject custom info (Section 2 will expand this).
    For now, just return the system message + user message.
    """
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]
    return messages


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    messages = build_context(user_message)

    # 🔁 You can swap this for another provider if you want
    response = client.chat.completions.create(
        model="gpt-4.1-mini",  # or gpt-5.1-mini etc.
        messages=messages,
    )

    reply = response.choices[0].message.content.strip()
    return jsonify({ "reply": reply })


if __name__ == "__main__":
    app.run(debug=True)
