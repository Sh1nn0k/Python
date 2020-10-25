import form1
import form2
import form3

valorTotal=float(input("Digite o valor total gasto: "))
print("Selecione a opção de pagamento desejada")
print()
print("1) À vista com 10% de desconto")
print("2) Parcelado em 2 vezes sem juros")
print("3) Parcelado de 3 a 10 vezes com 3% de juros ao mês (somente para compras acima de R$100.00)")
print()

try:
  opcao=int(input("Opção: "))
except:
  print("Opção incorreta")


if opcao==1:
  form1.a_vista(valorTotal)

if opcao==2:
  form2.parc_1(valorTotal)

if opcao==3:
  form3.parc_2(valorTotal)




