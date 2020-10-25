def fat():
  num1 = int(input("Digite o número: "))
  fatorial = 1
  for i in range(1, num1+1):
    fatorial = fatorial * i
  
  print(f'O fatorial de {num1} é: {fatorial}')