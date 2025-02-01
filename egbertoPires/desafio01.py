print('Insira um número inteiro e escolha a quantidade de antecessores e sucessores')

numero = int(input("Escolha um número: "))
antecessor = int(input("Quantos antecessores? "))
sucessor = int(input("Quantos sucessores? "))
resultado = 'Intervalo = {'
for i in range (numero - antecessor,numero + (sucessor + 1)):
       resultado += f'{i},'
print(f"{resultado[:-1]}" + "}")