from flask import Flask, render_template, request
import model

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def check():
    text = request.form['organo']
    ans = model.predict(str(text))
    print('Bye Bye Have a Nice Day!')
    return render_template('index.html', ans=ans)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='5000', debug=True)
