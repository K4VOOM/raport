import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QListWidgetItem
from PySide6.QtCore import Qt
from ui_generated.ui_form import Ui_MainWindow
from src.add_dialog import AddDialog
from src import database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.addButton.clicked.connect(self.add_item)
        self.ui.deleteButton.clicked.connect(self.delete_item)

        self.load_from_db()

    def load_from_db(self):
        """Завантажує всіх бійців з БД у список при старті програми."""
        self.ui.listWidget.clear()
        soldiers = database.get_all_soldiers()
        for soldier_id, name, rank in soldiers:
            self.add_list_item(soldier_id, name, rank)

    def add_list_item(self, soldier_id, name, rank):
        """Створює елемент списку і зберігає в ньому id з БД."""
        text = f"{name} — {rank}"
        item = QListWidgetItem(text)
        item.setData(Qt.UserRole, soldier_id)  # ховаємо id всередині елемента
        self.ui.listWidget.addItem(item)

    def add_item(self):
        dialog = AddDialog(self)
        result = dialog.exec()

        if result == QDialog.Accepted:
            name, rank = dialog.get_data()

            if not name or not rank:
                QMessageBox.warning(self, "Помилка", "Заповніть усі поля!")
                return

            soldier_id = database.add_soldier(name, rank)  # записуємо в БД
            self.add_list_item(soldier_id, name, rank)      # додаємо в список

    def delete_item(self):
        row = self.ui.listWidget.currentRow()
        if row >= 0:
            item = self.ui.listWidget.item(row)
            soldier_id = item.data(Qt.UserRole)

            database.delete_soldier(soldier_id)  # видаляємо з БД
            self.ui.listWidget.takeItem(row)      # видаляємо зі списку
        else:
            QMessageBox.information(self, "Увага", "Оберіть елемент для видалення")


database.init_db()  # створюємо таблицю (якщо її ще нема)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())