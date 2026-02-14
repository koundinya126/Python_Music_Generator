import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.QtCore import pyqtSignal, QObject
from WELCOME_SCREEN import MusicApp_Welcome_Screen
from CREATE_PROJ_SCREEN import MusicApp_Create_Proj_Screen  


class AppManager(QMainWindow):
    def __init__(self, PROJECT_NAME):
        super().__init__()
        self.PROJECT_NAME = PROJECT_NAME
        self.setWindowTitle(f"{PROJECT_NAME}")
        
        # Set window geometry to 60% of screen size, centered
        screen = self.screen().geometry()
        width = int(screen.width() * 0.6)
        height = int(screen.height() * 0.6)
        x = int((screen.width() - width) / 2)
        y = int((screen.height() - height) / 2)
        self.setGeometry(x, y, width, height)
        
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        self.welcome_screen = MusicApp_Welcome_Screen(self.PROJECT_NAME)
        self.welcome_screen.button_clicked.connect(self.Create_button_clicked)
        
        self.stacked_widget.addWidget(self.welcome_screen)
        self.stacked_widget.setCurrentIndex(0)
        
        self.create_proj_screen = None
    
    def Create_button_clicked(self, button_name):
        if button_name == "start":
            if self.create_proj_screen is None:
                self.create_proj_screen = MusicApp_Create_Proj_Screen()
                self.create_proj_screen.button_clicked.connect(self.Second_Screen_Cancel_Button_clicked)
                self.stacked_widget.addWidget(self.create_proj_screen)
            self.stacked_widget.setCurrentWidget(self.create_proj_screen)

    def Second_Screen_Cancel_Button_clicked(self, button_name):
        if button_name == "BACK":
            self.welcome_screen = MusicApp_Welcome_Screen(self.PROJECT_NAME)
            self.welcome_screen.button_clicked.connect(self.Create_button_clicked)
        
            self.stacked_widget.addWidget(self.welcome_screen)
            self.stacked_widget.setCurrentIndex(0)

            self.create_proj_screen = None
            self.stacked_widget.setCurrentWidget(self.welcome_screen)
    
    def run(self):
        return self.app.exec()

def main(PROJECT_NAME):
    app = QApplication(sys.argv)
    manager = AppManager(PROJECT_NAME)
    manager.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()