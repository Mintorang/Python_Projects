from flask import Blueprint, render_template, jsonify, redirect, url_for

# Create a Blueprint named 'views'
views = Blueprint(__name__, "views")

# Route for the home page
@views.route("/")
def home():
    return render_template("index.html")

# Route for the profile page
@views.route("/profile")
def profile():
    return render_template("profile.html")

# Route to return JSON data
@views.route("/json")
def get_json():
    return jsonify({
        "name": "Moyo",
        "age": 79
    })

# Route to redirect to the home page
@views.route("/go_home")
def go_home():
    return redirect(url_for("views.home"))

# Route to redirect to the JSON endpoint
@views.route("/go_json")
def go_json():
    return redirect(url_for("views.get_json"))

# Route to redirect to the profile page
@views.route("/go_profile")
def go_profile():
    return redirect(url_for("views.profile"))
