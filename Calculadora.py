import sys

from math import sqrt

from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

from interface.main_window import *


class Calculadora(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.atr_buttons()

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        key = a0.key()

        if key == Qt.Key_0:
            self.number_clicked("0")
        elif key == Qt.Key_1:
            self.number_clicked("1")
        elif key == Qt.Key_2:
            self.number_clicked("2")
        elif key == Qt.Key_3:
            self.number_clicked("3")
        elif key == Qt.Key_4:
            self.number_clicked("4")
        elif key == Qt.Key_5:
            self.number_clicked("5")
        elif key == Qt.Key_6:
            self.number_clicked("6")
        elif key == Qt.Key_7:
            self.number_clicked("7")
        elif key == Qt.Key_8:
            self.number_clicked("8")
        elif key == Qt.Key_9:
            self.number_clicked("9")
        elif key == Qt.Key_Backspace:
            self.back_clicked()
        elif key == Qt.Key_Delete:
            self.clear_clicked()
        elif key == Qt.Key_Return:
            self.equals_clicked()
        elif key == Qt.Key_Plus:
            self.plus_pressed()
        elif key == Qt.Key_Minus:
            self.minus_pressed()
        elif key == Qt.Key_Asterisk:
            self.mult_pressed()
        elif key == Qt.Key_Slash:
            self.division_pressed()
        elif key == Qt.Key_Period:
            self.comma_pressed()

    # Atribuição dos botões às respectivas funções
    def atr_buttons(self):
        buttons = [
            (self.btn_0, self.number_clicked),
            (self.btn_1, self.number_clicked),
            (self.btn_2, self.number_clicked),
            (self.btn_3, self.number_clicked),
            (self.btn_4, self.number_clicked),
            (self.btn_5, self.number_clicked),
            (self.btn_6, self.number_clicked),
            (self.btn_7, self.number_clicked),
            (self.btn_8, self.number_clicked),
            (self.btn_9, self.number_clicked),
            (self.btn_back, self.back_clicked),
            (self.btn_cancelEntry, self.cancelEntry_clicked),
            (self.btn_clear, self.clear_clicked),
            (self.btn_divByone, self.inverse_clicked),
            (self.btn_equal, self.equals_clicked),
            (self.btn_minus, self.operation_clicked),
            (self.btn_plus, self.operation_clicked),
            (self.btn_plus_minus, self.number_clicked),
            (self.btn_percent, self.percentage_clicked),
            (self.btn_raisedTotwo, self.square_clicked),
            (self.btn_squareRoot, self.square_root_clicked),
            (self.btn_mult, self.operation_clicked),
            (self.btn_division, self.operation_clicked),
            (self.btn_comma, self.number_clicked),
        ]

        for btn, method in buttons:
            btn.clicked.connect(method)

    def number_clicked(self, number=None):
        if self.label_res.text() == "0" or self.label_res.text() == "Error":
            self.label_res.clear()

        if number:
            self.label_res.setText(self.label_res.text() + number)

        else:
            button = self.sender()
            self.label_res.setText(self.label_res.text() + button.text())

    def clear_clicked(self):
        self.label_res.setText("0")
        self.label_visu.clear()

    def cancelEntry_clicked(self):
        self.label_res.setText("0")

    def operation_clicked(self):
        button_test = self.sender()

        # if button_test.text() == "X":
        #     button = "*"
        # elif button_test.text() == "÷":
        #     button = "/"
        # else:
        #     button = button_test.text()

        # try:
        #     if self.label_visu.text() == "":   
        #         expression = self.label_res.text()

        #         print(expression)
        #         result = eval(expression)

        #         print(result)
        #         self.label_visu.setText(str(result) + button)
        #     else:
        #         expression = self.label_visu.text() + button + self.label_res.text()

        #         print(expression)
        #         result = eval(expression)

        #         print(result)
        #         self.label_visu.setText(str(result) + button)
        # except Exception:
        #     self.label_res.setText("Error")


        self.label_res.clear()


    def equals_clicked(self):
        expression = self.label_res.text()
        try:
            result = eval(expression)
            self.label_res.setText(str(result))
        except Exception:
            self.label_res.setText("Error")

    def back_clicked(self):
        current_text = self.label_res.text()
        self.label_res.setText(current_text[:-1])

    def square_root_clicked(self):
        current_value = float(self.label_res.text())
        self.label_res.setText(str(sqrt(current_value)))

    def square_clicked(self):
        current_value = float(self.label_res.text())
        self.label_res.setText(str(current_value**2))

    def inverse_clicked(self):
        current_value = float(self.label_res.text())
        self.label_res.setText(str(1 / current_value))

    def percentage_clicked(self):
        current_value = float(self.label_res.text())
        self.label_res.setText(str(current_value / 100))

    def plus_pressed(self):
        pass

    def minus_pressed(self):
        pass

    def mult_pressed(self):
        pass

    def division_pressed(self):
        pass

    def comma_pressed(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculadora()
    calculator.show()
    app.exec_()
