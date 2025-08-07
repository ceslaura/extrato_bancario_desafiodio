menu = """ 
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
limite_saques = 3

while True:
 print('Bem vindo ao nosso sistema bancário, por gentileza, informe o que deseja fazer:')
 opcao = input(menu)
 
 if opcao == 'd':
   valor = float(input('Informe a quantia que deseja depositar: '))
   if valor > 0:
      saldo += valor
      print(f'A quantia de R${valor:.2f} foi depositado, retornando ao menu...\n')
      extrato.append(f'Depósito: R${valor:.2f}')
   else:
      print('Quantia informada inválida! Retornando ao menu...')
 elif opcao == 's':
  if numero_saques < limite_saques:
            valor = float(input('Informe a quantia que deseja sacar: '))
            if valor <= limite:
                if saldo > valor:
                    if valor > 0:
                      saldo -= valor
                      numero_saques +=1
                      print(f'Quantia de valor R${valor:.2f} foi sacada, voltando para o menu...\n')
                      extrato.append(f'Saque: R${valor:.2f}')
                    else:
                       print('Quantia informada inválida! Retornando ao menu...')
                else: 
                    print('Quantidade acima do saldo, retornando ao menu... ') 
                    continue 
            else: 
                print('Quantidade acima do limite desejado, retornando ao menu... ')
                continue 
  else: 
        print("Numero limite de saques diários foi atingido, voltando para o menu...\n") 
        continue
 elif opcao == 'e':
  if extrato == []:
    print('Não foi realizado nenhuma movimentação')
  else:
    print(f'Segue o extrato:\n')
    for linha in extrato:
      print(linha)
    print(f'Saldo atual: R${saldo:.2f}')
 elif opcao == 'q':
     print("Encerrando a operação, obrigado por usar nosso sistema bancário")
     break
 else:
   print("Operação inválida, retornando ao menu...")
   continue
