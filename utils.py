from models import Pessoas, Usuarios

#INSERE DADOS NA TABELA pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Paula', idade=42)
    print(pessoa)
    pessoa.save()

def insere_usuario(login, senha):
    usario = Usuarios(login=login, senha=senha)
    usario.save()

def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

#CONSULTA DADOS NA TABELA pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    # for i in pessoa:
    #     print(i.nome)
    pessoa = Pessoas.query.filter_by(nome='Ale').first()
    print(pessoa.idade)

#ALTERA DADOS NA TABELA pessoa
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Ale').first()
    pessoa.nome = 'Sandrinho'
    pessoa.idade = 101
    pessoa.save()

#EXCLUI DADOS NA TABELA pessoa
def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Paula').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoas()
    #consulta_pessoas()
    #exclui_pessoas()
    consulta_pessoas()
    #insere_usuario('pal', '123')
    #consulta_usuarios()