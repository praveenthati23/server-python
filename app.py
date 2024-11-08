from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Happy Diwali to you praveenkumar thati"

if __name__ == '__main__':
    app.run(debug=True)

