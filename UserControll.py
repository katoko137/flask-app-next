class UserControll:
    def __init__(self, db):
        self.db = db
    
    def insertUser(self, username):
        cur = self.db.cursor()
        sql = "insert into user (username) values(?)"
        data = (username, )
        try:
            cur.execute(sql, data)
            self.db.commit()
            return 1
        except Exception as e:
            print(e)
            return 0

    def getUsers(self):
        cur = self.db.cursor()
        sql = "select username from user"
        cur.execute(sql)
        res = cur.fetchall()
        res = [user[0] for user in res]
        return res
        

