import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel
from checkbox import checkbox
from button import button

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Layout principal
        self.layout = QVBoxLayout()
        self.checkboxx = []
        self.values = ''
        self.setWindowTitle("Página Principal")
        
        self.checkbox = checkbox()
        self.button = button(self)
        self.input = QLineEdit()

        self.layout.addWidget(self.button.drag_drop())

        self.button.creation_button(self)
        self.checkbox.creation_checkbox(self)

        self.layout.addWidget(self.checkbox)

        title = QLabel()
        title.setText("Gerar Série Temporal do Ponto: ")
        self.layout.addWidget(title)
        self.layout.addWidget(self.input)

        self.layout.addWidget(self.button)

        # Widget central
        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)

    def confirm(self):
        self.serie_temporal()
        self.button.process(self)
        self.show_values()

    def show_values(self):
            self.values = ''
            self.calling_string = []
            for value in self.checkboxx:
                self.values += str(int(value.isChecked()))+" "
                self.calling_string.append(int(value.isChecked()))

    def serie_temporal(self):
        if self.input.text().isnumeric():
            self.values += "1 "
            self.values += self.input.text()+" "
            self.calling_string.append(1)
            self.calling_string.append(int(self.input.text()))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
