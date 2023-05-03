#exercicio simples baseado em uma atividade do curso python developer da DIO, seguindo as metricas basicas do mesmo,
#o qual limitou a usar esses recursos mais simples

menu = """

[d]=Depositar
[s]=Sacar
[e]=Extrato
[q]=Sair

=>"""

saldo=0
LIMITE=500
extrato= ""
numero_de_saques=0
LIMITE_DE_SAQUES=3

while True:
    opcao= input(menu)
    #opcao de deposito
    if opcao=="d":
        valor_depositado=float(input("Digite qual o valor a se Depositar: "))
        if valor_depositado>0:
            saldo+=valor_depositado
            extrato+=f"Deposito de R$ {valor_depositado:.2f}\n"
        else:
            print("Operacao recusada, valor depositado invalido")
    
    #opcao de saque
    elif opcao=="s":
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

    #opcao de extrato        
    elif opcao=="e":
        #o .center serve para fazer o efeito de completar os espacos, no caso 41, contando a palavra Extrato, com =
        print("Extrato".center(41, "="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=".center(41,"="))
    
    #opcao sair
    elif opcao=="q":
        print("Obrigado pela utilizacao do sistema bancario, tenha um bom dia!")
        break
    
    #caso seja usado alguma operacao invalida
    else:
        print("Metodo nao existente no sistema! Utilize um dos metodos apresentados pelo Menu")
