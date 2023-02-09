# script threads_inc_lock.py
from threading import Thread, Lock
from multiprocessing import Process
import time

contador = 0
lock = Lock()
print_lock = Lock()

def funcao_a(indice):
    global contador
    for i in range(1000000):
        lock.acquire()
        contador += 1
        lock.release()
    print_lock.acquire()
    print("Termino thread ", indice)
    print_lock.release()

def main():
    tarefas = []
    for indice in range(10):
        tarefa = Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o termino!", contador)

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", contador)

if __name__ == "__main__":
    main()