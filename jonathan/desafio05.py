#Crie um programa que calcule quantos litros de gasolina será possivel abastecer. valor do litro 6,5
valor_litro = 6.5
valor_abastecimento = float(input("Qual o valor do abastecimento em reais? "))
Qtd_litros = valor_abastecimento/valor_litro
print(f"Você poderá abastecer {Qtd_litros:.2f} litros de gasolina.")