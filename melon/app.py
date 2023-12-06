import os
import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from bs4 import BeautifulSoup

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'melon.db')



db = SQLAlchemy(app)

class Melon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'{self.rank}등 {self.artist} {self.title} 추천 by {self.username}'

@app.route('/')
def home():
    url = "https://www.melon.com/chart/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    melon = []
    trs = soup.select('table > tbody > tr')
    for tr in trs:
        rank = tr.select_one('.rank').text
        title = tr.select_one('.rank01 > span > a').text
        artist = tr.select_one('.rank02 > a').text
        image = tr.select_one('img')['src']
        melon.append({'rank': rank, 'artist': artist, 'title': title, 'image': image})
        song = Melon(username="멜론", rank=rank, title=title, artist=artist, image_url=image)
        db.session.add(song)
    db.session.commit()

    return render_template('music.html', data=melon)

if __name__ == "__main__":
    app.run(debug=True)
