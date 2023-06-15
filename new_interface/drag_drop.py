from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton
from PySide6.QtGui import QDragEnterEvent, QDropEvent, Qt
import os as op

class DragDropWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.paths = []
        self.urls = []
        self.show_urls = []

        self.setWindowTitle("Informe os arquivos a serem utilizados")
        self.layout = QVBoxLayout()

        self.setLayout(self.layout)

        self.label = QLabel("Arraste e solte aqui")
        self.label.setMinimumSize(200, 200)
        self.label.setStyleSheet("border: 2px dashed gray;")
        

        self.layout.addWidget(self.label)
        self.button_clean()

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls() or event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            for url in urls:
                self.urls.append(url.toLocalFile())
                self.show_urls.append(op.path.basename(str(url.toLocalFile())))
                self.show_urls.append("<br>")

        self.label.setText(f'''{str(self.show_urls)}''')

    def clean(self):
        self.show_urls = []
        self.urls = []
        self.label.setText(f'''{str(self.show_urls)}''')

    def button_clean(self):
        self.button = QPushButton("Limpar", self)
        self.button.clicked.connect(
            self.clean
            )
        
        self.layout.addWidget(self.button)