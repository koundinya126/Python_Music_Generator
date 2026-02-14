import sys
from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QApplication
)
from PyQt6.QtCore import Qt, pyqtSignal, QPropertyAnimation
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import QGraphicsOpacityEffect
from PyQt6.QtCore import QSequentialAnimationGroup, QPropertyAnimation

# Color constants
BG_COLOR = "#222222"
TEXT_COLOR = "#f0f0f0"
BUTTON_COLOR = "#444444"

class MusicApp_Welcome_Screen(QMainWindow):
    button_clicked = pyqtSignal(str)  # Signal to emit button clicks

    def __init__(self, project_name, logo_path=None):
        super().__init__()
        self.project_name = project_name
        self.logo_path = logo_path  # Path to your logo image
        self.init_ui()

    # ---------------- Init UI ----------------
    def init_ui(self):
        self.setWindowTitle("Python Music Tool")
        self.setGeometryToCenter()
        self.create_labels()
        self.create_buttons()
        self.create_layout()
        self.setCentralWidget(self.central_widget)
        self.start_animation()  # start fade-in animation

    # ---------------- Geometry ----------------
    def setGeometryToCenter(self):
        screen = self.screen().geometry()
        width = int(screen.width() * 0.6)
        height = int(screen.height() * 0.6)
        x = (screen.width() - width) // 2
        y = (screen.height() - height) // 2
        self.setGeometry(x, y, width, height)
        self.setStyleSheet(f"QMainWindow {{ background-color: {BG_COLOR}; }}")

    # ---------------- Labels ----------------
    def create_labels(self):
        screen_height = self.screen().geometry().height()

        # Logo (optional)
        self.logo_label = QLabel()
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if self.logo_path:
            pixmap = QPixmap(self.logo_path)
            # Scale logo to 20% of screen height
            pixmap = pixmap.scaledToHeight(int(screen_height * 0.2), Qt.TransformationMode.SmoothTransformation)
            self.logo_label.setPixmap(pixmap)

        # Main app name
        self.label_title = QLabel(self.project_name)
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font_title = QFont()
        font_title.setPointSize(int(screen_height * 0.04))
        font_title.setBold(True)
        self.label_title.setFont(font_title)
        self.label_title.setStyleSheet(f"color: {TEXT_COLOR}; background-color: transparent;")

        # Tagline
        self.label_tagline = QLabel("Vibe with your own melodies")
        self.label_tagline.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font_tagline = QFont()
        font_tagline.setPointSize(int(screen_height * 0.025))
        self.label_tagline.setFont(font_tagline)
        self.label_tagline.setStyleSheet(f"color: {TEXT_COLOR}; background-color: transparent;")

        # Add opacity effect for fade-in
        for lbl in [self.logo_label, self.label_title, self.label_tagline]:
            opacity = QGraphicsOpacityEffect()
            lbl.setGraphicsEffect(opacity)
            lbl.opacity_effect = opacity  # store reference
            opacity.setOpacity(0)  # start invisible

    # ---------------- Buttons ----------------
    def create_buttons(self):
        self.btn_start = QPushButton("Let's Create")
        self.btn_exit = QPushButton("Exit")

        for btn in [self.btn_start, self.btn_exit]:
            btn.setStyleSheet(
                f"""
                QPushButton {{
                    background-color: {BUTTON_COLOR};
                    color: {TEXT_COLOR};
                    padding: 10px 30px;
                    font-size: 12pt;
                    border-radius: 5px;
                    min-width: 120px;
                }}
                """
            )

        self.btn_start.clicked.connect(lambda: self.button_clicked.emit("start"))
        self.btn_exit.clicked.connect(sys.exit)

        # Opacity for buttons too
        for btn in [self.btn_start, self.btn_exit]:
            opacity = QGraphicsOpacityEffect()
            btn.setGraphicsEffect(opacity)
            btn.opacity_effect = opacity
            opacity.setOpacity(0)

    # ---------------- Layout ----------------
    def create_layout(self):
        self.central_widget = QWidget()
        main_layout = QVBoxLayout()

        main_layout.addStretch(2)
        if self.logo_path:
            main_layout.addWidget(self.logo_label)
            main_layout.addStretch(1)
        main_layout.addWidget(self.label_title)
        main_layout.addWidget(self.label_tagline)
        main_layout.addStretch(2)

        # Buttons layout
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.btn_start)
        button_layout.addSpacing(20)
        button_layout.addWidget(self.btn_exit)
        button_layout.addStretch(1)

        main_layout.addLayout(button_layout)
        main_layout.addStretch(1)

        self.central_widget.setLayout(main_layout)

    # ---------------- Animation ----------------
    def start_animation(self):
        duration = 750  # ms

        # List of widgets to animate
        widgets = []
        if self.logo_path:
            widgets.append(self.logo_label)
        widgets.extend([self.label_title, self.label_tagline, self.btn_start, self.btn_exit])

        # Sequential animation group
        self.anim_group = QSequentialAnimationGroup()

        for widget in widgets:
            anim = QPropertyAnimation(widget.opacity_effect, b"opacity")
            anim.setDuration(duration)
            anim.setStartValue(0)
            anim.setEndValue(1)
            self.anim_group.addAnimation(anim)  # add to group

        self.anim_group.start()

