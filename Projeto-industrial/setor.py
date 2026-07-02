from database import conectar


def listar_setor():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    select * from setor
    """
    cursor.execute(sql)
    dados = cursor.fetchall()

    for setor in dados:
        print(setor)

    cursor.close()
    conexao.close()

def cadastrar_setor(nome):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    insert into setor (nome)
    values (%s)
    """
    valores = (nome,)
    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Setor {nome} cadastrado com sucesso!")

    cursor.close()
    conexao.close()

def atualizar_setor(id_setor, nome):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    update setor
    set nome = %s
    where id_setor = %s
    """
    valores = (nome, id_setor)
    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Setor {id_setor} atualizado com sucesso!")

    cursor.close()
    conexao.close()

def deletar_setor(id_setor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    delete from setor
    where id_setor = %s
    """
    valores = (id_setor,)
    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Setor {id_setor} deletado com sucesso!")

    cursor.close()
    conexao.close()