#3.	Em um jogo de Fazenda existe a opção de compras de frutas para jogador para manter em sua 
#   despensa.  No empório virtual as frutas são vendidas pelos seguintes preços: Maça: R$ 1,30 a
#   unidade, Melancia: R$ 4,00 a unidade e Laranja R$ 0,30 a unidade.  Escreva um programa para
#   ler a quantidade de melancias compradas, calcular e mostrar na tela o valor a pagar

quantMel = int(input("Quantas Melacias você que comprar: "))
valTotal = quantMel * 4.00
print("O valor a ser pago é R$", valTotal)
quit()
