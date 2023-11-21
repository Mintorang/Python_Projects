# Import the Flask framework and the render_template function
from flask import Flask, render_template

# Create a Flask web application instance
app = Flask(__name__)

# Define routes and corresponding view functions

# Route for the default page (index)
@app.route('/')
def index():
    # Render the 'index.html' template
    return render_template('index.html')

# Route for the 'form' page
@app.route("/form")
def form():
    # Render the 'Forms.html' template
    return render_template("Forms.html")

# Route for the 'home' page
@app.route("/home")
def home():
    # Render the 'home.html' template
    return render_template("home.html")

# Route for the 'profile' page
@app.route("/profile")
def profile():
    # Render the 'profile.html' template
    return render_template("profile.html")

# Run the Flask application if this script is executed
if __name__ == '__main__':
    # Start the development server with debug mode enabled
    app.run(debug=True)
