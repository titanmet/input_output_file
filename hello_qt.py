# -- coding: utf-8 --

import sys
import time

from PyQt4 import QtCore
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QApplication, QMainWindow, QFont

from my_bot import TextBot
from text_bot_gui import Ui_MainWindow


# Вызов окна (можно применять к любым окнам)
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.jake = TextBot('...')
        self.jake.answer_the_question()
        self.Main_text_window.setText(str(self.jake.bot_dialog_memory))

        self.font = QFont()

        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(30)

        self.label.setGeometry(QtCore.QRect(150, 70, 70, 50))
        self.label.setText('Bot: '+self.jake.bot_name)

        self.connect(self.pushButton, SIGNAL('clicked()'), self.show_answer)

        self.horizontalSlider.valueChanged.connect(self.font_resize)

        self.horizontalSlider.valueChanged.connect(self.lcdNumber.display)

    def font_resize(self, value):
        self.font.setPointSize(value)
        self.font.setWeight(value)
        self.label.setFont(self.font)
        self.Main_text_window.setFont(self.font)
        self.input_text_line.setFont(self.font)

    def show_answer(self):
        self.jake.input = self.input_text_line.toPlainText()
        self.input_text_line.clear()
        time.sleep(0.5)
        self.jake.answer_the_question()
        self.Main_text_window.setText(str(self.jake.bot_dialog_memory))

def main():
    '''
    функция для инициализации и отображения нашего основного окна приложения
    '''
    #Класс QApplication руководит управляющей логикой ГПИ и основными настройками.
    #Здеь мы создаем экземпляр класса QAplication передавая ему аргументы из коммандной строки.
    app = QApplication(sys.argv) # где sys.argv список аргументов командной строки, передаваемых сценарию Python.
    #Здсь мы создаем экземпляр класса MainWindow.
    main = MainWindow()
    main.show()
    #Метод show() отображает виджет на экране.Виджет сначала создаётся в памяти, и
    #только потом(с помощью метода show) показывается на экране.
    sys.exit(app.exec_())
    #exec_ запускает цикл обработки сообщений
    #и ждет, пока не будет вызвана exit() или не
    #будет разрушен главный виджет, и возвращает значение установленное в exit().
    #Здесь sys.exit обеспечивает чистый выход из приложения.

main()