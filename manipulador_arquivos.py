def escrever_arquivo (tarefa):
  arquivo = open('lista_tarefas.txt', 'a')
  arquivo.write(tarefa + '\n')
  arquivo.close()
  
def ler_arquivo():
  arquivo = open('lista_tarefas.txt', 'r')
  tarefas = arquivo.read()
  arquivo.close()
  return tarefas

def apagar_arquivo():
  arquivo = open('lista_tarefas.txt', 'w')
  arquivo.write('')
  arquivo.close()