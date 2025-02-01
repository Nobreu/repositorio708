#Crie um programa que calcule um buraco na pista e diga quantos sacos de piche serão
# nescessários para tapar o buraco.
#cada saco de piche pode tapar 2m²
comprimento = float(input("Digite o comprimento do buraco: "))
largura = float(input("Digite a largura do buraco: "))
area = comprimento * largura
piche = 2

quantidade_piches = area / piche
print(f"serão nescessários {quantidade_piches:.2f} sacos de piche para tapar o buraco.")