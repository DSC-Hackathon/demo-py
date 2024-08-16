from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# OpenAI API 키 설정
openai.api_key = ‘YOUR_OPENAI_API_KEY’

@app.route(‘/’)
def index():
    return render_template(‘input.html’)

@app.route(‘/summarize’, methods=[‘POST’])
def summarize():
    text = request.form[‘input_text’]
    # GPT 모델을 호출하여 요약 생성
    response = openai.Completion.create(
        engine=“text-davinci-003",  # GPT 모델 엔진
        prompt=f”Summarize the following text:\n\n{text}“,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    summary = response.choices[0].text.strip()
    return render_template(‘output.html’, original_text=text, summary=summary)


if __name__ == ‘__main__‘:
    app.run(debug=True)

    ###
