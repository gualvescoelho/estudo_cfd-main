import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from checkbox import checkbox
from button import button

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Layout principal
        self.layout = QVBoxLayout()


        self.setWindowTitle("Página Principal")

        self.checkbox = checkbox()
        self.button = button(self.checkbox.values)

        self.layout.addWidget(self.button.drag_drop())

        self.layout.addWidget(self.checkbox)
        
        self.layout.addWidget(self.button)

        # Widget central
        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
