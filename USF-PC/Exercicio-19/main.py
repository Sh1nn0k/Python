import soma
import subtrac
import pot
import fat

print("Selecione o tipo de operação desejada")
print()
print("1) Soma")
print("2) Subtração")
print("3) Potenciação")
print("4) Fatorial")
print()

try:
  opcao=int(input("Opção: "))
except:
  print("Opção incorreta")

if opcao==1:
  soma.soma()

elif opcao==2:
  subtrac.subtrac()

elif opcao==3:
  pot.pot()

elif opcao==4:
  fat.fat()

else:
  print("Opção inválida")

