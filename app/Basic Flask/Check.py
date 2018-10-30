from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
        return "Hello world!"
    
@app.route("/about/<name>")
def about(name):
        return "Hello %s!" %name
    
@app.route("/about/<int:age>")
def hi(age):
        return "Your age is: %d!" %age

if __name__=="__main__":
    app.run(debug= True)
