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

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        self.layout = QVBoxLayout()
        self.checkboxx = []
        self.calling_string = []
        self.values = ""
        self.button = button(self.values)

        self.layout.addWidget(self.button.drag_drop())

        self.creation_checkbox()
        self.layout.addWidget(self.button)

        self.widget = QWidget()
        
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def creation_checkbox(self):
        self.add_legendas("VELOCIDADES")
        self.generate_checkbox("Velocidade x: ")
        self.generate_checkbox("Velocidade y: ")
        self.generate_checkbox("Velocidade z: ") 
        self.generate_checkbox("Velocidades gerais: ")
        
        self.add_legendas("COORDENADA")
        self.generate_checkbox("Gerar arquivo com coordenadas? ")

        self.add_legendas("GRAFICOS")
        self.generate_checkbox("Velocidade grafico x:  ")
        self.generate_checkbox("Velocidade grafico y:  ")
        self.generate_checkbox("Velocidade grafico z:  ")

        self.add_legendas("DESVIO PADRAO")
        self.generate_checkbox("Calcular desvio padrão de x: ")
        self.generate_checkbox("Calcular desvio padrão de y: ")
        self.generate_checkbox("Calcular desvio padrão de z: ")


    def show_values(self):
        self.calling_string = []
        for value in self.checkboxx:
            self.values += str(int(value.isChecked()))+" "
            self.calling_string.append(int(value.isChecked()))
        

    
    def show_state(self, state):
        print(state == Qt.CheckState.Checked.value)
        print(state)
        self.show_values()

    def generate_layout(self):
        for checkbox in self.checkboxx:
            self.layout.addWidget(checkbox)

        return self.layout

    def generate_checkbox(self, text):
        checkbox = QCheckBox()
        checkbox.setCheckState(Qt.CheckState.Checked)
        checkbox.setText(text)
        checkbox.setChecked(False)
        checkbox.stateChanged.connect(self.show_state)

        self.layout.addWidget(checkbox)
        self.checkboxx.append(checkbox)

    def add_legendas(self, text):
        title = QLabel()
        title.setText(text)
        self.layout.addWidget(title)

    def confirm_button(self):
        self.button = button(self.values)
        self.layout.addLayout(self.button, self.str_values)

app = QApplication(sys.argv)    
window = MainWindow()
window.show()
app.exec()