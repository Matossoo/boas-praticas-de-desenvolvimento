from funcionario import cadastrar_funcionario, listar_funcionarios, atualizar_funcionario, deletar_funcionario

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