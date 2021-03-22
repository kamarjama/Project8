from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.methods == "POST":
        friendship_percent = random.randint(1, 101)
    friendship_percent = str(friendship_percent)
    return render_template('home.html', friendship=(friendship_percent + "%"))


if __name__ == '__main__':
    app.run(debug=True)
