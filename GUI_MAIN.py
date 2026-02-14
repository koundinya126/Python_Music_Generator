import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt

# Color constants
BG_COLOR = "#222222"
TEXT_COLOR = "#f0f0f0"

class MusicApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Python Music Tool")
        self.setGeometry(100, 100, 800, 500)
        
        self.label = QLabel("Welcome to Sound → BGM Tool", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.setStyleSheet(f"QMainWindow {{ background-color: {BG_COLOR}; }}")
        self.label.setStyleSheet(f"QLabel {{ color: {TEXT_COLOR}; }}")
        
        self.setCentralWidget(self.label)

def main():
    app = QApplication(sys.argv)
    window = MusicApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()