import sqlite3

# データベース接続の関数
def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

# quizテーブルを作成する関数
def create_table():
    conn = create_connection('quiz.db')
    cursor = conn.cursor()
    
    # テーブル作成SQL
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS quiz (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT unique,
        answer BOOLEAN
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username text unique
    );
    ''')
    conn.commit()
    conn.close()

# データベース接続とテーブル作成を実行
if __name__ == '__main__':
    create_table()
