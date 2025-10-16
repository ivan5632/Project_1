from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Renders the index.html file from the templates directory
    return render_template('index.html')

if __name__ == '__main__':
    # We will use Gunicorn for production, but this is fine for local testing
    app.run(host='0.0.0.0', port=5000)


