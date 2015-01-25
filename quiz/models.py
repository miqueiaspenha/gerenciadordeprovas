from pymongo import MongoClient

class Aluno():

	client = MongoClient()
	db = client.quiz
	collection = db.aluno

	def gravarAluno(self, aluno):
		self.collection.insert(aluno)

	def exibirAlunos(self):
		return self.collection.find()

	def excluirTodosAlunos(self):
		return self.collection.remove()