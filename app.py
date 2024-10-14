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
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # definindo atributos da classe
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# criando tabela no banco de dados
Base.metadata.create_all(bind=MEU_BANCO)

# CRUD.
# c - create - insert - salvar
os.system("cls || clear")
print("solicitando dados para o cliente.")
inserir_nome = input("digite seu nome: ")
inserir_email = input("digite seu e-mail: ")
inserir_senha = input("digite sua senha: ")

cliente = Cliente(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(cliente)
session.commit()

# r - read - select - consultar
print("\nexibindo dados de todos os clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

# u - update - update - atualizar
print("\natualizando dados do usuário")
email_cliente = input("digite o e-mail do cliente que será atualizado: ")

cliente = session.query(Cliente).filter_by(email = email_cliente).first()

if cliente:
    cliente.nome = input("digite seu nome: ")
    cliente.email = input("digite seu e-mail: ")
    cliente.senha = input("digite sua senha: ")

    session.commit()
else:
    print("cliente não encontrado")

# r - read - select - consultar
print("\nexibindo dados de todos os clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

# d - delete - delete - excluir
print("\nexcluindo um cliente")
email_cliente = input("digite o e-mail do cliente que será excluído: ")

cliente = session.query(Cliente).filter_by(email = email_cliente).first()

if cliente:
    session.delete(cliente)
    session.commit()
else:
    print("cliente não encontrado")

# r - read - select - consultar
print("\nexibindo dados de todos os clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

# r - read - select - consulta
print("pesquisando os dados de apenas um cliente")
email_cliente = input("digite o e-mail do cliente: ")

cliente = session.query(Cliente).filter_by(email = email_cliente).first()

if cliente:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")
else:
    print("cliente não encontrado")

# fechando conexão
session.close()