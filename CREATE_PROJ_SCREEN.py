import sys
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QGridLayout
from PyQt6.QtCore import Qt, pyqtSignal, QObject
from PyQt6.QtGui import QFont

# Color constants
BG_COLOR = "#222222"
TEXT_COLOR = "#f0f0f0"

class MusicApp_Create_Proj_Screen(QMainWindow):
    button_clicked = pyqtSignal(str)  # Signal to emit button click
    
    def __init__(self):
        super().__init__()
        self.init_ui()

    def Create_Project_Title(self):
        
        self.project_label = QLabel("Create New Project")
        self.project_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.project_label.setStyleSheet(f"QLabel {{ color: {TEXT_COLOR}; background-color: transparent; }}")
        
        screen = self.screen().geometry()
        font_size = int(screen.height() * 0.02)
        font = QFont()
        font.setPointSize(font_size)
        self.project_label.setFont(font)

    def Create_Project_Inputs(self):
        # Project Name
        self.proj_name_label = QLabel("Project Name:")
        self.proj_name_label.setStyleSheet(f"QLabel {{ color: {TEXT_COLOR}; background-color: transparent; }}")
        
        self.proj_name_input = QLineEdit()
        self.proj_name_input.setStyleSheet(f"QLineEdit {{ background-color: #444444; color: {TEXT_COLOR}; padding: 8px; border-radius: 3px; }}")
        self.proj_name_input.setMinimumWidth(300)
        
        # Location
        self.location_label = QLabel("Location:")
        self.location_label.setStyleSheet(f"QLabel {{ color: {TEXT_COLOR}; background-color: transparent; }}")
        
        self.location_input = QLineEdit()
        self.location_input.setStyleSheet(f"QLineEdit {{ background-color: #444444; color: {TEXT_COLOR}; padding: 8px; border-radius: 3px; }}")
        self.location_input.setMinimumWidth(300)
        
        self.browse_btn = QPushButton("Browse")
        self.browse_btn.clicked.connect(self.on_browse_clicked)
        self.browse_btn.setStyleSheet(f"QPushButton {{ background-color: #555555; color: {TEXT_COLOR}; padding: 8px 15px; font-size: 10pt; border-radius: 3px; }}")

    def Create_Project_Buttons(self):
        self.btn_create = QPushButton("Create Project")
        self.btn_create.clicked.connect(self.on_create_clicked)
        self.btn_create.setStyleSheet(f"QPushButton {{ background-color: #444444; color: {TEXT_COLOR}; padding: 10px 30px; font-size: 12pt; border-radius: 5px; min-width: 100px; }}")
        self.btn_create.setMinimumWidth(120)
        
        self.btn_BACK = QPushButton("BACK")
        self.btn_BACK.clicked.connect(self.on_BACK_clicked)
        self.btn_BACK.setStyleSheet(f"QPushButton {{ background-color: #444444; color: {TEXT_COLOR}; padding: 10px 30px; font-size: 12pt; border-radius: 5px; min-width: 100px; }}")
        self.btn_BACK.setMinimumWidth(120)

    def Create_Project_Layout(self):
        self.layout = QVBoxLayout()
        
        # Add title
        self.layout.addWidget(self.project_label)
        self.layout.addSpacing(20)
        
        # Use Grid Layout for aligned labels and inputs
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)
        
        # Add Project Name - Row 0
        grid_layout.addWidget(self.proj_name_label, 0, 0, alignment=Qt.AlignmentFlag.AlignRight)
        grid_layout.addWidget(self.proj_name_input, 0, 1)
        
        # Add Location - Row 1
        grid_layout.addWidget(self.location_label, 1, 0, alignment=Qt.AlignmentFlag.AlignRight)
        grid_layout.addWidget(self.location_input, 1, 1)
        grid_layout.addWidget(self.browse_btn, 1, 2)
        
        # Center the grid layout
        center_layout = QHBoxLayout()
        center_layout.addStretch()
        center_layout.addLayout(grid_layout)
        center_layout.addStretch()
        
        self.layout.addLayout(center_layout)
        
        self.layout.addSpacing(20)
        
        # Add buttons - centered
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.btn_create)
        button_layout.addWidget(self.btn_BACK)
        button_layout.addStretch()
        self.layout.addLayout(button_layout)
        
        self.layout.addSpacing(10)

    def Create_Project_Screen(self):
        self.Create_Project_Title()
        self.Create_Project_Inputs()
        self.Create_Project_Buttons()
        self.Create_Project_Layout()
        
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        
        return central_widget
    
    def on_browse_clicked(self):
        print("Browse button clicked")
    
    def on_create_clicked(self):
        print("Create Project button clicked")
        self.button_clicked.emit("create")
    
    def on_BACK_clicked(self):
        self.button_clicked.emit("BACK")

    def init_ui(self):
        self.setWindowTitle("Python Music Tool")
        self.setStyleSheet(f"QMainWindow {{ background-color: {BG_COLOR}; }}")
        
        central_widget = self.Create_Project_Screen()
        self.setCentralWidget(central_widget)

