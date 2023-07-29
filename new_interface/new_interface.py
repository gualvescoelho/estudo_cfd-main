import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QMessageBox, QFileDialog 
from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import QDragEnterEvent, QDropEvent

import new_interface_back as nb

class DragDropWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("My App")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Arraste e solte arquivos aqui", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMinimumSize(200, 200)
        self.label.setStyleSheet("border: 2px dashed gray;")

        self.layout.addWidget(self.label)

        # Botão de limpar
        self.button_clear = QPushButton("Limpar Arquivos", self)
        self.button_clear.clicked.connect(self.clear_files)
        self.layout.addWidget(self.button_clear)

        # Botão de consultar campos
        self.button_consult = QPushButton("Consultar Campos", self)
        self.button_consult.clicked.connect(self.process_files)
        self.layout.addWidget(self.button_consult)

        # Habilitar a recepção de drops
        self.setAcceptDrops(True)

        # Lista de arquivos
        self.file_paths = []

        # Dicionário para armazenar informações por arquivo
        self.file_info = {}

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            self.file_paths = [url.toLocalFile() for url in urls]

            # Atualizar o texto do label com os nomes dos arquivos
            file_names = [file_path.split("/")[-1] for file_path in self.file_paths]
            self.label.setText("\n".join(file_names))

            # Limpar o dicionário de informações ao receber novos arquivos
            self.file_info = {file_name: {} for file_name in file_names}

            # Exemplo: imprimir os caminhos dos arquivos no console
            print("Arquivos arrastados:")
            for file_path in self.file_paths:
                print(file_path)

    def clear_files(self):
        # Limpar a lista de arquivos, o texto exibido no label e o dicionário de informações
        self.file_paths = []
        self.label.setText("Arraste e solte arquivos aqui")
        self.file_info = {}

    def process_files(self):
        self.main_window.process_files(self.file_info)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.nb = nb.new_interface_back()
        self.setWindowTitle("My App")
        self.layout = QVBoxLayout()

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        # Drag and Drop Widget
        self.drag_drop_widget = DragDropWidget(self)
        self.layout.addWidget(self.drag_drop_widget)

        # Campos de entrada
        self.input_itmin = QLineEdit(self)
        self.input_itmin.setPlaceholderText("A partir de qual iteração considerar?")
        self.layout.addWidget(self.input_itmin)

        self.input_serie_temporal = QLineEdit(self)
        self.input_serie_temporal.setPlaceholderText("Série Temporal da Iteração")
        self.layout.addWidget(self.input_serie_temporal)

        self.checkboxx = []  # Lista para armazenar as checkboxes geradas
        self.creation_checkbox()

        # Botão de confirmação
        self.button_submit = QPushButton("Confirmar", self)
        self.button_submit.clicked.connect(self.confirm_button)
        self.layout.addWidget(self.button_submit)

    def select_directory(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(self, "Selecionar Diretório de Saída", options=options)
        if directory:
            return directory

    def creation_checkbox(self):
        self.add_legendas("VELOCIDADES")
        self.generate_checkbox("Velocidade x")
        self.generate_checkbox("Velocidade y")
        self.generate_checkbox("Velocidade z")
        self.generate_checkbox("Velocidades gerais")

        self.add_legendas("COORDENADA")
        self.generate_checkbox("Gerar arquivo com coordenadas")

        self.add_legendas("GRÁFICOS")
        self.generate_checkbox("Velocidade gráfico x")
        self.generate_checkbox("Velocidade gráfico y")
        self.generate_checkbox("Velocidade gráfico z")

        self.add_legendas("DESVIO PADRÃO")
        self.generate_checkbox("Calcular desvio padrão de x")
        self.generate_checkbox("Calcular desvio padrão de y")
        self.generate_checkbox("Calcular desvio padrão de z")

    def generate_checkbox(self, text):
        checkbox = QCheckBox(text, self)
        checkbox.setChecked(False)  # Inicia desmarcado (valor 0)
        checkbox.stateChanged.connect(self.checkbox_state_changed)
        self.layout.addWidget(checkbox)
        self.checkboxx.append(checkbox)

    def checkbox_state_changed(self, state):
        # Quando o checkbox é marcado, seu valor será 1
        sender = self.sender()
        if state == Qt.Checked:
            sender.setProperty("valor", 1)
        else:
            sender.setProperty("valor", 0)

    def add_legendas(self, text):
        title = QLabel(text, self)
        self.layout.addWidget(title)

    def get_checkbox_values(self):
        print("Checkbox")
        print(self.checkboxx)
        # Retorna uma lista de inteiros (0 ou 1) representando os valores dos checkboxes
        return [int(checkbox.isChecked()) for checkbox in self.checkboxx]

    def confirm_button(self):
        itmin = self.input_itmin.text()
        serie_temporal = self.input_serie_temporal.text()

        if(serie_temporal.__len__() < 0):
            serie_temporal = 0

        if not self.drag_drop_widget.file_paths:
            self.show_warning_message("Nenhum arquivo foi inserido!")
            return

        if not itmin:
            self.show_warning_message("Os cálculos vão utilizar o momento zero como início.")

        checkboxes_values = self.get_checkbox_values()

        self.selected_directory = self.select_directory()

        # Verifica se um diretório foi selecionado
        if not self.selected_directory:
            self.show_warning_message("Nenhum diretório selecionado!")
            return

        for path in self.drag_drop_widget.file_paths:
            string = path + str(itmin) + str(checkboxes_values) + self.selected_directory
            print(string)
            self.nb.process(itmin, path, str(checkboxes_values), serie_temporal, self.selected_directory)

        # Aqui você pode fazer o que quiser com as informações preenchidas
        # Neste exemplo, estamos apenas imprimindo-as no console.
        print("itmin:", itmin)
        print("Série Temporal:", serie_temporal)
        print("Valores dos Checkboxes:", checkboxes_values)

    def show_warning_message(self, message):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Aviso")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def process_files(self, file_info):
        # Método para processar os arquivos e suas informações
        print("Arquivos e informações recebidos:")
        for file_name, info in file_info.items():
            print(f"Nome do Arquivo: {file_name}")
            print(f"Valor de itmin: {info.get('itmin')}")
            print(f"Série Temporal: {info.get('serie_temporal')}")
            print("Campos marcados:")
            for checkbox in self.checkboxx:
                if checkbox.isChecked():
                    print(f"- {checkbox.text()}")
            print()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
