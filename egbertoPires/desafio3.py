from utilitario import linha

print('Escolha um número e veja a sua tabuada')
tabuada = int(input('Tabuada do número: '))
print(linha(20))
print(f'Tabuada do número {tabuada}')
for i in range (1,11):
    print(f'{tabuada} x {i} = {tabuada * i}')