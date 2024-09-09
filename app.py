from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def hello():
    user_agent = request.headers.get('User-Agent')
    is_android = 'Android' in user_agent
    return render_template("index.html", is_android=is_android)

if __name__ == '__main__':
    app.run(debug=True)

