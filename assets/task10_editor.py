from .DB_management import DB
from .Excel_management import Excel
from PyQt6.QtWidgets import QLabel


class Task10Editor():
    def __init__(self, label: QLabel):
        self.label = label
        pass

    # Получение данных из БД и их запись в Excel
    def get_data(self):
        sql = "SELECT word, rule, formatted, letter FROM Data"
        data = DB.exec(sql)
        Excel.to_excel(data)

    # Проверка корректности отредактированных пользователем данных
    def check_data(self):
        self.label.setText('текст22')
        Excel.from_excel()

    # Обновление БД
    def update_data(self):
        pass

    def check_wb(self):
        return Excel.wb is not None