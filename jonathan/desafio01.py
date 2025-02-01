#Crie um programa que calcule a média de notas de um aluno.
provas = int(input("Digite o numero de provas: "))
soma_notas = 0
for i in range(0, provas):
    nova_nota = int(input(f"Digite a nota da prova: "))
    soma_notas += nova_nota

media = soma_notas / provas

print(f"A média das notas é: {media}")