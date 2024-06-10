import time
from datetime import datetime

lista_placas = []
hora_atual = datetime.now().strftime('%H:%M:%S')

def cadastrar_placa():

  print('Bem-Vindo ao Estacionamento')
  time.sleep(1)
  print()
  print('Aqui você pode estacionar seu carro e retirar quando quiser')
  time.sleep(1)
  print()
  print('Para estacionar precisaremos de sua placa e para retirada também')
  time.sleep(1)
  print()
  while True:
   print()
   print('Temos as seguintes opções:')
   time.sleep(1)
   print()
   print('1 - Estacionar')
   time.sleep(1)
   print('2 - Retirar')
   time.sleep(1)
   print('3 - Sair')
   print()
   escolha = input(':')
   if escolha == '1' or escolha.lower() == 'estacionar':
     print('Ok, vamos estacionar seu carro')
     time.sleep(1)
     print()
     print('Digite a placa do seu carro')
     placa = input(':')
     lista_placas.append(placa)
     print(f'O carro foi estacionado com sucesso as {hora_atual}')
   elif escolha == '2' or escolha.lower() == 'retirar':
     print('Ok, vamos retirar seu carro')
     time.sleep(1)
     print()
     print('Digite a placa do seu carro')
     placa = input(':')
     if placa in lista_placas:
        lista_placas.remove(placa)
        print(f'O carro foi retirado com sucesso as {hora_atual}')
     else:
       print('Placa não encontrada')
   elif escolha == '3' or escolha.lower() == 'sair':
     print('Ok, volte sempre')
     time.sleep(1)
     print()
     print(f'Cliente Saiu as {hora_atual}')
     break
     
cadastrar_placa()
