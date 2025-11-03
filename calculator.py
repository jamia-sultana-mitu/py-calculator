# Basic Calculator Project
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton


class ClaculatorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setStyleSheet("font-size: 20px; padding: 10px;")
        layout.addWidget(self.display)

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        grid_layout = QGridLayout()

        for btn_txt, row, col in buttons:
            button = QPushButton(btn_txt)
            button.setStyleSheet("font-size: 12px; padding: 15px;")
            button.clicked.connect(lambda _, btn=button: self.click(btn))
            grid_layout.addWidget(button, row, col)

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def click(self, btn):
        btn_txt = btn.text()
        txt = self.display.text()
        if btn_txt == "C":
            self.display.clear()
        elif btn_txt == "=":
            try:
                result = eval(txt)
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Error!")
        else:
            self.display.setText(txt + btn_txt)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClaculatorWindow()
    window.show()
    app.exec_()
