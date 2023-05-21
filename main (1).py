import random

dias_semana = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
materias = []

while True:
    x = input('Quais matérias você quer estudar? (Digite "sair" para encerrar): ')
    if x.lower() == "sair":
        break
    materias.append(x)
prioridades = {}

for materia in materias:
    prioridade = int(input(f'Qual a prioridade da matéria "{materia}"? (Digite um número de 1 a 5): '))
    prioridades[materia] = prioridade

num_dias = int(input('Em quantos dias você quer estudar por semana? '))     
print(materias)

for dia in range(num_dias):
    dia_semana = random.choice(dias_semana)
    print(f"\nDia {dia + 1} - {dia_semana}:\n")
    materias_prioritarias = sorted(materias, key=lambda x: prioridades[x], reverse=True)
    for materia in materias_prioritarias:
        duracao_estudo = random.randint(1, 2)
        print(materia, "estude", duracao_estudo, "horas")

    dias_semana.remove(dia_semana)
print("\nBons Estudos!")