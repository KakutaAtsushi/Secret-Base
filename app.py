from flask import Flask, render_template
from datetime import datetime
from flask_socketio import SocketIO, emit
from flask_sockets import Sockets
# git add .
# git commit -m"1st commit"
# git push heroku master
# 更新手順

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hogehugahage'


@app.route('/')
def Home_index():
    name = "Taro"
    return render_template("index.html", title="flask test", name=name)


@app.route("/reference")
def My_reference():
    return render_template("reference.html", title="Reference_mypage", )


@app.route("/Lambda")
def Lambda_Action():
    return render_template("Lambda.html", title="Lambda_notify")


@app.route("/burst_demo")
def bust_index():
    return render_template("bustabit_demo.html", title="bustabit_demo")


if __name__ == '__main__':
    app.run(debug=True)
