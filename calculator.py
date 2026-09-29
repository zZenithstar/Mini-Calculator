# imports
import sys
import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import (
    QPushButton, QVBoxLayout, QWidget,
    QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QApplication, QSizePolicy, QListWidget
)
from PyQt5.QtWidgets import QLCDNumber
# imports


# features
# decimal point can be added
# multiple operations with operator precedence can be added
# number keys
# if self.easteregg == 10:
#     self.operation_display.setText("pls leave me alone")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator App")
        self.setGeometry(700, 250, 500, 600)
        self.setStyleSheet("background-color: Slate grey;")

        self.color = "White"
        self.easteregg = 0

        self.num1 = QPushButton("1")
        self.num2 = QPushButton("2")
        self.num3 = QPushButton("3")
        self.num4 = QPushButton("4")
        self.num5 = QPushButton("5")
        self.num6 = QPushButton("6")
        self.num7 = QPushButton("7")
        self.num8 = QPushButton("8")
        self.num9 = QPushButton("9")
        self.num0 = QPushButton("0")

        self.plusN = QPushButton("+")
        self.minusN = QPushButton("-")
        self.equalsN = QPushButton("=")
        self.multiN = QPushButton("x")
        self.hundrN = QPushButton("%")
        self.themeB = QPushButton("☀️")
        self.divideN = QPushButton("/")
        self.cE = QPushButton("C")
        self.deleteB = QPushButton("Del")
        self.powerB = QPushButton("**")

        self.answerB = QLCDNumber(self)
        self.answerB.setStyleSheet(
            "background-color: #C0C0C0;"
            "color: black;"
        )

        self.answerBox = QLineEdit()  # display box for the top row

        self.currentnumber = " "
        self.numberone = 0
        self.numbertwo = 0
        self.easternum = 0
        self.operator = " "
        self.new_number_waiting = False

        self.opshower = QLabel("Hello!", self)

        self.historydizi = []
        self.historyB = QPushButton("📜")
        self.historywidget = QListWidget(self)
        self.history_open = False

        self.alldel = QPushButton("🆑", self)

        self.UI()

    # changes the theme
    def setColor(self):
        if self.color == "white":

            self.num1.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.num2.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.num3.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.num4.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.num5.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.num6.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.num7.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.num8.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.num9.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.num0.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.deleteB.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.cE.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.divideN.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.multiN.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.minusN.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.plusN.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.themeB.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.equalsN.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.powerB.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.hundrN.setStyleSheet(""" 
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.answerB.setStyleSheet(
                "background-color: #404040;"
                "color: white;"
            )

            self.opshower.setStyleSheet("""
                QLabel {
                    background-color: #2B2B2B;
                    font-size: 25px;
                    color: white;
                }
            """)

            self.historyB.setStyleSheet("""
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 25px;
                    border: 3px solid white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.historywidget.setStyleSheet("""
                QListWidget {
                    background-color: #2B2B2B;
                    font-size: 30px;
                    border: 3px solid white;
                    color: white;
                }
                QListWidget:hover {
                    background-color: #404040;
                }
                QListWidget:pressed {
                    background-color: #141414;
                }
            """)

            self.alldel.setStyleSheet("""
                QPushButton {
                    background-color: #2B2B2B;
                    font-size: 25px;
                    border: 3px solid white;
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #141414;
                }
            """)

            self.color = "black"

        else:

            self.num1.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.num2.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.num3.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.num4.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.num5.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.num6.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.num7.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.num8.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.num9.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.num0.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.deleteB.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.cE.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.divideN.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.multiN.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.minusN.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.plusN.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.themeB.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.equalsN.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.powerB.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.hundrN.setStyleSheet(""" 
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.answerB.setStyleSheet(
                "background-color: #C0C0C0;"
                "color: black;"
            )

            self.opshower.setStyleSheet("""
                QLabel {
                    background-color: #C0C0C0;
                    font-size: 25px;
                    color: black;
                }
            """)

            self.historyB.setStyleSheet("""
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 25px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.historywidget.setStyleSheet("""
                QListWidget {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                    color: black;
                }
                QListWidget:hover {
                    background-color: grey;
                }
                QListWidget:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.alldel.setStyleSheet("""
                QPushButton {
                    background-color: #C0C0C0;
                    font-size: 30px;
                    border: 3px solid black;
                }
                QPushButton:hover {
                    background-color: grey;
                }
                QPushButton:pressed {
                    background-color: #BDBBD7;
                }
            """)

            self.color = "white"

    # user interface
    def UI(self):
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        main_widget.resize(20, 20)

        # collect all buttons into a list
        all_buttons = [
            self.num1, self.num2, self.num3, self.num4, self.num5,
            self.num6, self.num7, self.num8, self.num9, self.num0,
            self.plusN, self.minusN, self.equalsN, self.multiN,
            self.hundrN, self.themeB, self.divideN, self.cE,
            self.deleteB, self.powerB, self.historyB
        ]

        # make all buttons expand horizontally and vertically
        for btn in all_buttons:
            btn.setSizePolicy(
                QSizePolicy.Expanding,
                QSizePolicy.Expanding
            )

        for btn in all_buttons:
            btn.setSizePolicy(
                QSizePolicy.Expanding,
                QSizePolicy.Expanding
            )
            btn.setFocusPolicy(Qt.NoFocus)

        # outer column
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.historywidget, 1)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # row 1
        self.inside1_layout = QHBoxLayout()
        self.inside1_layout.setSpacing(0)
        self.inside1_layout.setContentsMargins(0, 0, 0, 0)
        self.inside1_layout.addWidget(self.answerB)

        # row 2
        self.inside2_layout = QHBoxLayout()
        self.inside2_layout.setSpacing(0)
        self.inside2_layout.setContentsMargins(0, 0, 0, 0)
        self.inside2_layout.addWidget(self.themeB)
        self.inside2_layout.addWidget(self.cE)
        self.inside2_layout.addWidget(self.deleteB)
        self.inside2_layout.addWidget(self.equalsN)

        # row 3
        self.inside3_layout = QHBoxLayout()
        self.inside3_layout.setSpacing(0)
        self.inside3_layout.setContentsMargins(0, 0, 0, 0)
        self.inside3_layout.addWidget(self.num1)
        self.inside3_layout.addWidget(self.num2)
        self.inside3_layout.addWidget(self.num3)
        self.inside3_layout.addWidget(self.plusN)

        # row 4
        self.inside4_layout = QHBoxLayout()
        self.inside4_layout.setSpacing(0)
        self.inside4_layout.setContentsMargins(0, 0, 0, 0)
        self.inside4_layout.addWidget(self.num4)
        self.inside4_layout.addWidget(self.num5)
        self.inside4_layout.addWidget(self.num6)
        self.inside4_layout.addWidget(self.minusN)

        # row 5
        self.inside5_layout = QHBoxLayout()
        self.inside5_layout.setSpacing(0)
        self.inside5_layout.setContentsMargins(0, 0, 0, 0)
        self.inside5_layout.addWidget(self.num7)
        self.inside5_layout.addWidget(self.num8)
        self.inside5_layout.addWidget(self.num9)
        self.inside5_layout.addWidget(self.multiN)

        # row 6
        self.inside6_layout = QHBoxLayout()
        self.inside6_layout.setSpacing(0)
        self.inside6_layout.setContentsMargins(0, 0, 0, 0)
        self.inside6_layout.addWidget(self.hundrN)
        self.inside6_layout.addWidget(self.num0)
        self.inside6_layout.addWidget(self.powerB)
        self.inside6_layout.addWidget(self.divideN)

        # top row
        self.inside0_layout = QHBoxLayout()
        self.inside0_layout.setSpacing(0)
        self.inside0_layout.setContentsMargins(0, 0, 0, 0)
        self.inside0_layout.addWidget(self.historyB, 1)
        self.inside0_layout.addWidget(self.alldel, 1)
        self.inside0_layout.addWidget(self.opshower, 8)
        self.opshower.setAlignment(Qt.AlignRight)

        # put everything together
        self.outside1_layout = QVBoxLayout()
        self.outside1_layout.setSpacing(0)
        self.outside1_layout.setContentsMargins(0, 0, 0, 0)

        self.outside1_layout.addLayout(self.inside0_layout, 1)
        self.outside1_layout.addLayout(self.inside1_layout, 3)
        self.outside1_layout.addLayout(self.inside2_layout, 2)
        self.outside1_layout.addLayout(self.inside3_layout, 2)
        self.outside1_layout.addLayout(self.inside4_layout, 2)
        self.outside1_layout.addLayout(self.inside5_layout, 2)
        self.outside1_layout.addLayout(self.inside6_layout, 2)

        self.main_layout.addLayout(self.outside1_layout, 1)
        main_widget.setLayout(self.main_layout)

        self.historywidget.hide()

        self.num1.clicked.connect(lambda _: self.press_number("1"))
        self.num2.clicked.connect(lambda _: self.press_number("2"))
        self.num3.clicked.connect(lambda _: self.press_number("3"))
        self.num4.clicked.connect(lambda _: self.press_number("4"))
        self.num5.clicked.connect(lambda _: self.press_number("5"))
        self.num6.clicked.connect(lambda _: self.press_number("6"))
        self.num7.clicked.connect(lambda _: self.press_number("7"))
        self.num8.clicked.connect(lambda _: self.press_number("8"))
        self.num9.clicked.connect(lambda _: self.press_number("9"))
        self.num0.clicked.connect(lambda _: self.press_number("0"))

        self.plusN.clicked.connect(lambda: self.press_operator("+"))
        self.minusN.clicked.connect(lambda: self.press_operator("-"))
        self.multiN.clicked.connect(lambda: self.press_operator("*"))
        self.divideN.clicked.connect(lambda: self.press_operator("/"))
        self.hundrN.clicked.connect(lambda: self.press_operator("%"))
        self.powerB.clicked.connect(lambda: self.press_operator("**"))

        self.equalsN.clicked.connect(self.press_equals)
        self.cE.clicked.connect(self.clear)
        self.deleteB.clicked.connect(self.delete)
        self.historyB.clicked.connect(self.history)
        self.alldel.clicked.connect(self.clear_history)

        # backgrounds
        self.num1.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.num2.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.num3.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.num4.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.num5.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.num6.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.num7.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.num8.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.num9.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.num0.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.deleteB.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.cE.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.divideN.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.multiN.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.minusN.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.plusN.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.themeB.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.equalsN.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.powerB.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.hundrN.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.opshower.setStyleSheet(
            "background-color: #C0C0C0;"
            "color: black;"
            "font-size: 25px;"
        )

        self.opshower.setFont(QFont("Helvetica"))

        self.historyB.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 25px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        self.historywidget.setStyleSheet(
            "background-color: #C0C0C0;"
            "font-size: 30px;"
            "font-weight: bold;"
            "border: 1px solid black;"
            "color: black;"
        )

        self.alldel.setStyleSheet(""" 
            QPushButton {
                background-color: #C0C0C0;
                font-size: 30px;
                border: 3px solid black;
            }
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: #BDBBD7;
            }
        """)

        # connections
        self.themeB.clicked.connect(self.setColor)

        self.answerB.display(0)
        self.answerB.setDigitCount(20)

        # self.answerB.display(123) displays the number inside the parentheses

    def press_number(self, number):

        if self.new_number_waiting:
            self.currentnumber = " "
            self.new_number_waiting = False

        self.currentnumber += number
        self.answerB.display(self.currentnumber)

    def press_operator(self, op):

        if self.currentnumber != " ":
            self.numberone = int(self.currentnumber)

        self.operator = op
        self.new_number_waiting = True

        self.opshower.setText(
            f"{self.numberone} {self.operator}"
        )

        self.answerB.display("0")

    def press_equals(self):

        if not self.operator or self.currentnumber == " ":
            return

        self.numbertwo = int(self.currentnumber)
        self.numberone = int(self.numberone)

        result = 0

        if self.operator == "+":
            result = self.numberone + self.numbertwo

        elif self.operator == "-":
            result = self.numberone - self.numbertwo

        elif self.operator == "*":
            result = self.numberone * self.numbertwo

        elif self.operator == "**":
            result = self.numberone ** self.numbertwo

        elif self.operator == "%":
            result = self.numberone * (self.numbertwo / 100)

        elif self.operator == "/":
            if self.numbertwo == 0:
                self.answerB.display("Error")
                self.clear()
                return

            result = self.numberone / self.numbertwo

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        self.opshower.setText(
            f"{self.numberone} {self.operator} {self.numbertwo} = "
        )

        self.answerB.display(result)
        self.currentnumber = str(result)

        history_result = (
            f"{self.numberone} {self.operator} "
            f"{self.numbertwo} = {result}"
        )

        self.operator = None
        self.new_number_waiting = True

        self.save(history_result)

    def clear(self):

        self.numberone = 0
        self.currentnumber = ""
        self.operator = None
        self.new_number_waiting = False

        self.answerB.display(0)

        self.opshower.setText("0")

        self.easteregg += 1

        if self.easteregg == 15:
            self.opshower.setText("Leave me alone vro")

    def delete(self):

        if len(self.currentnumber) > 0:
            self.currentnumber = self.currentnumber[:-1]

            if self.currentnumber == "":
                self.answerB.display(0)
            else:
                self.answerB.display(self.currentnumber)

    def history(self):

        if not self.history_open:
            self.historywidget.show()
            self.setGeometry(350, 250, 1000, 600)
            self.history_open = True

        else:
            self.historywidget.hide()
            self.setGeometry(700, 250, 500, 600)
            self.history_open = False

    def save(self, text):
        self.historywidget.addItem(text)

    def clear_history(self):
        self.historywidget.clear()

    def keyPressEvent(self, event):

        key = event.key()
        text = event.text()

        if key == Qt.Key_Escape:
            self.history()

        elif key == Qt.Key_Backspace:
            self.delete()

        elif key == Qt.Key_Delete:
            self.clear()

        elif key == Qt.Key_Return or key == Qt.Key_Enter:
            self.press_equals()

        elif text in "0123456789":
            self.press_number(text)

        elif text == "+":
            self.press_operator("+")

        elif text == "-":
            self.press_operator("-")

        elif text == "*":
            self.press_operator("*")

        elif text == "/":
            self.press_operator("/")

        elif text == "%":
            self.press_operator("%")

        elif text.lower() == "p":
            self.press_operator("**")

        elif text.lower() == "c":
            self.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
