blog_url = "https://api.npoint.io/5f4ada92b2082a2bb41d"

from flask import Flask, render_template
from post import Post
import requests

posts = requests.get(blog_url).json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["content"])
    post_objects.append(post_obj)

print(post_objects[0].content)


app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)


@app.route("/post/<int:index>")
def show_post(index):
    return render_template("post.html", post=post_objects[index])


if __name__ == "__main__":
    app.run(debug=True)