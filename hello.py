from flask import Flask, request
import os
import openai

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_KEY')


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

#we use app.route to define the route of the API which means the URL
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


@app.route('/create_code', methods=['POST']) #we use the POST method because we send data to the API
def create_code():
    #we set the language and the content
    language = request.json['language']
    content = request.json['content']
    #we create the prompt
    completion = openai.Completion.create(
        #we use the davinci-codex model
        engine="davinci-codex",
        prompt=f"Generate {language} code:\n{content}\n",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    #we return the response from the API 
    response = completion.choices[0].text.strip() #the completion is a list of choices, we take the first one
    return response

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
