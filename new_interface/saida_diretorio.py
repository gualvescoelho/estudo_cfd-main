from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Selecionar Diretório de Saída")

        button = QPushButton("Selecionar Diretório", self)
        button.clicked.connect(self.open_dialog)

        self.setCentralWidget(button)

    def open_dialog(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        directory = QFileDialog.getExistingDirectory(self, "Selecionar Diretório de Saída", options=options)
        if directory:
            print("Diretório selecionado:", directory)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
