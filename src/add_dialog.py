from PySide6.QtWidgets import QDialog
from ui_generated.ui_dialog import Ui_Dialog

class AddDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.rankEdit.addItems([
            "Солдат", "Молодший сержант", "Сержант",
            "Старший сержант", "Молодший лейтенант", "Лейтенант"
        ])

        self.ui.okButton.clicked.connect(self.accept)
        self.ui.cancelButton.clicked.connect(self.reject)

    def get_data(self):
        name = self.ui.nameEdit.text().strip()
        rank = self.ui.rankEdit.currentText().strip()
        return name, rank