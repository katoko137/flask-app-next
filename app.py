from flask import Flask, render_template, redirect, request
import random

app = Flask(__name__)

# 仮のデータ
players = []  # 参加者の名前を保持
start_button_pressed = False  # スタートボタンが押されたかどうか

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
    # スタートボタンが押された状態をTrueに設定
    global start_button_pressed
    start_button_pressed = True
    return "OK", 200

@app.route("/game/<string:username>")
def game(username):
    # クイズの問題をランダムに取得
    question = random.choice(quiz_data)
    return render_template("game.html", question=question, username=username)

@app.route("/check_start_button")
def check_start_button():
    # スタートボタンが押されたかどうかの状態を返す
    return {"start_button_pressed": start_button_pressed}

if __name__ == "__main__":
    app.run(debug=True)
