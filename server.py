from flask import Flask, render_template, request, redirect
from werkzeug.utils import redirect

from user import User
app = Flask(__name__)
@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route("/create_form")
def create_form():

    return render_template("create.html")

@app.route("/create", methods=['POST', 'GET'])
def insert():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    User.save(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)