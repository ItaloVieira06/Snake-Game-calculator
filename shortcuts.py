from tkinter import messagebox
import time

#setagem de variáveis
jogadas = 0
pontos = 0

#checagem de formato
def check(a=0):
 while True:
  try:
   a = int(a)
   return a
  except ValueError:
   messagebox.showinfo("Erro!!!", "Há presença de \n formatos Inválidos!!!!")
   a = 0