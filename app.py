from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def create_table():
    conn = sqlite3.connect('notas.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS notas
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       titulo TEXT NOT NULL,
                       mensagem TEXT NOT NULL)''')
    conn.commit()
    conn.close()


@app.route('/inserir', methods=['GET', 'POST'])
def inserir():
    if request.method == 'POST':
        titulo = request.form['titulo']
        mensagem = request.form['mensagem']
        conn = sqlite3.connect('notas.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO notas (titulo, mensagem) VALUES (?, ?)', (titulo, mensagem))
        conn.commit()
        conn.close()
        return '''
            <form method="post">
                <label for="titulo">Título:</label><br>
                <input type="text" id="titulo" name="titulo"><br>
                <label for="mensagem">Mensagem:</label><br>
                <textarea id="mensagem" name="mensagem"></textarea><br>
                <input type="submit" value="Inserir">
            </form>
        '''

@app.route('/show')
def show():
    conn = sqlite3.connect('notas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notas')
    notas = cursor.fetchall()
    conn.close()
    return jsonify(notas)

# Rota para deletar uma nota pelo ID
@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('notas.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM notas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return f'Nota com ID {id} foi excluída.'

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
