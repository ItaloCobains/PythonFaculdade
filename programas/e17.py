# from time import sleep
# from threading import Thread


# def tarefa(tempo__espera, mensagem):
#     print(f"Iniciando tarefa {mensagem}")
#     sleep(tempo__espera)
#     print(f"Terminando tarefa {mensagem}")


# thread = Thread(target=tarefa, args=(3, "1"))
# thread2 = Thread(target=tarefa, args=(2, "2"))
# thread.start()
# thread2.start()
# print("aguardando execução da thread")
# thread.join()
# thread2.join()
# print("thread terminada")


# script processos.py
from threading import Thread

minha_lista = []


def adiciona():
    for i in range(100):
        minha_lista.append(1)


def main():
    tarefas = []

    for indice in range(10):
        t = Thread(target=adiciona)
        tarefas.append(t)
        t.start()

    for indice in range(10):
        p = Thread(target=adiciona)
        tarefas.append(t)
        p.start()

    for tarefa in tarefas:
        tarefa.join()

    print(len(minha_lista))


if __name__ == "__main__":
    main()
