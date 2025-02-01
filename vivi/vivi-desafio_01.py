nome_aluno = input("Digite o nome do aluno")

nota1 = float(input("Digite a primeira nota"))
nota2 = float(input("Digite a segunda nota"))
nota3 = float(input("Digite a terceira nota"))

media = (nota1 + nota2 + nota3) / 3
print(f"O aluno {nome_aluno} obteve a {media:.2f}")
