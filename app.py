from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Happy Diwali india,have a blast!"

if __name__ == '__main__':
    app.run(debug=True)

