alunos = {}

for i in range(5):
    nome = input("Informe o nome: ")
    nota = float(input("Informe a nota: "))
    alunos[nome] = nota

media = sum(alunos.values()) / len(alunos)
print("Media da turma = ", media)

for nome, nota in alunos.items():
    if nota >= 7:
        print("Aprovado")