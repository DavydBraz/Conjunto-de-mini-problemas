#exercicio simples baseado em uma atividade do curso python developer da DIO, seguindo as metricas basicas do mesmo,
#utilizando agora junto de funcoes

saldo=0
LIMITE=500
extrato= ""
numero_de_saques=0
LIMITE_DE_SAQUES=3
usuarios = []
contas = []
AGENCIA = "0001"

def menu():
    text="""\n=====MENU=====\n[d]=Depositar\n[s]=Sacar\n[e]=Extrato\n[nc]=Nova conta\n[lc]=Listar contas\n[nu]=Novo usuário\n[q]=Sair\n=>"""
    return input(text)

def depositar(saldo, valor_depositado, extrato):
    if valor_depositado>0:
        saldo+=valor_depositado
        extrato+=f"Deposito de R$ {valor_depositado:.2f}\n"
    else:
        print("Operacao recusada, valor depositado invalido")
    return saldo, extrato

def sacar(*,saldo, valor_requisitado, extrato, LIMITE):
    valor_requisitado=float(input("Digite qual o valor que deseja sacar: "))
    if valor_requisitado>saldo:
        print("Operacao recusada, voce nao possui saldo o suficiente para este saque!")
    elif valor_requisitado>LIMITE:
        print("Operacao recusada, valor requistado para saque maior que o limite permitido!")
    elif numero_de_saques>=LIMITE_DE_SAQUES:
        print("Operacao recusada, voce ja excedeu o numero de saques limite!")
    elif valor_requisitado>0:
        saldo-=valor_requisitado
        extrato+=f"Efetuado o saque de R${valor_requisitado:.2f}\n"
        numero_de_saques+=1
    else:
        print("Operacao recusada, valor requisitado invalido")
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("Extrato".center(41, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=".center(41,"="))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, fluxo de criação de conta encerrado! ")    


def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
            Agência:\t{conta['agencia']}\n
            C/C:\t\t{conta['numero_conta']}\n
            Titular:\t{conta['usuario']['nome']}\n
        """
        print("=" * 100)
        print(linha)
while True:
    opcao= menu()
    #opcao de deposito
    if opcao=="d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)
    
    #opcao de saque
    elif opcao=="s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = sacar(saldo=saldo, valor=valor,extrato=extrato, LIMITE=LIMITE)

    #opcao de extrato        
    elif opcao=="e":
        mostrar_extrato(saldo, extrato=extrato)

    #opcao de criar novo usuario
    elif opcao == "nu":
        criar_usuario(usuarios)

    #criar nova conta
    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    #opcao para listar as contas
    elif opcao == "lc":
        listar_contas(contas)
    
    #opcao sair
    elif opcao=="q":
        print("Obrigado pela utilizacao do sistema bancario, tenha um bom dia!")
        break
    
    #caso seja usado alguma operacao invalida
    else:
        print("Metodo nao existente no sistema! Utilize um dos metodos apresentados pelo Menu")
