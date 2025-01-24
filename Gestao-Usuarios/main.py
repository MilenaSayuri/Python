from flask import Flask, url_for, render_template

#inicializacao
app = Flask(__name__)

#rotas
@app.route("/")
def hello():
    titulo = 'Gestao de Usuario'
    usuario = [
        {'nome': 'Milena', 'membro_ativo': True},
        {'nome': 'Caio', 'membro_ativo': False},      
        {'nome': 'Rafaela', 'membro_ativo': True},
    ]
    return render_template('index.html', titulo=titulo, usuario=usuario)

@app.route("/sobre")
def pag_sobre():
    return """"
        <b>ProgramdorPython</b>: Perfil 3D no 
        <a href="https://www.instagram.com/corchc_miittsuki_3d/">Instagram</a>
    """

#execucao
if __name__ == "__main__":
    app.run(debug=True)