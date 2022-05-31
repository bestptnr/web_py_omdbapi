from flask import Flask, render_template,request,url_for
import json
import requests
app = Flask(__name__)


@app.route("/",methods=["GET","POST"])

def movie():
    if request.method == "GET":
        search = dict()
        return render_template("index.html",data = search)
    if request.method == "POST":
        name = request.form['url']
        new_apiurl = "http://www.omdbapi.com/?apikey=3f968d6e&s="+name
        new_result = json.loads(requests.get(new_apiurl).text)
        search = []
        search = new_result['Search']
        return render_template("index.html",data = search)

if __name__ == "__main__":
    app.run(debug=True)
