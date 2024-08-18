from flask import Flask, render_template, request, jsonify, Response, redirect, url_for, flash
# import openai

app = Flask(__name__)

# Set up your OpenAI API key
# openai.api_key = 'your-openai-api-key'

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     # if request.method == 'POST':
#     #     user_input = request.form['textbox']
        
#     #     # Call OpenAI's API to generate worksheet content
#     #     response = openai.Completion.create(
#     #         engine="gpt-4",  # Adjust the engine name if using Gemini or another model
#     #         prompt=f"Create a worksheet based on the following input: {user_input}",
#     #         max_tokens=500
#     #     )
        
#     #     worksheet_content = response.choices[0].text.strip()
        
#         return render_template('index.html', worksheet_content=worksheet_content)

#     return render_template('index.html', worksheet_content=None)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
