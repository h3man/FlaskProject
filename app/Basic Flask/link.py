from flask import Flask, redirect, url_for,render_template
app=Flask(__name__)
@app.route("/")
def index():
    name="Python Flask Workshop"

    return render_template("tmp.html",name1=name)
@app.route("/list")
def list():
    a=[132,144,343]
    return render_template("tmp.html",name2=a)
@app.route("/dict")
def dict():
    dict={0:"hemanshu",1:"Arjun"}
    return render_template("tmp.html",name3=dict)
if __name__=="__main__":
    app.run(debug=True)
