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
    message =args.get("message")
    print(message)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return completion['choices'][0]['message']['content']

@app.route('/codegen', methods=['POST'])
def codegen():
    # Get the language and content from the request JSON data
    language = request.json['language']
    content = request.json['content']

    # Generate code using the OpenAI GPT-3 API
    prompt = f"Generate {language} code for the following task:\n\n{content}\n\n"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the response text from the OpenAI API response
    response_text = response.choices[0].text.strip()

    # Return the generated code
    return response_text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
