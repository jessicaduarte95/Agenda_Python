# Criando uma agenda com Python.

import os
import sqlite3
from sqlite3 import Error

# Criando Conexão com o Banco.

def conexaoBanco():
    caminho = "C:\\Users\\jessica\\Documents\\Treino_python\\Agenda_python\\agendabanco.db"
    con = None
    try: 
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = conexaoBanco()

# Criando o Menu Principal.

def menuPrincipal():
    os.system("cls")
    print("1 - Inserir Novo Registro.")
    print("2 - Deletar Registro.")
    print("3 - Atualizar Registro.")
    print("4 - Consultar Registro.")
    print("5 - Consultar Registro por Nome.")
    print("6 - Sair.")

# Inserir, deletar e atualizar.

def query(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Operação realizada com sucesso.")
    except Error as ex:
        print(ex)
    finally:
        print("Operação realizada com sucesso.")
       # conexao.close()

# Consultar.

def consultar(conexao,sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    return res

# Opção 01 -> Inserir.

def inserir():
    os.system("cls")
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    vsql = "INSERT INTO tb_contatos  (Nome, Telefone, Email) VALUES('"+nome+"', '"+telefone+"', '"+email+"')"
    query(vcon,vsql)


# Opção 02 -> Deletar.

def deletar():
    os.system("cls")
    id = input("Digite o ID do registro que você deseja deletar: ")
    vsql = "DELETE FROM tb_contatos WHERE ID = "+id
    query(vcon,vsql)

# Opção 03 -> Atualizar.

def atualizar():
    os.system("cls")
    id = input("Qual ID você deseja atualizar: ")
    r = consultar(vcon,"SELECT * FROM tb_contatos WHERE ID="+id)
    rnome = r[0][1]
    rtelefone = r[0][2]
    remail = r[0][3]
    nome = input("Digite o nome que você deseja atualizar: ")
    telefone = input("Digite o telefone que você deseja atualizar: ")
    email = input("Digite o email que você deseja atualizar: ")
    if (len(nome) == 0):
        nome = rnome
    if (len(telefone) == 0):
        telefone = rtelefone
    if (len(email) == 0):
        email = remail
    vsql = "UPDATE tb_contatos SET Nome = '"+nome+"', Telefone = '"+telefone+"', Email = '"+email+"' WHERE ID="+id
    query(vcon,vsql)

# Opção 04 -> Consultar.

def consultarRegistro():
    vsql = "SELECT * FROM tb_contatos"
    res = consultar(vcon,vsql)
    lim = 10
    cont = 0
    for r in res:
        print("ID: {0:_<3} Nome: {1:_<30} Telefone: {2:_<15} Email: {3:_<30}".format(r[0],r[1],r[2],r[3]))
        cont+=1
        if(cont >= lim):
            cont = 0
            os.system("pause")
            os.system("cls")
    print("Fim da lista.")
    os.system("pause")

    
# Opção 05 -> Consultar nomes.

def consultarNome():
    nome = input("Digite o nome: ")
    vsql = "SELECT * FROM tb_contatos WHERE Nome LIKE '%"+nome+"%'"
    res = consultar(vcon,vsql)
    lim = 10
    cont = 0
    for r in res:
        print("ID: {0:_<3} Nome: {1:_<30} Telefone: {2:_<15} Email: {3:_<30}".format(r[0],r[1],r[2],r[3]))
        cont+=1
        if(cont >= lim):
            cont = 0
            os.system("pause")
            os.system("cls")
    print("Fim da lista.")
    os.system("pause")


opc = 0

while opc != 6:
    menuPrincipal()
    opc = int(input("Digite uma opção: "))
    if opc == 1:
        inserir()
    elif opc == 2:
        deletar()
    elif opc == 3:
        atualizar()
    elif opc == 4:
        consultarRegistro()
    elif opc == 5:
        consultarNome()
    elif opc == 6:
        os.system("cls")
        print("Programa Finalizado.")
    else:
        os.system("cls")
        print("Opção Inválida.")
        os.system("pause")

vcon.close()
os.system("pause")
