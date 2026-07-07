#from funcionario import cadastrar_funcionario, listar_funcionarios, atualizar_funcionario, deletar_funcionario
#from setor import criar_setor, listar_setores, atualizar_setor, deletar_setor
from fornecedor import cadastrar_fornecedor, listar_fornecedores, atualizar_fornecedor, deletar_fornecedor
#from produto import cadastrar_produto, listar_produtos, atualizar_produto, deletar_produto
"""
while True:

    print("\n====== SISTEMA INDUSTRIAL ======")
    print("1 - Listar funcionários")
    print("2 - Cadastrar funcionário")
    print("3 - Atualizar salário")
    print("4 - Remover funcionário")
    print("0 - Sair")

    opcao=input("\nEscolha uma opção: ")

    if opcao == "1":

        listar_funcionarios()

    elif opcao == "2":

        nome = input("Digite o nome do funcionário: ")
        cpf = input("Digite o CPF do funcionário: ")
        cargo = input("Digite o cargo do funcionário: ")
        salario = float(input("Digite o salário do funcionário: "))
        data_admissao = input("Digite a data de admissão do funcionário (YYYY-MM-DD): ")
        id_setor = int(input("Digite o ID do setor do funcionário: "))
        cadastrar_funcionario(nome, cpf, cargo, salario, data_admissao, id_setor)

    elif opcao == "3":

        id_funcionario = int(input("Digite o ID do funcionário que deseja atualizar o salário: "))
        novo_salario = float(input("Digite o novo salário: "))
        atualizar_funcionario(id_funcionario, novo_salario)

    elif opcao == "4":

        id_funcionario = int(input("Digite o ID do funcionário que deseja remover: "))
        deletar_funcionario(id_funcionario)

    elif opcao == "0":

        print("Saindo do sistema...")
        break

while True:
    print("\n====== SISTEMA INDUSTRIAL ======")
    print("1 - Listar setores")
    print("2 - Cadastrar setor")
    print("3 - Atualizar setor")
    print("4 - Remover setor")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        listar_setores()

    elif opcao == "2":
        nome = input("Digite o nome do setor: ")
        descricao = input("Digite a descrição do setor: ")
        criar_setor(nome, descricao)

    elif opcao == "3":
        id_setor = int(input("Digite o ID do setor que deseja atualizar: "))
        nome = input("Digite o novo nome do setor: ")
        descricao = input("Digite a nova descrição do setor: ")
        atualizar_setor(id_setor, nome, descricao)

    elif opcao == "4":
        id_setor = int(input("Digite o ID do setor que deseja remover: "))
        deletar_setor(id_setor)

    elif opcao == "0":
        print("Saindo do sistema...")
        break
"""
while True:

    print("\n====== SISTEMA INDUSTRIAL ======")
    print("1 - Listar Fornecedores")
    print("2 - Cadastrar Fornecedor")
    print("3 - Atualizar Fornecedor")
    print("4 - Remover Fornecedor")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        listar_fornecedores()

    elif opcao == "2":
        nome = input("Digite o nome do fornecedor: ")
        cnpj = input("Digite o CNPJ do fornecedor: ")
        endereco = input("Digite o endereço do fornecedor: ")
        telefone = input("Digite o telefone do fornecedor: ")
        cadastrar_fornecedor(nome, cnpj, endereco, telefone)

    elif opcao == "3":
        id_fornecedor = int(input("Digite o ID do fornecedor que deseja atualizar: "))
        nome = input("Digite o novo nome do fornecedor: ")
        cnpj = input("Digite o novo CNPJ do fornecedor: ")
        endereco = input("Digite o novo endereço do fornecedor: ")
        telefone = input("Digite o novo telefone do fornecedor: ")
        atualizar_fornecedor(id_fornecedor, nome, cnpj, endereco, telefone)

    elif opcao == "4":
        id_fornecedor = int(input("Digite o ID do fornecedor que deseja remover: "))
        deletar_fornecedor(id_fornecedor)

    elif opcao == "0":
        print("Saindo do sistema...")
        break