from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import seaborn as sns
import numpy as np

nome_in = "geracao_grafico_x"
nome_in = filedialog.askopenfilename(initialdir="/", title="Selecione um arquivo")

with open(nome_in, 'r') as f:
    dados = f.read() 

dados_ = dados[1:].split('/')
is_y = False
dados_y = [1.1]
dados_x = [1.1]
for d in dados_:
    if d != 'y':
        if is_y and d != 'y':
            dados_y.append(float(d))
        else:
            dados_x.append(float(d))
    else:
        is_y = True


plt.ylabel('Eixo Y')
plt.xlabel('Eixo X')
plt.title('Novo Gráfico')


print(dados_x[1:])
print(dados_y[1:])

plt.axis(xmin=0,xmax=(max(dados_x)*1.2),ymin=-0,ymax=(1+max(dados_y)))

plt.plot(dados_x[1:], dados_y[1:])
plt.show()
