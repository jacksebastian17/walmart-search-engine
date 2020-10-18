from flask import Flask, redirect, url_for, render_template, request
import os

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, './')

app = Flask(__name__, template_folder=template_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=["POST", "GET"])
def search():
    if request.method == "POST":
        query = request.form["nm"]
        return redirect(url_for("query", qry=query))
    else:
        return render_template('search.html')

@app.route('/<qry>')
def query(qry):
    return f"<h1>{qry}</h1>"



if __name__ == '__main__':
    app.run(debug=True)