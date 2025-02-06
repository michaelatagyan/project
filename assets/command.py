
from .Basecommand import bus, Basecommand
from PyQt6.QtWidgets import QLabel


class Command(Basecommand):
    def __init__(self, label: QLabel):
        self.label = label
        bus.text_changer = self


    def new_text(self, txt):
        self.label.setText(txt)
