# Calcular a Media de notas

print("Calculo da média:")
notaUm = float(input("Digite a 1°:"))
notaDois = float(input("Digite a 2°:"))
notaTres = float(input("Digite a 3°:"))
notaQuatro = float(input("Digite a 4°:"))
media = (notaUm + notaDois + notaTres + notaQuatro)/4
print("--------------")


print("------- BOLETIM ESCOLAR ----------")
print("Seja bem vindo(a)!")
print(f"NOTA 1º: {notaUm}\n"
f"NOTA 2º: {notaDois}\n"
f"NOTA 3º: {notaTres}\n"
f"NOTA 4º {notaQuatro}\n"
f"MÉDIA: {media}")
print("----------------------------------")

if media >= 7:
   print(f"APROVADO: {media}")
else:
   print(f"REPROVADO: {media}")