#imports
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont


class Stopwatch(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowTitle("Stopwatch")
        self.setGeometry(300, 200, 500, 250)

        # Store elapsed time in milliseconds
        self.elapsed_ms = 0

        # Create a timer object
        self.timer = QTimer(self)

        # Every timeout signal calls update_time()
        self.timer.timeout.connect(self.update_time)

        # Label to display the stopwatch time
        self.label = QLabel("00:00:00.000", self)
        self.label.setGeometry(50, 30, 400, 70)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 24))

        # Start button
        self.start_button = QPushButton("Start", self)
        self.start_button.setGeometry(50, 150, 100, 40)
        self.start_button.clicked.connect(self.start_timer)

        # Stop button
        self.stop_button = QPushButton("Stop", self)
        self.stop_button.setGeometry(200, 150, 100, 40)
        self.stop_button.clicked.connect(self.stop_timer)

        # Reset button
        self.reset_button = QPushButton("Reset", self)
        self.reset_button.setGeometry(350, 150, 100, 40)
        self.reset_button.clicked.connect(self.reset_timer)

    def start_timer(self):
        # Start timer and trigger every 10 milliseconds
        self.timer.start(10)

    def stop_timer(self):
        # Stop the timer
        self.timer.stop()

    def reset_timer(self):
        # Stop timer and reset elapsed time
        self.timer.stop()
        self.elapsed_ms = 0

        # Reset label text
        self.label.setText("00:00:00.000")

    def update_time(self):
        # Increase elapsed time by 10 ms
        self.elapsed_ms += 10

        # Convert milliseconds into hours, minutes, seconds, milliseconds
        hours = self.elapsed_ms // 3600000

        minutes = (self.elapsed_ms % 3600000) // 60000

        seconds = (self.elapsed_ms % 60000) // 1000

        milliseconds = self.elapsed_ms % 1000

        # Display time in HH:MM:SS.mmm format
        self.label.setText(
            f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"
        )


def main():
    # Create the application
    app = QApplication(sys.argv)

    # Create the main window
    window = Stopwatch()

    # Show the window
    window.show()

    # Start the event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()