import sqlite3

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS plants (id INTEGER PRIMARY KEY, crop text, quantity int, plant_date datetime, outcome text, notes text)")
        self.conn.commit()

    def insert(self, crop, quantity, plant_date, outcome, notes):
        self.cur.execute("INSERT INTO plants VALUES (NULL,?,?,?,?,?)",(crop, quantity, plant_date, outcome, notes))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM plants")
        rows=self.cur.fetchall()
        return rows

    def search(self, crop="", quantity="", plant_date="", outcome=""):
        self.cur.execute("SELECT * FROM plants WHERE crop=? or quantity=? or plant_date=? or outcome=?",(crop,quantity,plant_date,outcome))
        rows=self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM plants WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id,crop="", quantity="", plant_date="", outcome="", notes=""):
        self.cur.execute("UPDATE plants SET crop=?, quantity=?, plant_date=?, outcome=?, notes=? WHERE id=?" ,(crop,quantity,plant_date,outcome,notes,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# insert("Potato",12,"March15,2017","Epic Fail!","We thought we were planting tomatoes.")
# update(3,"Broccoli",5,"April2,2017","meh","small crowns but predation was acceptible")
