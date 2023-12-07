# 필수 라이브러리
'''
0. Flask : 웹서버를 시작할 수 있는 기능. app이라는 이름으로 플라스크를 시작한다
1. render_template : html파일을 가져와서 보여준다
'''
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import unquote

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
#DB code

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(10000), nullable=False)

    def __repr__(self):
        return f'{self.title} {self.artist} 추천 by {self.username}'

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    name = '최지웅'
    motto = "행복해서 웃는게 아니라 웃어서 행복합니다."

    context = {
        "name": name,
        "motto": motto,
    }
    return render_template('motto.html', data=context)

@app.route("/music/")
def music():
    song_list = Song.query.all()
    return render_template('music.html', data=song_list)

@app.route("/music/<username>/")
def render_music_filter(username):
    filter_list = Song.query.filter_by(username=username).all()
    return render_template('music.html', data=filter_list)

@app.route('/music/create/')
def music_create():
    username_receive = unquote(request.args.get('username'))
    title_receive = unquote(request.args.get('title'))
    artist_receive = unquote(request.args.get('artist'))
    image_receive = unquote(request.args.get('image_url'))

    #data save to DB
    song = Song(username=username_receive, title=title_receive, artist=artist_receive, image_url=image_receive)
    db.session.add(song)
    db.session.commit()

    return redirect(url_for('render_music_filter', username=username_receive))
if __name__ == "__main__":
    app.run(debug=True)