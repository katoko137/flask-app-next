from flask import Flask, render_template, redirect, request
import random

app = Flask(__name__)

# 仮のデータ
players = []  # 参加者の名前を保持
players_ready = []  # スタートボタンを押したユーザーのリスト
quiz_data = [
    {"question": "2 + 2 = 4 ?", "answer": "〇"},
    {"question": "5 - 3 = 2 ?", "answer": "〇"},
    {"question": "3 * 3 = 9 ?", "answer": "〇"},
    {"question": "10 / 2 = 4 ?", "answer": "×"}
]

@app.route("/")
def index():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    # ユーザー名を取得してリストに追加
    username = request.form.get('username')
    if username not in players:
        players.append(username)
    return redirect(f"/waiting_room/{username}")

@app.route("/waiting_room/<string:username>")
def waiting_room(username):
    # 参加者のリストを表示
    return render_template("waiting_room.html", players=players, username=username)

@app.route("/start_game", methods=["POST"])
def start_game():
    # 参加者がスタートボタンを押す
    username = request.form.get('username')
    
    # ユーザーが既にスタートボタンを押しているか確認
    if username not in players_ready:
        players_ready.append(username)
    
    # 全員がスタートボタンを押したか確認
    if len(players_ready) == len(players):
        return redirect("/game")
    
    # まだスタートボタンを押していない場合はそのまま待機
    return redirect(f"/waiting_room/{username}")

@app.route("/game")
def game():
    # クイズの問題をランダムに取得
    question = random.choice(quiz_data)
    return render_template("game.html", question=question)

if __name__ == "__main__":
    app.run(debug=True)
