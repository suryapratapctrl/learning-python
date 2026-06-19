# imports
import sys  # this module provides access to some variables used or maintained by the interpreter
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry(
            0, 0, 500, 500
        )  # first two number sets the coordinate of top left conor and next two number sets the height and weidth of the window
        self.setWindowIcon(QIcon("icon.jpeg"))  # to set the icon for the window
        label = QLabel("hiiiiiii", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet(
            "color:#292929;"
            "background-color:blue;"
            "font-weight:bold;"
            "font-style: italic;"
            "text-decoration: underline;"
        )

        label.setAlignment(Qt.AlignTop)  # vertically top
        #label.setAlignment(Qt.AlignBottom)  # vertically bottom
        #label.setAlignment(Qt.AlignVCenter)  # vertically center
        #label.setAlignment(Qt.AlignRight)  # horizontally right
        #label.setAlignment(Qt.AlignLeft)  # horizontally left


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
