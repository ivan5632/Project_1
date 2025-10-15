from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    """
    The main route that renders the HTML template.
    This template contains the button and the JavaScript logic for the message.
    """
    # Flask automatically looks for 'index.html' inside the 'templates' folder.
    return render_template('index.html')

# Run the application if the script is executed directly
if __name__ == '__main__':
    # Setting debug=True allows the server to reload automatically on code changes
    # and provides helpful error messages.
    app.run(debug=True)
