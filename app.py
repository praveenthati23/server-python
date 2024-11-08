from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():

    return "Happy Diwali india,have a blasting day the fire crackers! and be safe india"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


