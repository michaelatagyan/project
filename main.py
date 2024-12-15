import io
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from template import template
from possible_words import stress_dict
from docx import Document
from task import tsk
import subprocess, os


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()
        self.current_task = None

    def initUI(self):
        self.amount.setEnabled(False)
        self.amount.setVisible(False)

        self.baton.setEnabled(False)
        self.baton.setVisible(False)

        self.kolvo.setVisible(False)
        self.scs.setVisible(False)

        self.Btn_4.clicked.connect(self.task_4)
        self.Btn_mix.clicked.connect(self.task_19plus)
        self.Btn_10.clicked.connect(self.task_10)
        self.baton.clicked.connect(self.generate)

        self.setWindowTitle('Подготовка к ЕГЭ по русскому языку')
        self.words = stress_dict

    def generate(self):
        if self.current_task == 4:
            self.create_task_4()
        elif self.current_task == 10:
            self.create_task_10()
        elif self.current_task == 19:
            self.create_task_19plus()

    def task_10(self):
        self.kolvo.setVisible(True)
        self.amount.setEnabled(True)
        self.amount.setVisible(True)
        self.baton.setEnabled(True)
        self.baton.setVisible(True)

        # self.Btn_4.setEnabled(False)
        # self.Btn_4.setVisible(False)
        # self.Btn_mix.setEnabled(False)
        # self.Btn_mix.setVisible(False)

        self.label.setText('Генерация для задания: 10')
        # self.baton.clicked.connect(self.create_task_10)
        self.current_task = 10

    def create_task_10(self):
        k = int(self.amount.text())
        tsk.answers = []
        dc = Document()
        path = self.save_file()
        dc.save(path)
        for i in range(k):
            tsk.fill_10(path, i + 1)
        tsk.fill_doc(tsk.answers, path)
        self.scs.setVisible(True)
        if os.name == 'nt':  # Windows
            os.startfile(path)
        elif os.name == 'posix':  # macOS, Linux
            subprocess.run(['open', path])

    def task_4(self):
        self.kolvo.setVisible(True)
        self.amount.setEnabled(True)
        self.amount.setVisible(True)
        self.baton.setEnabled(True)
        self.baton.setVisible(True)

        # self.Btn_10.setEnabled(False)
        # self.Btn_10.setVisible(False)
        # self.Btn_mix.setEnabled(False)
        # self.Btn_mix.setVisible(False)

        self.label.setText('Генерация для задания: 4')
        self.current_task = 4
        # self.baton.clicked.connect(self.create_task_4)

    def create_task_4(self):
        k = int(self.amount.text())
        tsk.answers = []
        dc = Document()
        path = self.save_file()
        dc.save(path)
        cnt = 1
        for i in range(k):
            correct = tsk.fill_correct()
            incorrect = tsk.fill_incorrect()
            mixed = tsk.fill_mixed()
            answers = tsk.fill_answers(mixed)
            dc = tsk.create_word_doc(mixed, path, cnt)
            dc.save(path)
            cnt += 1
        tsk.fill_doc(tsk.answers, path)
        self.scs.setVisible(True)
        if os.name == 'nt':  # Windows
            os.startfile(path)
        elif os.name == 'posix':  # macOS, Linux
            subprocess.run(['open', path])
        # print(correct, incorrect, mixed, answers, sep='\n')

    def task_19plus(self):
        self.kolvo.setVisible(True)
        self.amount.setEnabled(True)
        self.amount.setVisible(True)
        self.baton.setEnabled(True)
        self.baton.setVisible(True)

        # self.Btn_4.setEnabled(False)
        # self.Btn_4.setVisible(False)
        # self.Btn_10.setEnabled(False)
        # self.Btn_10.setVisible(False)

        self.label.setText('Генерация для задания: 19-21')
        # self.baton.clicked.connect(self.create_task_19plus)
        self.current_task = 19

    def create_task_19plus(self):
        k = int(self.amount.text())
        dc = Document()
        tsk.answers = []
        par = dc.add_paragraph()
        par.add_run('Здесь и далее примеры взяты из Национального корпуса русского языка (ruscorpora.ru)')
        dc.add_paragraph()
        path = self.save_file()
        dc.save(path)
        c = 1
        for i in range(k):
            tsk.fill_19plus(path, c)
            c += 1

        tsk.fill_doc(tsk.answers, path)
        self.scs.setVisible(True)
        if os.name == 'nt':  # Windows
            os.startfile(path)
        elif os.name == 'posix':  # macOS, Linux
            subprocess.run(['open', path])

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(
            caption="Сохранение файла",
            filter="MS Word (*.docx)"
        )
        return file_path


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
