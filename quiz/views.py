from quiz import app
from flask import render_template
from models import Aluno

aluno = Aluno()

@app.route("/")
def index():
	return "Hello World!"

@app.route("/salvaraluno/")
def salvaraluno():
	joao = {'nome':'Jose Filho'}
	aluno.gravarAluno(joao)
	return 'Salvei o aluno'

@app.route('/mostraralunos/')
def mostraralunos():
	dados = aluno.exibirAlunos()
	return render_template('index.html', dados=dados)

@app.route('/excluiralunos/')
def excluiralunos():
	aluno.excluirTodosAlunos()
	return render_template('alunosExcluidos.html')
