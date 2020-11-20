import sqlite3
test_bd = 'testdb.sqlite3'

class BDBot():

    def __init__(self):
        self.con = sqlite3.connect(test_bd)
        with self.con:
            self.cur = self.con.cursor()
            self.cur.execute("CREATE TABLE IF NOT EXISTS game ("
                        "id INTEGER PRIMARY KEY,"
                        "chat_id INTEGER UNIQUE NOT NULL)")
            self.con.commit()

    def new_game(self, chat_id):
        entities = (chat_id,)
        sql = "INSERT INTO game (chat_id) VALUES(?)"
        print(sql, chat_id)
        self.cur.execute(sql, entities)
        self.con.commit()

    def delete_game(self, chat_id):
        entities = (chat_id,)
        sql = "DELETE FROM game WHERE chat_id=({});".format(chat_id)
        self.cur.execute(sql)
        self.con.commit()


    def read_table(self):
        sql = "SELECT * FROM game"
        self.cur.execute(sql)
        all_results = self.cur.fetchall()
        return all_results



vv = BDBot()
vv.new_game(212)
vv.new_game(21)
print(*vv.read_table())
vv.delete_game(21)
print(*vv.read_table())