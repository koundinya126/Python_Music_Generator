import sys
from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout,
    QApplication, QLineEdit, QFileDialog, QFrame, QScrollArea, QSizePolicy
)
from PyQt6.QtCore import Qt, pyqtSignal, QSize, QUrl
from PyQt6.QtGui import QIcon, QFont, QColor, QDesktopServices
from PyQt6.QtWidgets import QGraphicsDropShadowEffect

# Colors
BG_COLOR = "#222222"
TEXT_COLOR = "#f0f0f0"
BUTTON_COLOR = "#444444"
INPUT_BG_COLOR = "#333333"
ACCENT_COLOR = "#4A90E2"

class MusicApp_Create_Proj_Screen(QMainWindow):
    button_clicked = pyqtSignal(str)

    def __init__(self, project_name="VibeLab"):
        super().__init__()
        self.project_name = project_name
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(f"{self.project_name} - Create Project")
        self.setGeometryToCenter()
        self.create_labels()
        self.create_inputs()
        self.create_buttons()
        self.create_layout()
        self.setCentralWidget(self.central_widget)

    def setGeometryToCenter(self):
        screen = self.screen().geometry()
        width = int(screen.width() * 0.75)
        height = int(screen.height() * 0.65)
        x = (screen.width() - width) // 2
        y = (screen.height() - height) // 2
        self.setGeometry(x, y, width, height)
        self.setStyleSheet(f"QMainWindow {{ background-color: {BG_COLOR}; }}")

    # ---------------- Labels ----------------
    def create_labels(self):
        screen_height = self.screen().geometry().height()
        self.label_title = QLabel("Create New Project")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font_title = QFont()
        font_title.setPointSize(int(screen_height * 0.025))
        font_title.setBold(True)
        self.label_title.setFont(font_title)
        self.label_title.setStyleSheet(f"color: {TEXT_COLOR}; background-color: transparent;")

    # ---------------- Inputs ----------------
    def create_inputs(self):
        self.input_project_name = QLineEdit()
        self.input_project_name.setPlaceholderText("Enter project name")
        self.input_project_name.setStyleSheet(f"""
            QLineEdit {{
                background-color: {INPUT_BG_COLOR};
                color: {TEXT_COLOR};
                padding: 8px;
                border-radius: 8px;
            }}
        """)

        self.input_location = QLineEdit()
        self.input_location.setPlaceholderText("Select project location")
        self.input_location.setStyleSheet(f"""
            QLineEdit {{
                background-color: {INPUT_BG_COLOR};
                color: {TEXT_COLOR};
                padding: 8px;
                border-radius: 8px;
            }}
        """)

        self.btn_browse = QPushButton("Browse")
        self.btn_browse.setStyleSheet(f"""
            QPushButton {{
                background-color: {BUTTON_COLOR};
                color: {TEXT_COLOR};
                padding: 6px 20px;
                font-size: 11pt;
                border-radius: 8px;
            }}
            QPushButton:hover {{
                background-color: {ACCENT_COLOR};
                color: white;
            }}
        """)
        self.btn_browse.clicked.connect(self.browse_location)

    def browse_location(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Project Folder")
        if folder:
            self.input_location.setText(folder)
            print(f"Selected folder: {folder}")

    # ---------------- Buttons ----------------
    def create_buttons(self):
        # Main action buttons
        self.btn_new_project = QPushButton("New Project")
        self.btn_BACK = QPushButton("BACK")

        for btn in [self.btn_new_project, self.btn_BACK]:
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {BUTTON_COLOR};
                    color: {TEXT_COLOR};
                    padding: 10px 30px;
                    border-radius: 10px;
                    font-size: 12pt;
                }}
                QPushButton:hover {{
                    background-color: {ACCENT_COLOR};
                    color: white;
                }}
            """)

        self.btn_new_project.clicked.connect(lambda: print(
            f"New Project clicked | Name: {self.input_project_name.text()} | Location: {self.input_location.text()}"
        ))
        self.btn_BACK.clicked.connect(lambda: self.button_clicked.emit("BACK"))

        # Left bottom buttons (Help, YouTube, Instagram)
        self.btn_help = QPushButton("Help")
        self.btn_help.setIcon(QIcon("icons/help.png"))
        self.btn_help.setIconSize(QSize(18, 18))

        self.btn_youtube = QPushButton("YouTube")
        self.btn_youtube.setIcon(QIcon("icons/youtube.png"))
        self.btn_youtube.setIconSize(QSize(18, 18))

        self.btn_instagram = QPushButton("Instagram")
        self.btn_instagram.setIcon(QIcon("icons/instagram.png"))
        self.btn_instagram.setIconSize(QSize(18, 18))

        for btn in [self.btn_help, self.btn_youtube, self.btn_instagram]:
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {BUTTON_COLOR};
                    color: {TEXT_COLOR};
                    padding: 4px 10px;
                    border-radius: 8px;
                    font-size: 10pt;
                }}
                QPushButton:hover {{
                    background-color: {ACCENT_COLOR};
                    color: white;
                }}
            """)

        self.btn_help.clicked.connect(lambda: QDesktopServices.openUrl(
            QUrl("https://github.com/koundinya126/Python_Music_Generator/tree/main")
        ))
        self.btn_youtube.clicked.connect(lambda: print("YouTube clicked"))
        self.btn_instagram.clicked.connect(lambda: print("Instagram clicked"))

    # ---------------- Layout ----------------
    def create_layout(self):
        self.central_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(30)

        # -------- Left Panel --------
        left_frame = QFrame()
        left_frame.setFixedWidth(300)
        left_frame.setStyleSheet(f"""
            QFrame {{
                border: 2px solid #555555;
                border-radius: 10px;
                padding: 10px;
                background-color: {BG_COLOR};
            }}
        """)
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(10)

        # Recent projects title
        left_title = QLabel("Recent Projects")
        left_title.setStyleSheet(f"color: {TEXT_COLOR}; font-weight: bold;")
        left_layout.addWidget(left_title, alignment=Qt.AlignmentFlag.AlignLeft)

        # Scroll area for recent projects
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedHeight(int(self.height() * 0.7))  # 70% vertical
        scroll_area.setStyleSheet(f"QScrollArea {{ background-color: {BG_COLOR}; border: none; }}")

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout()
        scroll_layout.setSpacing(8)

        # Dummy projects
        for i in range(20):
            name = f"Project {i+1}"
            btn = QPushButton(name)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {BG_COLOR};
                    color: {TEXT_COLOR};
                    padding: 6px 15px;
                    border-radius: 6px;
                    text-align: left;
                }}
                QPushButton:hover {{
                    background-color: {ACCENT_COLOR};
                    color: white;
                }}
            """)
            btn.clicked.connect(lambda checked, n=name: print(f"Recent project clicked: {n}"))
            scroll_layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignLeft)

        scroll_layout.addStretch(1)
        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)

        left_layout.addWidget(scroll_area)

        # Bottom left buttons
        bottom_buttons_layout = QHBoxLayout()
        bottom_buttons_layout.addWidget(self.btn_help)
        bottom_buttons_layout.addWidget(self.btn_youtube)
        bottom_buttons_layout.addWidget(self.btn_instagram)
        bottom_buttons_layout.addStretch(1)
        left_layout.addLayout(bottom_buttons_layout)

        left_frame.setLayout(left_layout)
        main_layout.addWidget(left_frame, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # -------- Right Panel --------
        right_panel = QVBoxLayout()
        right_panel.addSpacing(30)  # Push down 30px from top
        right_panel.addWidget(self.label_title, alignment=Qt.AlignmentFlag.AlignCenter)
        right_panel.addSpacing(20)

        right_panel.addWidget(QLabel("Project Name:"), alignment=Qt.AlignmentFlag.AlignLeft)
        right_panel.addWidget(self.input_project_name)
        right_panel.addSpacing(10)

        right_panel.addWidget(QLabel("Project Location:"), alignment=Qt.AlignmentFlag.AlignLeft)
        loc_layout = QHBoxLayout()
        loc_layout.addWidget(self.input_location)
        loc_layout.addWidget(self.btn_browse)
        right_panel.addLayout(loc_layout)
        right_panel.addSpacing(30)

        # New Project and Back side by side
        btns_layout = QHBoxLayout()
        btns_layout.addStretch(1)
        btns_layout.addWidget(self.btn_new_project)
        btns_layout.addWidget(self.btn_BACK)
        btns_layout.addStretch(1)
        right_panel.addLayout(btns_layout)
        right_panel.addStretch(1)

        main_layout.addLayout(right_panel, 1)
        self.central_widget.setLayout(main_layout)

# ---------------- Run ----------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicApp_Create_Proj_Screen()
    window.show()
    sys.exit(app.exec())
