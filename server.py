from flask import Flask
app = Flask(__name__)
@app.route("/contact")
def index():
    return "<h1>hello world</h1>"

app.run(debug=True)