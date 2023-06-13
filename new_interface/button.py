import sys
from PySide6.QtWidgets import QPushButton

# Subclasse QMainWindow para criar a janela principal da aplicação
class button(QPushButton):
    def __init__(self):
        super().__init__()

        # Cria um botão
        button = QPushButton("Confirmar", self)

        # Conecta o sinal clicked() do botão a um slot (método) chamado on_button_clicked
        button.clicked.connect(self.on_button_clicked)

    # Método de slot para lidar com o clique no botão
    def on_button_clicked(self):
        print("O botão foi clicado!")
        #inserir aqui string em c