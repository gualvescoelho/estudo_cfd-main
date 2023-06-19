import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QLabel
)

from drag_drop import DragDropWidget as dp
from button import button

# verificar se o arquivo veio limpo ou sujo
# ler as coordenadas e quantidade de linhas automaticamente e pgtar o itmin
# contar a quantidade coordenadas quando nao tiver #
# criar entrada de dados para o itmin

class checkbox(QMainWindow):
    def __init__(self):
        super(checkbox, self).__init__()

        self.setWindowTitle("My App")
        
        self.layout = QVBoxLayout()
        self.values = ""
        self.button = button(self.values)

        self.widget = QWidget()
        
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def creation_checkbox(self, parent):
        self.add_legendas("VELOCIDADES")
        self.generate_checkbox("Velocidade x: ", parent)
        self.generate_checkbox("Velocidade y: ", parent)
        self.generate_checkbox("Velocidade z: ", parent) 
        self.generate_checkbox("Velocidades gerais: ", parent)
        
        self.add_legendas("COORDENADA")
        self.generate_checkbox("Gerar arquivo com coordenadas? ", parent)

        self.add_legendas("GRAFICOS")
        self.generate_checkbox("Velocidade grafico x:  ", parent)
        self.generate_checkbox("Velocidade grafico y:  ", parent)
        self.generate_checkbox("Velocidade grafico z:  ", parent)

        self.add_legendas("DESVIO PADRAO")
        self.generate_checkbox("Calcular desvio padrão de x: ", parent)
        self.generate_checkbox("Calcular desvio padrão de y: ", parent)
        self.generate_checkbox("Calcular desvio padrão de z: ", parent)
        
    def generate_checkbox(self, text, parent):
        checkbox = QCheckBox()
        checkbox.setCheckState(Qt.CheckState.Checked)
        checkbox.setText(text)
        checkbox.setChecked(False)
        checkbox.stateChanged.connect(parent.show_values)

        self.layout.addWidget(checkbox)
        parent.checkboxx.append(checkbox)

    def add_legendas(self, text):
        title = QLabel()
        title.setText(text)
        self.layout.addWidget(title)

    def confirm_button(self):
        self.button = button(self.values)
        self.layout.addLayout(self.button, self.str_values)