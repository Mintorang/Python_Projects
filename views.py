from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home_():
    return """
    Thank You For Going onto 127.0.1:8000

    Have A Good Time. 
    
    Thank You!
    
    
    """
    return render_template("index.html", name="Moyo Ehindero")


@views.route("/profile/<username>")
def profile_username(username):


    return render_template("index.html", name=username)

@views.route("/profile")
def profile():
    return "Please enter your username after the slash after profile example: /profile/exampleusername"
@views.route("/json")
def get_json():
    return jsonify({

        "name" : "Moyo", 
        "age" : 79
    })

@views.route("/go_home")
def go_home():
    return redirect(url_for("views.home_"))
@views.route("/go_json")
def go_json():

    return redirect(url_for("views.get_json"))
@views.route("/go_profile")
def go_profile():
    
    return redirect(url_for("views.profile"))






