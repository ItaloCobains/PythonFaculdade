from time import sleep
from threading import Thread


def tarefa(tempo__espera, mensagem):
    print(f"Iniciando tarefa {mensagem}")
    sleep(tempo__espera)
    print(f"Terminando tarefa {mensagem}")


thread = Thread(target=tarefa, args=(2, "aaaaaaa"))
thread.start()
print("aguardando execução da thread")
thread.join()
print("thread terminada")
