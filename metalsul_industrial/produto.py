from database import conectar

def listar_produto(nome, descricao, preco, setor_id):
    conexao = conectar()

    cursor = conexao.cursor()

    sql = """
    select 
        p.id_produto,
        p.nome,
        p.descricao,
        p.preco,
        s.nome as setor
    from produto p
    join setor s on p.setor_id = s.id_setor
    where (%s is null or p.nome ilike %s) and
          (%s is null or p.descricao ilike %s) and
          (%s is null or p.preco = %s) and
          (%s is null or p.setor_id = %s)
    """

    cursor.execute(sql, (nome, nome, descricao, descricao, preco, preco, setor_id, setor_id))
    dados = cursor.fetchall()

    for produto in dados:
        print(produto)

    cursor.close()
    conexao.close()

def cadastrar_produto(nome, descricao, preco, setor_id):
    conexao = conectar()

    cursor = conexao.cursor()

    sql = """
    insert into produto (nome, descricao, preco, setor_id)
    values (%s, %s, %s, %s)
    """

    valores = (nome, descricao, preco, setor_id)

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Produto {nome} cadastrado com sucesso!")

    cursor.close()
    conexao.close()

def atualizar_produto(id_produto, nome, descricao, preco, setor_id):
    conexao = conectar()

    cursor = conexao.cursor()

    sql = """
    update produto
    set nome = %s,
        descricao = %s,
        preco = %s,
        setor_id = %s
    where id_produto = %s
    """

    valores = (nome, descricao, preco, setor_id, id_produto)

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Produto {id_produto} atualizado com sucesso!")

    cursor.close()
    conexao.close()

def deletar_produto(id_produto):
    conexao = conectar()

    cursor = conexao.cursor()

    sql = "delete from produto where id_produto = %s"

    cursor.execute(sql, (id_produto,))
    conexao.commit()

    print(f"Produto {id_produto} deletado com sucesso!")

    cursor.close()
    conexao.close()




