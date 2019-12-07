import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS notes (id INTENGER PRIMARY KEY, title text, body text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM notes")
        rows = self.cur.fetchall()
        return rows

    def insert(self, title, body):
        self.cur.execute("INSERT INTO notes VALUES(NULL, ?,?)",(title, body))
        self.conn.commit()

    def remove(self,id):
        self.cur.execute("DELETE FROM notes WHERE id=?"(id,))
        self.conn.commit()

    def update(self, id, part,customer, retailer, price):
        self.cur.execute("UPDATE notes SET title = ?,body = ? WHERE ID =?",(notes,title, id))
        self.conn.commit()

    def __del__ (self):
        self.conn.close()

db = Database('notas.db')
db.insert("estudar testes unitarios","procurar algum bom livro sobre testes unitarios e fazer os exercicios")
db.insert("terminar cursos", "terminar curso de golang no udemy e curso de tensor flow no udacity")
db.insert("separar 30 reais", "grana pra ir no evento no bar do niquinho dia 14")


