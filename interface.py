from tkinter import *
from gamecode import *

#core do projeto
def jogo(Entra, jogadas, numa):
 try:
   #get do número
   num = Entra.get()
   num = check(num)
   #complemento do check
   if(num == 0):
     return vezes
   else:
     #início do jogo
     jogadas -=1
    
     #check de finalização
     game(jogadas, num, numa)
     if (jogadas <= 0):
      messagebox.showinfo("Fim", "Obrigado por jogar!!!")
      main.destroy()
 finally:
    #nova janela de inserção de números/ impedir choques de valores com a janela anterior
    main.geometry("400x350")
    caixa.grid_remove()
    iniciar.grid_remove()

    título = Label(main, text="                 Agora vamos apostar em um número!!!!                     ")
    título.grid(column=0, row=1, padx=40, pady=30)
        
    numa = Entry(main, width=10)
    numa.grid(column = 0, row=2, padx = 40, pady = 30)
    
    enviar = Button(main, text="Enviar", command= lambda: jogo(numa, jogadas, numa))
    enviar.grid(column=0, row=3, padx=40, pady=30)

def startar (Entra, jogadas):
    #get de jogadas
    try:
      jogadas = Entra.get()
      jogadas = check(jogadas)
      return jogadas
    finally:
        #página 2
        main.geometry("400x350")
        caixa.grid_remove()
        iniciar.grid_remove()

        título = Label(main, text="                 Agora vamos apostar em um número!!!!                     ")
        título.grid(column=0, row=1, padx=40, pady=30)
        
        numa = Entry(main, width=10)
        numa.grid(column = 0, row=2, padx = 40, pady = 30)
    
        enviar = Button(main, text="Enviar", command= lambda: jogo(numa, jogadas, numa))
        enviar.grid(column=0, row=3, padx=40, pady=30)

def vezes():
    #reseter
    iniciar.grid_remove()
    t2.grid_remove()

    #reposicionamento da página
    main.geometry("310x350")

    título = Label(main, text="Digite o número de vezes que gostaria de jogar: ")
    título.grid(column=0, row=1, padx=20, pady=30)

    caixa = Entry(main, width=10)
    caixa.grid(column=0, row=2, padx=20, pady=30)

    enviar = Button(main, text="Enviar", command= lambda: startar(caixa, jogadas))
    enviar.grid(column=0, row=3, padx=20, pady=30)


#janela principal / main do projeto
main = Tk()
main.title("Jogo da adivinhação")
main.geometry("310x350")

título = Label(main, text = "Jogo de adivinhação de NÚMEROS!!!")
título.grid(column=0, row=0, padx=50, pady=30)

t2 = Label(main, text = "Digite o seu nome abaixo: ")
t2.grid(column=0, row=1, padx=50, pady=30)
caixa = Entry(main, width=10)
caixa.grid(column=0, row=2, padx=50, pady=30)

iniciar = Button(main, text="JOGAR", command= vezes)
iniciar.grid(column=0, row=3, padx=50, pady=30)

main.mainloop()