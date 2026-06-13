from urllib import response

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(
base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

# LOGIN PAGE
@app.route('/')
def home():
    return render_template('login.html')

# CHAT PAGE
@app.route('/chat')
def chat():
    name = request.args.get('name')
    return render_template('chat.html', name=name)

# HOME PAGE
@app.route('/home')
def home_page():
    name = request.args.get('name')
    return render_template('home.html', name=name)

# CHATBOT RESPONSE
@app.route('/get_response', methods=['POST'])
def chatbot_response():

    try:
        data = request.get_json()

        user_message = data.get('message')
        username = data.get('username')

        if user_message.lower() in ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]:

            prompt = f"""
            You are MindMate, a supportive mental health chatbot.

            Greet the user warmly using their name {username}.
            Keep the response short and friendly.
            """

        else:

            prompt = f"""
            You are MindMate, a supportive mental health chatbot.

            Reply naturally and helpfully.
            Do NOT greet the user again.
            Do NOT repeat the user's name unless necessary.

            User message:
            {user_message}
            """

       
        response = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        bot_reply = response.choices[0].message.content

        return jsonify({
            "response": bot_reply
        })

    except Exception as e:
        print("FULL ERROR:", str(e))

        return jsonify({
            "response": str(e)
        })
# MAIN
if __name__ == '__main__':
    app.run(debug=True)