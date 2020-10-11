i = 0
it = 0
qst = "s"
total = 0.00
nlist = list(range(1,10**5))
qlist = list(range(1,10**5))
ulist = list(range(1,10**5))

print("*** CAIXA DE SUPERMERCADO ***")

print()

print("* Inserindo produtos *")

print()

while qst == "S" or qst == "s":

  i += 1

  print(f"Digite as informações do produto {i}")

  print()

  nome = input("Nome do produto: ")
  qtd = int(input("Quantidade do produto: "))
  unit= float(input("Valor unitário do produto: "))

  nlist[i] = nome
  qlist[i] = qtd
  ulist[i] = unit

  total = total + (qtd*unit)

  it = range(1,i+1)

  print()

  qst = input("Deseja continuar? S/N: ")
  print()
  

print()
print("* Recibo *")
print()

for item in it:

  print(f"[PRODUTO {item}]")
  print()
  print(f"Nome: {nlist[item]}")
  print(f"Quantidade: {qlist[item]}")
  print(f"Valor unitário: {ulist[item]}")
  print(f"Valor total deste produto: {qlist[item]*ulist[item]}")
  
  print()
  print()
  print()

print(f"Valor total dos produtos: {total}")

