#Programa para cálculo da média das notas de 30 alunos

mult = 1
soma = 0

opcao = int(input("Digite qual o tipo de média que deseja calcular: \n\n \
1 - Média Aritmética\n \
2 - Média Geométrica \n \
3 - Média Harmônica \n\n \
Opção:"))

try:
  qtd = int(input('\nDigite a quantidade de alunos: '))
except:
  print('\nErro: Valor inserido não é do tipo inteiro\n')

nlist = list (range(1,qtd+1))

if opcao == 1:
  
  try:

    for i in range(1,qtd+1):
        nota = float(input(f"Digite o valor da nota do aluno {i}: "))
        nlist[i-1] = nota

    mediaAritmetica = round((sum(nlist))/len(nlist),4)
    print(f"\nA média aritmética equivale a: {mediaAritmetica}")

  except:
    print('\nErro: Não é possível realizar a média aritmética, visto que não há valores reais para realizar as operações')

elif opcao == 2:
  
  try:
    
    for i in range(1,qtd+1):
      nota = float(input(f"Digite o valor da nota do aluno {i}: "))
      nlist[i-1] = nota
      mult = mult*nlist[i-1]
    
    mediaGeometrica = round((mult) ** (1/len(nlist)),4)
    print(f"\nA média geométrica equivale a: {mediaGeometrica}")

  except:
    print('\nErro: Não é possível realizar a média geométrica, visto que não há valores reais para realizar as operações')

elif opcao == 3:
  
  try:

    for i in range(1,qtd+1):
      nota = float(input(f"Digite o valor da nota do aluno {i}: "))
      nlist[i-1] = nota
      soma = soma + (1/nlist[i-1])

    mediaHarmonica = round(len(nlist) / soma,4)
    print(f"\nA média harmônica equivale a: {mediaHarmonica}")

  except:
    print('\nOs dados inseridos apresentam algum dos erros a seguir:\n 1 - Não é possível realizar a média harmônica com o valor "0", visto que não há valores reais para operações com este.\n 2 - Não é possível realizar a média aritmética, visto que não há valores reais para realizar as operações')

else:
  print("\nOpção inválida")
