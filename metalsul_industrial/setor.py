from database import conectar

def criar_setor(nome, descricao):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO setores (nome, descricao) VALUES (%s, %s)"
    cursor.execute(sql, (nome, descricao))
    conexao.commit()
    cursor.close()
    conexao.close()

def listar_setores():
    conexao = conectar()

    cursor = conexao.cursor()

    sql = "SELECT * FROM setores"

    cursor.execute(sql)

    setores = cursor.fetchall()

    for setor in setores:
        print(setor)

    cursor.close()
    conexao.close()

def atualizar_setor(id, nome, descricao):
   conexao = conectar()

   cursor = conexao.cursor()

   sql = "UPDATE setores SET nome = %s, descricao = %s WHERE id = %s"

   cursor.execute(sql, (nome, descricao, id))

   conexao.commit()

   cursor.close()
   conexao.close()

def deletar_setor(id):
   conexao = conectar()

   cursor = conexao.cursor()

   sql = "DELETE FROM setores WHERE id = %s"

   cursor.execute(sql, (id,))

   conexao.commit()

   cursor.close()
   conexao.close()
