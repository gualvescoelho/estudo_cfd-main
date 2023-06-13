from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QDragEnterEvent, QDropEvent, Qt

paths = []

class DragDropWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.paths = []
        self.setWindowTitle("Informe os arquivos a serem utilizados")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Arraste e solte aqui")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMinimumSize(200, 200)
        self.label.setStyleSheet("border: 2px dashed gray;")

        self.layout.addWidget(self.label)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            file_path = urls[0].toLocalFile()
            self.label.setText(f"Arquivo: {file_path}")
            paths.append(file_path)

    def get_paths():
        return paths