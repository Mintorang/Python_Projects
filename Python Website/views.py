from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home_():
    return render_template("home.html")
    



@views.route("/profile")
def profile():
    return render_template("profile.html")
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






