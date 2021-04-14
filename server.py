from flask import Flask, render_template
import random
import requests
import datetime

GENDER_URL = "https://api.genderize.io"
AGE_URL = "https://api.agify.io"

app = Flask(__name__)


@app.route('/')
def home_page():
    current_year = datetime.datetime.now().year
    random_number = random.randint(0, 9)
    return render_template("index.html", num=random_number, year=current_year)


@app.route('/guess/<name>')
def guess_page(name):

    parameter = {
        "name": f"{name}"
    }
    gender_request = requests.get(url=GENDER_URL, params=parameter)
    age_request = requests.get(url=AGE_URL, params=parameter)
    name_gender = gender_request.json()["gender"]
    name_age = age_request.json()["age"]

    return render_template("guess.html", name=name, gender=name_gender, age=name_age)


@app.route("/blog/<number>")
def blog_page(number):
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    blog_posts = requests.get(url=blog_url).json()

    return render_template("blog.html", posts=blog_posts, num=number)


if __name__ == "__main__":
    app.run(debug=True)
