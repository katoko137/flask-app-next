# userテーブルの全削除
import sqlite3

def deleteUser():
    # データベースに接続
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    # 全行を削除
    cursor.execute("DELETE FROM user")

    # 変更を保存
    conn.commit()

    # 接続を閉じる
    conn.close()
