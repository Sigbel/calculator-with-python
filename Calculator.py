import sys

# Functions
from math import sqrt

# PyQt5
from PyQt5.QtGui import QKeyEvent, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

# Interface
from interface.main_window import *

class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowIcon(QIcon("resources\calculator-svg.svg"))

        self.atr_buttons()

        self.last_oper = ""
        self.num_backup = ""
        self.equal_ative = False
        self.last_num_ative = False
        self.comma_ative = False

    # maps keys to functions
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
            self.equals_clicked("e")
        elif key == Qt.Key_Enter:
            self.equals_clicked("e")
        elif key == Qt.Key_Plus:
            self.operation_clicked("+")
        elif key == Qt.Key_Minus:
            self.operation_clicked("-")
        elif key == Qt.Key_Asterisk:
            self.operation_clicked("*")
        elif key == Qt.Key_Slash:
            self.operation_clicked("/")
        elif key == Qt.Key_Period:
            self.number_clicked(",")
        elif key == Qt.Key_Comma:
            self.number_clicked(",")

    # assigning buttons to their respective functions
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
            (self.btn_plus_minus, self.change_signal),
            (self.btn_percent, self.percentage_clicked),
            (self.btn_raisedTotwo, self.square_clicked),
            (self.btn_squareRoot, self.square_root_clicked),
            (self.btn_mult, self.operation_clicked),
            (self.btn_division, self.operation_clicked),
            (self.btn_comma, self.number_clicked),
        ]

        for btn, method in buttons:
            btn.clicked.connect(method)

    # function that captures the key typed or pressed
    def number_clicked(self, number=None):

        if self.label_visu.text().endswith("="):
            self.label_visu.clear()
            self.label_res.clear()

        if self.label_res.text() in ["0", "Error", self.label_visu.text()[:-1]]:
            self.label_res.clear()

        if number:
            button = number
        else:
            button_test = self.sender()
            button = button_test.text()

        if button == ",":
            button = "."
            if "." in self.label_res.text():
                self.label_res.setText(self.label_res.text())
            else:
                self.label_res.setText(self.label_res.text() + button)
        else:
            self.label_res.setText(self.label_res.text() + button)

    # function to clear results e visualization
    def clear_clicked(self):
        self.label_res.setText("0")
        self.label_visu.clear()

    # function to clear results
    def cancelEntry_clicked(self):
        self.label_res.setText("0")

    # function that captures the operation selected
    def operation_clicked(self, operation=None):
        self.last_num_ative = True

        if operation:
            button = operation
        else:
            button_test = self.sender()

            if button_test.text() == "x":
                button = "*"
            elif button_test.text() == "÷":
                button = "/"
            else:
                button = button_test.text()

        label_res = self.label_res.text()

        self.last_oper = button

        try:
            if self.label_visu.text() == "":
                expression = label_res

                result = eval(expression)

                self.label_visu.setText(str(result) + button)

            else:
                print(eval(self.label_visu.text()[:-1]))
                if self.label_visu.text()[:-1] == label_res:
                    self.equal_ative = False
                    return

                if self.equal_ative == True and str(
                    eval(self.label_visu.text()[:-1])
                ) in [label_res]:
                    self.label_visu.setText(label_res + button)
                    self.equal_ative = False
                    return

                if label_res in ["", "0"]:
                    self.label_visu.setText(self.label_visu.text()[:-1] + button)
                    self.equal_ative = False
                    return

                expression = (self.label_visu.text()[:-1]) + button + label_res

                result = eval(expression)

                self.label_visu.setText(str(result) + button)
                self.equal_ative = False

        except Exception as e:
            self.label_res.setText("Error")

        self.label_res.setText(self.label_visu.text()[:-1])

    # function that captures whether the equal key was used
    def equals_clicked(self, mode=None):
        operation = self.last_oper

        if self.last_num_ative:
            self.num_backup = self.label_res.text()

        if mode:
            button = "="
        else:
            button_test = self.sender()
            button = button_test.text()

        label_res = self.label_res.text()

        if self.label_visu.text() in [""]:
            expression = label_res

        else:
            if self.num_backup:
                if self.label_visu.text().split(operation)[1] == "":
                    expression = (
                        self.label_visu.text()[:-1] + self.last_oper + self.num_backup
                    )
                else:
                    expression = label_res + self.last_oper + self.num_backup
            else:
                expression = self.label_visu.text() + label_res

        try:
            print(expression)
            result = eval(expression)

            expression_2 = expression.split(operation)

            if self.num_backup:
                self.label_visu.setText(
                    expression_2[0] + self.last_oper + self.num_backup + button
                )
            else:
                self.label_visu.setText(str(result) + button)

            self.label_res.setText(str(result))
            self.equal_ative = True
            self.last_num_ative = False
        except Exception:
            self.label_res.setText("Error")

    # function that captures wheter the back key was used
    def back_clicked(self):
        current_text = self.label_res.text()

        if current_text[:-1] == "":
            self.label_res.setText("0")
        else:
            self.label_res.setText(current_text[:-1])

    # function that captures wheter the square root key was used
    def square_root_clicked(self):
        current_value = float(self.label_res.text())
        self.label_res.setText(str(sqrt(current_value)))

    # function that captures wheter the square key was used
    def square_clicked(self):
        current_value = float(self.label_res.text())
        self.label_res.setText(str(current_value**2))

    # function that captures wheter the inverse key was used
    def inverse_clicked(self):
        current_value = float(self.label_res.text())
        self.label_res.setText(str(1 / current_value))

    # function that captures wheter the percentage key was used
    def percentage_clicked(self):
        current_value = float(self.label_res.text())
        self.label_res.setText(str(current_value / 100))

    # function that captures wheter the change sinal key was used
    def change_signal(self):
        current_value = float(self.label_res.text())
        if current_value == "0":
            return
        self.label_res.setText(str(-current_value))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    app.exec_()
