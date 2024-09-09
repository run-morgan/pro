from flask import Flask, render_template
import os
os.environ['FLASK_DEBUG'] = '1'

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)