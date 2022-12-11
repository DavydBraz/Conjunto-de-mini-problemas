casos=int(input("Numero de testes: "))
resultado=0

for i in range(casos):
    resultado=0
    avg=list(map(int, input("Digite os valores que deseja e 0 para indicar ultimo valor"). split()))
    for numero in avg:
        if numero!=0:
            resultado+=numero
    resultado/=int(len(avg)-1)
    print(resultado)
