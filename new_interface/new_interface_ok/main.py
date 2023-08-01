import sys
from PySide6.QtGui import QAction, QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QStackedWidget, QMenuBar, QLineEdit, QFileDialog, QMessageBox, QCheckBox
from PySide6.QtCore import Qt

import dragDrop as dp
import formatacao as TelaLimpeza
import Graficos as TelaGraficos
import calculos as TelaCalculos
import serieTemporal as TelaSerieTemporal

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ferramenta de pos-processamento")

        # Criar o widget que contém as telas
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Adicionar as telas ao widget stacked
        self.telaLimpeza = TelaLimpeza.TelaLimpeza()
        self.telaSerieTemporal = TelaSerieTemporal.TelaSerieTemporal()
        self.telaCalculos = TelaCalculos.TelaCalculos()
        self.telaGraficos = TelaGraficos.TelaGraficos()

        self.stacked_widget.addWidget(self.telaLimpeza)
        self.stacked_widget.addWidget(self.telaSerieTemporal)
        self.stacked_widget.addWidget(self.telaCalculos)
        self.stacked_widget.addWidget(self.telaGraficos)

        # Criar o menu superior
        menu_bar = QMenuBar(self)

        # Adicionar o menu ao QMainWindow
        self.setMenuBar(menu_bar)

        # Criar as ações para trocar de tela
        action_first_screen = QAction("Formatação Arquivos postProcessing", self)
        action_first_screen.triggered.connect(lambda: self.stacked_widget.setCurrentWidget(self.telaLimpeza))

        action_second_screen = QAction("Serie Temporal", self)
        action_second_screen.triggered.connect(lambda: self.stacked_widget.setCurrentWidget(self.telaSerieTemporal))

        action_third_screen = QAction("Cálculos e Estatísticas", self)
        action_third_screen.triggered.connect(lambda: self.stacked_widget.setCurrentWidget(self.telaCalculos))

        action_fourth_screen = QAction("Gráficos", self)
        action_fourth_screen.triggered.connect(lambda: self.stacked_widget.setCurrentWidget(self.telaGraficos))

        # Adicionar as ações ao menu
        menu_bar.addAction(action_first_screen)
        menu_bar.addAction(action_second_screen)
        menu_bar.addAction(action_third_screen)
        menu_bar.addAction(action_fourth_screen)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())