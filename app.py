from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🏆 E Sala Cup Namdu! Azure CI/CD Flask app proudly deployed by Poornesh 💪"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
