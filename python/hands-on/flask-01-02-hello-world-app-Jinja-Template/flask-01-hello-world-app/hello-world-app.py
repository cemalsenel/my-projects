from flask import Flask 

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi Jimmy, we'll handle your problem in the break time"

@app.route("/second")
def second():
    return "This is the second page"

@app.route('/third/subthird')
def third():
    return "I think Jimmy understood this topic"

@app.route("/forth/<string:id>")
def forth(id):
    return f"Id of this page is {id}"

if __name__=="__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=80)