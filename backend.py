import sqlite3

def connect():
    conn=sqlite3.connect("plantings.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS plants (id INTEGER PRIMARY KEY, crop text, quantity int, plant_date datetime, outcome text, notes text)")
    conn.commit()
    conn.close()

def insert(crop, quantity, plant_date, outcome, notes):
    conn=sqlite3.connect("plantings.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO plants VALUES (NULL,?,?,?,?,?)",(crop, quantity, plant_date, outcome, notes))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("plantings.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM plants")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(crop="", quantity="", plant_date="", outcome=""):
    conn=sqlite3.connect("plantings.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM plants WHERE crop=? or quantity=? or plant_date=? or outcome=?",(crop,quantity,plant_date,outcome))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("plantings.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM plants WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,crop="", quantity="", plant_date="", outcome="", notes=""):
    conn=sqlite3.connect("plantings.db")
    cur=conn.cursor()
    cur.execute("UPDATE plants SET crop=?, quantity=?, plant_date=?, outcome=?, notes=? WHERE id=?" ,(crop,quantity,plant_date,outcome,notes,id))
    conn.commit()
    conn.close()

connect()
# insert("Potato",12,"March15,2017","Epic Fail!","We thought we were planting tomatoes.")
# update(3,"Broccoli",5,"April2,2017","meh","small crowns but predation was acceptible")
