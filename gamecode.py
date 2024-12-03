import random
from shortcuts import *

def game(jogadas, num, numa):
    num_maquina(numa, num, pontos)
    messagebox.showinfo("Jogadas: ", jogadas)
    return jogadas

def num_maquina(numa, num, pontos):
    numa = random.randrange(1, 10)
    if (num == numa):
     pontos +=3
     time.sleep(0.75)
     messagebox.showinfo("Parabéns", "Você acertou! \n Calculando pontos....")
     time.sleep(0.5)
    else:
     pontos -= 1
     time.sleep(0.5)
     messagebox.showinfo("Errou! O sorteado foi: ", numa)
     time.sleep(0.5)
     if (pontos <=0):
        pontos = 0
    
    messagebox.showinfo("Pontos:", pontos)
    return pontos