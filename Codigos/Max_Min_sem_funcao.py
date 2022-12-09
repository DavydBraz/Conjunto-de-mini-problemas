#observacao sera feito sem utilizar funcoes min e max
entrada = list(
  map(int,input("\nDigite os valores para ver qual o maximo e minimo: ").split()))
maximo = 0
minimo = 0

#vai ser feito o laco baseado na quantidade de entradas
for i in range(len(entrada)):
  #se o valor que ele verifica quando estiver percorrendo naquela posicao for maior que o maximo ele sera o novo valor maximo
  if entrada[i] > maximo:
    maximo = entrada[i]
  #se o valor que ele verifica quando estiver percorrendo naquela posicao for meno que o minimo ele sera o novo valor minimo
  if entrada[i] < minimo:
    minimo = entrada[i]
print("O valor minimo:{}\nO valor maximo:{}".format(minimo, maximo))
