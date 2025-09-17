from datetime import date, datetime, time

menu = """ 
[ac] Acessar usuário
[nu] Criar novo usuário
[q] Sair

"""

menu_usuario = """
[ac] Acessar conta
[nc] Criar nova conta
[q] Sair

"""

menu_conta = """ 
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
usuarios = []
contas = []
agencia = '0001'
numero_conta = 1
mascara_dia_ptbr = "%d/%m/%Y"
mascara_hora_ptbr = "%H:%M:%S"

def criar_usuario(usuarios):
  cpf = input('Informe o CPF (somente números): ')
  if not validar_cpf(cpf):
    print('CPF inválido! Retornando ao menu...')
    return
  usuario = filtrar_usuario(cpf, usuarios)
  if usuario:
    print('Já existe usuário com esse CPF! Retornando ao menu...')
    return
  nome = input('Informe o nome completo: ')
  if not validar_nome(nome):
    print('Nome inválido! Retornando ao menu...')
    return
  data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
  if not validar_dara_nascimento(data_nascimento):
    print('Data de nascimento inválida! Retornando ao menu...')
    return
  endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')
  usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
  print('Usuário criado com sucesso! Retornando ao menu...')

def validar_cpf(cpf):
  if len(cpf) != 11 or not cpf.isdigit():
    return False
  if cpf == cpf[0] * 11:
    return False
  if cpf == "12345678909": 
    return False
  soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
  resto = soma % 11  
  if resto < 2:
    digito1 = 0
  else:
    digito1 = 11 - resto 
  if int(cpf[9]) != digito1:
    return False
  return True
def validar_dara_nascimento(data_nascimento):
  try:
    dia, mes, ano = map(int, data_nascimento.split('-'))
    data = date(ano, mes, dia)
    ano_atual = date.today().year
    if ano < 1900 or ano > ano_atual or mes < 1 or mes > 12 or dia < 1 or dia > 31:
      return False
    return True
  except ValueError:
    return False

def validar_nome(nome):
  if len(nome) < 3 or not all(x.isalpha() or x.isspace() for x in nome):
    return False
  return True
  
def filtrar_usuario(cpf, usuarios): 
  usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None

def filtrar_conta(numero_conta, contas):
  contas_filtradas = [conta for conta in contas if conta['numero_conta'] == numero_conta]
  return contas_filtradas[0] if contas_filtradas else None

def criar_conta(agencia, numero_conta, usuarios):
  #usuario = filtrar_usuario(cpf, usuarios)
  if usuario:
    print('Conta criada com sucesso! Retornando ao menu...')
    return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
  print('Usuário não encontrado, retornando ao menu...')

def saque(valor, saldo, extrato, limite, numero_saques, limite_saques):
  if numero_saques >= limite_saques:
    print('Número limite de saques atingido, retornando ao menu... ')
    return saldo, numero_saques, extrato
  if valor <= 0:
   print('Quantia informada inválida! Retornando ao menu...')
   return saldo, numero_saques, extrato
  if valor > limite:
    print('Quantidade acima do limite, retornando ao menu... ') 
    return saldo, numero_saques, extrato
  if valor > saldo:
    print('Quantidade acima do saldo, retornando ao menu... ')
    return saldo, numero_saques, extrato
  saldo -= valor
  numero_saques +=1
  print(f'Quantia de valor R${valor:.2f} foi sacada, voltando para o menu...\n')
  extrato.append(f'Saque: R${valor:.2f} no dia {date.today().strftime(mascara_dia_ptbr)} às {datetime.now().time().strftime(mascara_hora_ptbr)}')
  return saldo, numero_saques, extrato
def deposito(valor, saldo, extrato):
  if valor < 0:
      print('Quantia informada inválida! Retornando ao menu...')
      return saldo, extrato
  saldo += valor
  print(f'A quantia de R${valor:.2f} foi depositado, retornando ao menu...\n')
  extrato.append(f'Depósito: R${valor:.2f} no dia {date.today().strftime(mascara_dia_ptbr)} às {datetime.now().time().strftime(mascara_hora_ptbr)}')
  return saldo, extrato
def mostrar_extrato(saldo, extrato):
  print('\n================ EXTRATO ================')
  if not extrato:
      print('Não foram realizadas movimentações.')
  else:
      for linha in extrato:
          print(linha)
  print(f'\nSaldo: R${saldo:.2f}')
  print('==========================================')

while True:
 print('Bem vindo ao nosso sistema bancário, por gentileza, informe o que deseja fazer:')
 opcao = input(menu)

 #criar novo usuário
 if opcao == 'nu':
   criar_usuario(usuarios)
 #acessar usuário
 elif opcao == 'ac':
   cpf = input('Informe o CPF do usuário: ')
   usuario = filtrar_usuario(cpf, usuarios)
   if not usuario:
     print('Usuário não encontrado, retornando ao menu...')
     continue
   if usuario:
     while True:
      print(f'Bem vindo {usuario["nome"]}! por gentileza, informe o que deseja fazer:')
      opcao = input(menu_usuario)
      if opcao == 'nc':
        conta = criar_conta(agencia, numero_conta, usuarios)
        contas.append(conta)
        numero_conta += 1
      if opcao == 'ac':
        if contas == []:
          print('Nenhuma conta encontrada, por gentileza, crie uma conta primeiro!')
          continue
        print('Segue a lista de suas contas:')
        for conta in contas:
         print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}")
        numero_conta = int(input('Informe o número da conta: '))
        conta = filtrar_conta(int(numero_conta),contas)
        if conta:
         while True:
           print(f'Acessando a conta {numero_conta}, por gentileza, informe o que deseja fazer:')
           opcao = input(menu_conta)
           #depositar
           if opcao == 'd': 
             valor = float(input('Informe a quantia que deseja depositar: '))
             saldo,extrato = deposito(valor, saldo, extrato)
           #sacar
           elif opcao == 's':
             valor = float(input('Informe a quantia que deseja sacar: '))
             saldo,numero_saques,extrato = saque(valor, saldo, extrato, limite, numero_saques, limite_saques)
             #extrato
           elif opcao == 'e':
             mostrar_extrato(saldo, extrato)
           elif opcao == 'q':
             print(f"Encerrando a operação da conta {numero_conta}")
             break
           else:  
             print("Operação inválida, retornando ao menu...")
           continue
        else:
          print('Operação inválida ou conta não encontrada!')
        continue
      elif opcao == 'q':
       print(f"Encerrando a operação usuário {usuario["nome"]}, obrigado por usar nosso sistema bancário")
      break
   else:
     print('Usuário não encontrado, retornando ao menu...')
     continue
 elif opcao == 'q':
     print("Encerrando a operação, obrigado por usar nosso sistema bancário")
     break
 else:  
   print("Operação inválida, retornando ao menu...")
   continue


