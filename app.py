from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
<<<<<<< HEAD
    return "Happy Diwali india,have a blast!"
>>>>>>> a412003c0da1345372ea31f10f91d000eb139c3d

if __name__ == '__main__':
    app.run(debug=True)

