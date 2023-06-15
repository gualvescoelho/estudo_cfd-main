from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QDragEnterEvent, QDropEvent, Qt

paths = []

class DragDropWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.paths = []
        self.urls = []
        self.setWindowTitle("Informe os arquivos a serem utilizados")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Arraste e solte aqui")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMinimumSize(200, 200)
        self.label.setStyleSheet("border: 2px dashed gray;")

        self.layout.addWidget(self.label)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls() or event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            for url in urls:
                self.urls.append(url.toLocalFile())
                print("Arquivo arrastado:", url.toLocalFile())
                self.label.setText(f"Arquivo: {url.toLocalFile()}")
        elif event.mimeData().hasText():
            text = event.mimeData().text()
            print("Texto arrastado:", text)

        print("urls1", self.urls)

    def get_paths():
        return paths