def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(menu)
def depositar(saldo,valor,extrato):
    if valor > 0 :
        saldo = saldo + valor
        extrato += f'Extrato --> Saldo atual {saldo}'
        print("Depósito realizado com sucesso !")
    else:
        print("Depósito sem sucesso")
    
    return saldo, extrato

def sacar(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite")

    elif excedeu_saques:
        print( "Operação falhou! Número máximo de saques excedido")

    elif valor > 0:
        saldo = saldo - valor
        extrato += f"Saque: R$ {valor:.2f}"
        numero_saques += 1
        print(" Saque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido")
    
    return saldo, extrato
    
def exibir_extrato(saldo,extrato):
    print("-------------------EXTRATO--------------------")
    if not extrato:
        print("Não foram realizadas movimentações")
    else:
        print(extrato)
        print(f"Saldo --> {saldo}")
def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF --->>")
    usuario = filtrar_usuarios(cpf,usuarios)

    if usuario:
        
        return print("Usuário já existe")
    else:
        nome = input("Digite o nome do usuário -->")
        nascimento = input("Digite a data de nascimento (DD/MM/YY) -->")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        
        usuarios.append({"nome": nome, "data_nascimento": nascimento, "cpf": cpf, "endereco": endereco})
        print("Usuário criado com sucesso !")
def criar_conta(agencia,numero_conta,usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print(" Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrado")

def filtrar_usuarios(cpf,usuarios):
    filtro = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    if len(filtro) == 0:
        return None
    else:
        return filtro[0]
def listar_contas(contas):
    linha = ""
    for conta in contas:
        linha += f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
    print(linha)



def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()