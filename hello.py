from flask import Flask,request
import os
import openai

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_KEY')

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"


@app.route('/chatgpt')
def chatgpt():
    args = request.args
    message = args.get("message")
    print(message)
    completion = openai.ChatCompletion.create(
        model="text-davinci-002",
        prompt=f"{message}\nCode:",
        temperature=0.7,
        max_tokens=1024,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    response = completion.choices[0].text.strip()
    return response


@app.route('/create_code', methods=['POST'])
def create_code():
    data = request.json
    language = data['language']
    content = data['content']
    completion = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Generate {language} code:\n{content}\n",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    response = completion.choices[0].text.strip()
    return response
