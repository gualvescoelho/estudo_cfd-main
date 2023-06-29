import os as op
from PySide6.QtWidgets import QPushButton, QFileDialog
from drag_drop import DragDropWidget as dp

# Subclasse QMainWindow para criar a janela principal da aplicação
class button(QPushButton):
    def __init__(self, parent):
        super().__init__()

    def creation_button(self, parent):
        button = QPushButton("Confirmar", self)
        button.clicked.connect(parent.confirm)

    # Método de slot para lidar com o clique no botão
    def process(self, parent):
        self.open_dialog()
        op.system('mkdir "' + self.diretorio_saida + '/vel_media"')
        op.system('mkdir "' + self.diretorio_saida + '/coordenadas"')
        op.system('mkdir "' + self.diretorio_saida + '/vel_media_grafico"')
        op.system('mkdir "' + self.diretorio_saida + '/desvio_padrao"')

        for url in self.dragdrop_widget.urls:
            # self.limpeza(url)
            
            self.read_file(url)
            # criação dessa regra de negocio
            if self.first == '#':
                self.limpeza(url)

            self.processing(url, str(self.qnt_coord), '200', parent.values)


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

    def processing(self, url, qtd_coord, itmin, values):
        string = 'start new_c "' + url + '" '+ qtd_coord +" "+ itmin +" "+ self.lines +" "+ values + ' "' + self.diretorio_saida + '"'
        print("string ", string)
        op.system(
            string
        )

    def drag_drop(self):
        self.dragdrop_widget = dp()
        return self.dragdrop_widget
        
    def read_file(self, url):
        with open(url, 'r') as arquivo:

            # informa o primeiro caracter do arquivo e volta ao inicio com fim de verificar as linhas
            first = arquivo.read(1)
            arquivo.seek(0)
            read = arquivo.read()
            qtd_coord = self.getting_qtd_coord(read, first)
            arquivo.seek(0)

            
            # retornar a quantidade de iterações e subtrair pela quantidade de coordenadas
            len = arquivo.readlines()
        
        size = int(len.__len__()) - int(qtd_coord) - 2

        # Imprimir os caracteres lidos
        self.qnt_coord = str(qtd_coord)
        self.first = str(first)
        self.lines = str(size)

    def getting_qtd_coord(self, file, first):
        if first != '#':
            i = 0
            for x in file:
                if x == '\n':
                    a += 1
                    i += 1
                else:
                    a = 0
                if(a == 2):
                    return i - 1
        else:
            qtd_coord = file.count('#')
            return qtd_coord - 1