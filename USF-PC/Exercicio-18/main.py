import matplotlib.pyplot as plt
import sys

notas = []
aluno = []

try:
  qtd = int(input("\nDigite a quantidade de alunos para cálculo\nda média aritmética da sala de aula: "))
  print()
except (ValueError, NameError):
  print("\nErro: O valor da nota inserida não pertence ao conjunto dos números reais\n")
  sys.exit(0)
  

for i in range(qtd):
  try:
    insNota = float(input(f"Digite a nota do aluno {i+1}: "))
  except:
    print("\nErro: O valor da nota inserida não pertence ao conjunto dos números reais\n")
    sys.exit(0)

  if insNota >=0 and insNota <=10:
    notas.append(insNota)
    aluno.append(f'Aluno {i+1}')

  else:
    print("\nA nota inserida não é válida\n")
    continue

media = (sum(notas)/len(notas))
print(f"\nA média aritmética da sala de aula é: {media}\n")


print("Digite o número da opção de grafico desejada")
print()
print("1) Gráfico de linha")
print("2) Gráfico de barra")
print("3) Gráfico de dispersão (scatterplot)")
print()

try:
  opcao = int(input("Opção: "))
except:
    print("\nErro: O valor da nota inserida não pertence ao conjunto dos números reais\n")
    sys.exit(0)  

if opcao == 1:
  plt.plot(aluno, notas, color='black', marker='o', linewidth=2)
  plt.show()

elif opcao == 2:
  plt.bar(aluno, notas, color='blue', align='center', width=0.5)
  plt.show()

elif opcao == 3:
  plt.scatter(aluno, notas, marker='.',  color='red', s=500)
  plt.show()

else:
  print("\nOpção inválida\n")