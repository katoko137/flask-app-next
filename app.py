from flask import Flask, render_template, redirect, request
from flask_socketio import SocketIO, emit
from UserControll import UserControll
import sqlite3
from deleteUser import deleteUser
from database import create_table

# user tableを初期化
create_table()
deleteUser()
print("はじまったよ")

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

players = []
player_info = []

db = sqlite3.connect("quiz.db", check_same_thread=False)
uc = UserControll(db)

def update_players():
    global players
    players = uc.getUsers()

def update_players_info():
    global players_info
    players_info = []

@app.route("/")
def index():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    # ユーザー名の取得
    username = request.form.get('username')
    # データベースにユーザーの登録
    res = uc.insertUser(username)
    if not res:
        print("=====================")
        print("名前が重複しています")
        print("====================")
    return redirect(f"/waiting_room/{username}")

@app.route("/waiting_room/<string:username>")
def waiting_room(username):
    # playersの更新
    update_players()
    return render_template("waiting_room.html", players=players, username=username)

@app.route("/game/<string:username>")
def game(username):
    return render_template("game.html", players=players, username=username, )

@socketio.on('start_game')
def start_game():
    update_players_info()
    print("スタートゲーム")
    emit('start_game_f', {}, broadcast=True)


if __name__ == "__main__":
    socketio.run(app,port=10000,debug=False)
