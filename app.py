from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def Home_index():
    name = "Taro"
    return render_template("index.html", title="flask test", name=name)



@app.route("/reference")
def My_reference():
    return render_template("reference.html", title="Reference_mypage",)



if __name__ == '__main__':
    app.run(debug=True)
