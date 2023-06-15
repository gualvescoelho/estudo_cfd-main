import os as op
from PySide6.QtWidgets import QPushButton, QFileDialog
from drag_drop import DragDropWidget as dp
from urllib.parse import quote

# Subclasse QMainWindow para criar a janela principal da aplicação
class button(QPushButton):
    def __init__(self):
        super().__init__()

        # Cria um botão
        button = QPushButton("Confirmar", self)

        # Conecta o sinal clicked() do botão a um slot (método) chamado on_button_clicked
        button.clicked.connect(self.on_button_clicked)

    # Método de slot para lidar com o clique no botão
    def on_button_clicked(self, string):
        print(self.dragdrop_widget.urls)
        self.open_dialog()
        for url in self.dragdrop_widget.urls:

            path = '"' + url + '"' + " " + '"' + self.diretorio_saida +"\\"+ op.path.basename(url) + '"'

            print(
                "start limpeza_1.exe " + path
            )
            op.system(
                "start limpeza_1.exe " + path
            )

    def open_dialog(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(self, "Selecionar Diretório de Saída", options=options)
        if directory:
            self.diretorio_saida = directory

    def drag_drop(self):
        self.dragdrop_widget = dp()
        return self.dragdrop_widget
        
    def file_name(string):
        return string.spl