import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# criando conexão com banco de dados
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# criando tabela
Base = declarative_base()

class Aluno(Base):
    __tablename__ = "alunos"

    # definindo campos da tabela
    ra = Column("ra", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    sobrenome = Column("sobrenome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # definindo atributos da classe
    def __init__(self, nome: str, sobrenome: str, email: str, senha: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

# criando tabela no banco de dados
Base.metadata.create_all(bind=MEU_BANCO)

def criar():
    print("solicitando dados para o aluno.")
    inserir_nome = input("digite seu nome: ")
    inserir_sobrenome = input("digite seu sobrenome: ")
    inserir_email = input("digite seu e-mail: ")
    inserir_senha = input("digite sua senha: ")

    aluno = Aluno(nome=inserir_nome, sobrenome=inserir_sobrenome, email=inserir_email, senha=inserir_senha)
    session.add(aluno)
    session.commit()

def consultar():
    print("\nexibindo dados de todos os clientes.")
    lista_alunos = session.query(Aluno).all()

    for aluno in lista_alunos:
        print(f"{aluno.ra} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")

os.system("cls || clear")

while True:
    print("código \t descrição")
    print("1 \t adicionar aluno")
    print("2 \t consultar aluno")
    print("3 \t atualizar aluno")
    print("4 \t deletar aluno")
    resposta = int(input("informe o código desejado: \n"))
    
    match(resposta):
        case 1:
            criar()
        case 'R':
            consultar()




# u - update - update - atualizar
def atualizar():
    print("\natualizando dados do usuário")
    email_aluno = input("digite o e-mail do aluno que será atualizado: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        aluno.nome = input("digite seu nome: ")
        aluno.sobrenome = input("digite seu sobrenome: ")
        aluno.email = input("digite seu e-mail: ")
        aluno.senha = input("digite sua senha: ")

        session.commit()
    else:
        print("cliente não encontrado")

# d - delete - delete - excluir
def excluir():
    print("\nexcluindo um aluno")
    email_aluno = input("digite o e-mail do aluno que será excluído: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        session.delete(aluno)
        session.commit()
    else:
        print("aluno não encontrado")

# r - read - select - consulta
def consultaUnica():
    print("pesquisando os dados de apenas um aluno")
    email_aluno = input("digite o e-mail do aluno: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        print(f"{aluno.id} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")
    else:
        print("aluno não encontrado")

# fechando conexão
session.close()