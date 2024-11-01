from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World Have a Nice Day"

if __name__ == '__main__':
    app.run(debug=True)

