from manipulador_arquivos import *
import os


def limpar_tela():
  os.system('cls' if os.name == 'nt' else 'clear')

def mostrar(tarefas):
  numero = 1
  for tarefa in tarefas.splitlines():
    print(f'{numero} - {tarefa}')
    numero += 1

def pausar():
  input('Digiter enter para continuar.')

def selecionar_menu(opcao):
  if opcao == '1':
    tarefa = input('Digite a nova tarefa: ')
    escrever_arquivo(tarefa)
  elif opcao == '2':
    tarefas = ler_arquivo()
    mostrar(tarefas)
    pausar()
  elif opcao == '3':
    tarefas = ler_arquivo()
    mostrar(tarefas)
    numero_tarefa = int(input('Digite o número da tarefa para excluir: ')) - 1
    tarefas = tarefas.splitlines()
    del tarefas[numero_tarefa]
    apagar_arquivo()
    tarefas = '\n'.join(tarefas)
    escrever_arquivo(tarefas)
  elif opcao == '4':
    tarefas = ler_arquivo()
    mostrar(tarefas)
    numero_tarefa = int(input('Digite o número da tarefa para editar: ')) - 1
    nova_tarefa = input('Digite a nova tarefa: ')
    tarefas = tarefas.splitlines()
    tarefas[numero_tarefa] = nova_tarefa
    apagar_arquivo()
    tarefas = '\n'.join(tarefas)
    escrever_arquivo(tarefas)
  elif opcao == '0':
    print('Saindo do sistema.')
    exit(0)

def exibir_menu():
  limpar_tela()
  print('--->MENU<---')
  print('1 - Adicionar tarefa')
  print('2 - Listar tarefas')
  print('3 - Excluir tarefa')
  print('4 - Editar tarefa')
  print('0 - Sair')
  opcao = input('Escolha uma opção: ')
  selecionar_menu(opcao)
  
  exibir_menu()
  
  

exibir_menu()