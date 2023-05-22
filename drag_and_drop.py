from tkinter import *
from tkinter import filedialog

def selecionar_arquivo():
    arquivo = filedialog.askopenfilename(initialdir="/", title="Selecione um arquivo")

    print(arquivo)
    print(type(arquivo))

janela = Tk()

botao = Button(janela, text="Selecionar arquivo", command=selecionar_arquivo)
botao.pack()

janela.mainloop()