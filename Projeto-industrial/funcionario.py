#agora esse arquivo é um modulo que será importado no main.py
#é reponsável por funcionalidades referentes a funcionarios

from database import conectar



def listar_funcionarios():


    #abrir conexão
    conexao = conectar()

    #criar cursor
    cursor = conexao.cursor()

    #sql da consulta
    sql = """
    select 
        f.id_funcionario,
        f.nome,
        f.cargo,
        s.nome as setor
    from funcionario f
    join setor s on f.id_setor = s.id_setor
    """

    #executa sql
    cursor.execute(sql)

    #recuperar dados
    dados = cursor.fetchall()

    #exibir dados
    for funcionario in dados:
        print(funcionario)

    #fechar a conexão
    cursor.close()
    conexao.close()

def cadastrar_funcionario(nome, cargo, id_setor): 


    #abrir conexão
    conexao = conectar()

    #criar cursor
    cursor = conexao.cursor()

    #sql de inserção
    sql = """
    insert into funcionario (nome, cargo, id_setor)
    values (%s, %s, %s)
    """

    #valores a serem inseridos
    valores = (nome, cargo, id_setor)

    #executa sql
    cursor.execute(sql, valores)

    #confirma a transação
    conexao.commit()

    print(f"Funcionário {nome} cadastrado com sucesso!")

    #fechar a conexão
    cursor.close()
    conexao.close()

def atualizar_funcionario(id_funcionario, nome, cargo, id_setor):

    #abrir conexão
    conexao = conectar()

    #criar cursor
    cursor = conexao.cursor()

    #sql de atualização
    sql = """
    update funcionario
    set nome = %s, cargo = %s, id_setor = %s
    where id_funcionario = %s
    """

    #valores a serem atualizados
    valores = (nome, cargo, id_setor, id_funcionario)

    #executa sql
    cursor.execute(sql, valores)

    #confirma a transação
    conexao.commit()

    print(f"Funcionário {id_funcionario} atualizado com sucesso!")

    #fechar a conexão
    cursor.close()
    conexao.close()

def deletar_funcionario():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    delete from funcionario
    where id_funcionario = %s
    """

    cursor.close()
    conexao.close()