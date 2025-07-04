from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Auto-deployment is working! Helloo from Poornesh's updated Flask apps!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
