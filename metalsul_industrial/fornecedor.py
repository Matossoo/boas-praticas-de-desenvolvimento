from database import conectar

def listar_fornecedores():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT id_fornecedor, razao_social, cnpj, telefone, cidade FROM fornecedor"
    cursor.execute(sql)
    fornecedores = cursor.fetchall()

    for fornecedor in fornecedores:
        print(fornecedor)

    cursor.close()
    conexao.close()

def cadastrar_fornecedor(razao_social, cnpj, telefone, cidade):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO fornecedor (razao_social, cnpj, telefone, cidade) VALUES (%s, %s, %s, %s)"
    valores = (razao_social, cnpj, telefone, cidade)
    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Fornecedor {razao_social} cadastrado com sucesso!")

    cursor.close()
    conexao.close()

def atualizar_fornecedor(id_fornecedor, razao_social, cnpj, telefone, cidade):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "UPDATE fornecedor SET razao_social = %s, cnpj = %s, telefone = %s, cidade = %s WHERE id_fornecedor = %s"
    valores = (razao_social, cnpj, telefone, cidade, id_fornecedor)
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

