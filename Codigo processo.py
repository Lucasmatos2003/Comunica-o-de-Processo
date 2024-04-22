import multiprocessing
import queue
import time



# Função para processar tarefas
def individual_process_task(task_priority, task_name, result_queue):

   contador = 0

   print(f"Iniciando: {task_name} com prioridade {task_priority}")
   time.sleep(2)



   while task_name == "Tarefa do Sistema Operacional" and contador <= 2:
       contador += 1
       print(f"Tarefa {task_name} está em execução -  Tarefa do Utorrent / Tarefa do Terraria Esperem para executar ")
       time.sleep(2)


      # Simulando o processamento da tarefa

       while task_name == "Tarefa do Sistema Operacional" and contador <= 3:
           contador += 1
           print(f"Terminando: {task_name} com prioridade {task_priority}")
           print(f"{task_name} terminou o processamento, Tarefa do Terraria = Livre para executar")
           # Coloque uma mensagem na fila de resultados para indicar que a tarefa foi concluída


   contador2 = 0

   time.sleep(3)




   while task_name == "Tarefa do Terraria" and contador2 <= 2:
       contador2 += 1
       print(f"Tarefa {task_name} está em execução -  Tarefa do Utorrent Espere para executar ")
       time.sleep(2)

   # Simulando o processamento da tarefa
   # Você pode adicionar o código real de processamento aqui

       while task_name == "Tarefa do Terraria" and contador2 <= 3:
           contador2 += 1
           print(f"\nTerminando: {task_name} com prioridade {task_priority}")
           print(f"{task_name} terminou o processamento, Tarefa do Utorrent  = Livre para executar")
           # Coloque uma mensagem na fila de resultados para indicar que a tarefa foi concluída




   contador1 = 0

   time.sleep(4)


   while task_name == "Tarefa do Utorrent" and contador1 <= 2:
       contador1 += 1
       print(
           f"Tarefa {task_name} está em execução -  Próxima Tarefa espere para executar ")
       time.sleep(2)

   # Simulando o processamento da tarefa
   # Você pode adicionar o código real de processamento aqui

       while task_name == "Tarefa do Utorrent" and contador1 <= 3:
           contador1 += 1
           print(f"Terminando: {task_name} com prioridade {task_priority}")
           print(f"{task_name} terminou o processamento, Próxima Tarefa  = Livre para executar")
           # Coloque uma mensagem na fila de resultados para indicar que a tarefa foi concluída








       result_queue.put(task_name)


if __name__ == "__main__":
  # Crie uma fila de prioridade para armazenar as tarefas
  task_queue = queue.PriorityQueue()

  # Adicione tarefas à fila de prioridade com prioridades diferentes
  task_queue.put((1, "Tarefa do Sistema Operacional"))
  task_queue.put((1, "Tarefa do Terraria"))
  task_queue.put((1, "Tarefa do Utorrent"))

  # Crie uma fila para armazenar os resultados
  result_queue = multiprocessing.Queue()

  # Crie e inicie processos para processar as tarefas
  num_processes = 3  # Número de processos que você deseja usar
  processes = []

  for _ in range(num_processes):
      task_priority, task_name = task_queue.get()
      process = multiprocessing.Process(target= individual_process_task, args=(task_priority, task_name, result_queue))
      processes.append(process)
      process.start()

  # Espere até que todos os processos terminem
  for process in processes:
      process.join()

  # Imprima os resultados
  while not result_queue.empty():
      completed_task = result_queue.get()
      print(f"Tarefa concluída: {completed_task}")