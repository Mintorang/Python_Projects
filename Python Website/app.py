# from flask import Flask
# from views import views

# app = Flask(__name__)
# #this is a blueprint
# app.register_blueprint(views, url_prefix="/")





# if __name__ == "__main__":
#     app.run(debug=True, port=8000)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)