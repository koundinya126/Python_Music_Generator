import sys
from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout,
    QApplication, QLineEdit, QFileDialog, QFrame, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont

# Colors
BG_COLOR = "#222222"
TEXT_COLOR = "#f0f0f0"
BUTTON_COLOR = "#444444"
INPUT_BG_COLOR = "#333333"

class MusicApp_Create_Proj_Screen(QMainWindow):
    button_clicked = pyqtSignal(str)

    def __init__(self, project_name="VibeLab"):
        super().__init__()
        self.project_name = project_name
        self.init_ui()

    # ---------------- Init ----------------
    def init_ui(self):
        self.setWindowTitle(f"{self.project_name} - Create Project")
        self.setGeometryToCenter()
        self.create_labels()
        self.create_inputs()
        self.create_buttons()
        self.create_layout()
        self.setCentralWidget(self.central_widget)

    # ---------------- Geometry ----------------
    def setGeometryToCenter(self):
        screen = self.screen().geometry()
        width = int(screen.width() * 0.7)
        height = int(screen.height() * 0.6)
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
        font_title.setPointSize(int(screen_height * 0.035))
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
                border-radius: 5px;
            }}
        """)

        self.input_location = QLineEdit()
        self.input_location.setPlaceholderText("Select project location")
        self.input_location.setStyleSheet(f"""
            QLineEdit {{
                background-color: {INPUT_BG_COLOR};
                color: {TEXT_COLOR};
                padding: 8px;
                border-radius: 5px;
            }}
        """)

        self.btn_browse = QPushButton("Browse")
        self.btn_browse.setStyleSheet(f"""
            QPushButton {{
                background-color: {BUTTON_COLOR};
                color: {TEXT_COLOR};
                padding: 6px 20px;
                font-size: 11pt;
                border-radius: 5px;
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
        self.btn_new_project = QPushButton("New Project")
        self.btn_BACK = QPushButton("BACK")

        for btn in [self.btn_new_project, self.btn_BACK]:
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {BUTTON_COLOR};
                    color: {TEXT_COLOR};
                    padding: 10px 30px;
                    font-size: 12pt;
                    border-radius: 5px;
                    min-width: 180px;
                }}
            """)

        self.btn_new_project.clicked.connect(lambda: print(
            f"New Project clicked | Name: {self.input_project_name.text()} | Location: {self.input_location.text()}"
        ))
        self.btn_BACK.clicked.connect(lambda: self.button_clicked.emit("BACK"))

    # ---------------- Layout ----------------
    def create_layout(self):
        self.central_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # -------- Left Panel: Recent Projects --------
        left_panel = QFrame()
        left_panel.setFixedWidth(250)  # approx 50% of small width
        left_panel.setStyleSheet(f"""
            QFrame {{
                border: 2px solid #555555;
                border-radius: 5px;
                padding: 10px;
                background-color: {BG_COLOR};
            }}
        """)
        left_layout = QVBoxLayout()
        left_layout.setSpacing(10)

        left_title = QLabel("Recent Projects")
        left_title.setStyleSheet(f"color: {TEXT_COLOR}; font-weight: bold;")
        left_layout.addWidget(left_title, alignment=Qt.AlignmentFlag.AlignLeft)

        dummy_projects = ["Project Alpha", "Project Beta", "Project Gamma"]
        for p in dummy_projects:
            btn = QPushButton(p)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {BG_COLOR};
                    color: {TEXT_COLOR};
                    padding: 6px 10px;
                    border-radius: 5px;
                    text-align: left;
                }}
            """)
            btn.clicked.connect(lambda checked, name=p: print(f"Recent project clicked: {name}"))
            left_layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignLeft)

        # add spacer to control vertical height (10% - 50% of window)
        left_layout.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        left_panel.setLayout(left_layout)
        main_layout.addWidget(left_panel, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # -------- Right Panel: Create Project Form --------
        right_panel = QVBoxLayout()
        right_panel.addWidget(self.label_title)
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
        right_panel.addWidget(self.btn_new_project, alignment=Qt.AlignmentFlag.AlignCenter)
        right_panel.addWidget(self.btn_BACK, alignment=Qt.AlignmentFlag.AlignCenter)
        right_panel.addStretch(1)  # full vertical expansion

        main_layout.addLayout(right_panel, 1)  # right panel fills remaining width

        self.central_widget.setLayout(main_layout)


# ---------------- Run ----------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicApp_Create_Proj_Screen()
    window.show()
    sys.exit(app.exec())
