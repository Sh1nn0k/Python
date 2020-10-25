def parc_2(valorTotal):
  qtd=int(input("Digite a quantidade de parcelas desejadas: "))
  if qtd >= 3 and qtd <=10:
    juros = 1.03 ** qtd
    valorFinal = valorTotal * juros
    print(f"Pagamento: 0{qtd} parcelas de R${valorFinal}")

  else:
    print("Quantidade inválida de parcelas")
