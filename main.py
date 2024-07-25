from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def homepage():
    url = "https://api.npoint.io/1fa827e6600c6d33289f"
    response = requests.get(url)
    all_data = response.json()
    return render_template("index.html", data=all_data)

@app.route("/index")
def indexpage():
    url = "https://api.npoint.io/1fa827e6600c6d33289f"
    response = requests.get(url)
    all_data = response.json()
    return render_template("index.html", data=all_data)

@app.route("/contact")
def contactpage():
    return render_template("contact.html")

@app.route("/about")
def aboutpage():
    return render_template("about.html")

@app.route("/<int:num>")
def get_post(num):
    url = "https://api.npoint.io/1fa827e6600c6d33289f"
    response = requests.get(url)
    all_data = response.json()
    for n in all_data:
        if n["id"] == num:
            title = n["title"]
            subtitle = n["subtitle"]
            img = n["image_url"]
            name = n['author']
            date= n['date']
            para= n['body']
            return render_template("post.html", title=title,subtitle=subtitle,img=img,name=name,date=date,para=para)


if __name__ == "__main__":
    app.run(debug=True)