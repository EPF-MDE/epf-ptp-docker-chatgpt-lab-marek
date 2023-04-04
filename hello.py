from flask import Flask, request
import openai
import os

app = Flask(__name__)

# Set the OpenAI API key
openai.api_key = os.environ.get("OPENAI_KEY")

@app.route('/chatgpt', methods=['GET'])
def chatgpt():
    # Get the message from the request query parameters
    message = request.args.get('message')

    # Generate a response using the OpenAI GPT-3 API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the response text from the OpenAI API response
    response_text = response.choices[0].text.strip()

    # Return the response text
    return response_text

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


