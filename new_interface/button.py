import os as op
from PySide6.QtWidgets import QPushButton, QFileDialog
from drag_drop import DragDropWidget as dp

# Subclasse QMainWindow para criar a janela principal da aplicação
class button(QPushButton):
    def __init__(self, values):
        super().__init__()
        print("values", values)
        self.values = values
        # Cria um botão
        button = QPushButton("Confirmar", self)

        # Conecta o sinal clicked() do botão a um slot (método) chamado on_button_clicked
        button.clicked.connect(self.on_button_clicked)

    # Método de slot para lidar com o clique no botão
    def on_button_clicked(self):

        self.open_dialog()
        
        for url in self.dragdrop_widget.urls:
            # self.limpeza(url)
            
            self.read_file(url)
            # criação dessa regra de negocio
            # if self.first == '#':
            #     self.limpeza(url)

            self.processing(url, str(self.qnt_coord), '200')


    def open_dialog(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(self, "Selecionar Diretório de Saída", options=options)
        if directory:
            self.diretorio_saida = directory

    def limpeza(self, url):
        path = '"' + url + '"' + " " + '"' + self.diretorio_saida +"\\"+ op.path.basename(url) + '"'
        op.system(
            "start limpeza_1.exe " + path
        )

    def processing(self, url, qtd_coord, itmin):
        values = ''.join(self.values)
        string = 'start geral_interface"' + url + '" '+ qtd_coord +" "+ itmin +" "+ self.lines +" "+ values + ' "' + self.diretorio_saida + '"'
        print(string)
        # op.system(
        #     "start geral_interface " + string
        # )

    def drag_drop(self):
        self.dragdrop_widget = dp()
        return self.dragdrop_widget
        
    def read_file(self, url):
        with open(url, 'r') as arquivo:

            # informa o primeiro caracter do arquivo e volta ao inicio com fim de verificar as linhas
            first = arquivo.read(1)
            arquivo.seek(0)
            
            read = arquivo.read()
            qtd_coord = read.count('#') - 1
            arquivo.seek(0)

            # retornar a quantidade de iterações e subtrair pela quantidade de coordenadas
            len = arquivo.readlines()
        
        size = int(len.__len__()) - int(qtd_coord) - 2

        # Imprimir os caracteres lidos
        self.qnt_coord = str(qtd_coord)
        self.first = str(first)
        self.lines = str(size)