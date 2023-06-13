import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton

# buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)

        dlg = QDialog(self)
        dlg.setWindowTitle("HELLO!")
        dlg.exec_()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()