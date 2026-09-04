import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.addButton.clicked.connect(self.add_item)
        self.ui.deleteButton.clicked.connect(self.delete_item)

    def add_item(self):
        text = self.ui.lineEdit.text()  # припустимо, є поле вводу
        if text:
            self.ui.listWidget.addItem(text)
            self.ui.lineEdit.clear()

    def delete_item(self):
        row = self.ui.listWidget.currentRow()
        if row >= 0:
            self.ui.listWidget.takeItem(row)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())