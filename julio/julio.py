print('tranformardor de Kg em Mg,G')
medida = str(input('Qual a medida você quer utilizar (Mg ou G) : '))
print('(Aviso o valor colocado tem que ser em "Kg" e nao colocar KG no final EX: 100 )')
valor =int(input('Qual valor voce quer transformar : '))
if medida == 'Mg'or 'mg' or 'MG' or 'mG':
     calculo = valor * 1000000
     print(f'Valor: {valor} tranformado em {medida} = {calculo}')
elif medida == 'G'or 'g':
    calculo = valor * 1000
    print(f'Valor: {valor} tranformado em {medida} = {calculo}')
else:
    print('Algo deu errado,tente novamente.')

# desafio 2 ------------------------------------------------------------------------------
print('Calculadora')
numero = int(input('Digete o número qual a tabuada sera mostrada'))
for i in range(1+10):
    calculo = numero * i
    print(f'{numero} * {i} = {calculo}')

# desafio 3 ------------------------------------------------------------------------------
print('Posto de gasolina')
print('preço da gasolina R$ 6,50')
valor  = float(input("digite o valor desejado : "))
print('aviso usar (.) inves de (,)')
calculo = valor / 6.50
print(f'foi abestecido {calculo}Litros')
