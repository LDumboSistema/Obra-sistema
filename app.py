from flask import Flask, request, render_template, redirect, url_for
import sqlite3, os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/fotos'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def init_db():
    with sqlite3.connect('database/funcionarios.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                bi TEXT,
                cargo TEXT,
                setor TEXT,
                data_entrada TEXT,
                data_saida TEXT,
                estado TEXT,
                motivo_saida TEXT,
                foto TEXT
            )
        """)
        conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    bi = request.form['bi']
    cargo = request.form['cargo']
    setor = request.form['setor']
    data_entrada = request.form['data_entrada']
    estado = request.form['estado']
    motivo_saida = request.form.get('motivo_saida', '')
    data_saida = request.form.get('data_saida', '')

    foto = request.files['foto']
    filename = ''
    if foto:
        filename = secure_filename(foto.filename)
        foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    with sqlite3.connect('database/funcionarios.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO funcionarios (nome, bi, cargo, setor, data_entrada, data_saida, estado, motivo_saida, foto)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (nome, bi, cargo, setor, data_entrada, data_saida, estado, motivo_saida, filename))
        conn.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
