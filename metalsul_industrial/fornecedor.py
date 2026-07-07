from database import conectar

def listar_fornecedores():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM fornecedor"
    cursor.execute(sql)
    fornecedores = cursor.fetchall()

    for fornecedor in fornecedores:
        print(fornecedor)

    cursor.close()
    conexao.close()

def cadastrar_fornecedor(nome, cnpj, endereco, telefone):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO fornecedor (nome, cnpj, endereco, telefone) VALUES (%s, %s, %s, %s)"
    valores = (nome, cnpj, endereco, telefone)
    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Fornecedor {nome} cadastrado com sucesso!")

    cursor.close()
    conexao.close()

def atualizar_fornecedor(id_fornecedor, nome, cnpj, endereco, telefone):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "UPDATE fornecedor SET nome = %s, cnpj = %s, endereco = %s, telefone = %s WHERE id_fornecedor = %s"
    valores = (nome, cnpj, endereco, telefone, id_fornecedor)
    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Fornecedor {id_fornecedor} atualizado com sucesso!")

    cursor.close()
    conexao.close()

def deletar_fornecedor(id_fornecedor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM fornecedor WHERE id_fornecedor = %s"
    cursor.execute(sql, (id_fornecedor,))
    conexao.commit()

    print(f"Fornecedor {id_fornecedor} deletado com sucesso!")

    cursor.close()
    conexao.close()

