from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from .components import GlassButton
from .theme import BG_COLOR

class MenuScreen(QWidget):
    def __init__(self, start_callback):
        super().__init__()
        self.start_callback = start_callback
        self.setStyleSheet(f"background-color: {BG_COLOR};")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("⭕بازی دوز❌")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:40px; font-family:doran; font-weight:bold;")
        layout.addWidget(title)

        subtitle = QLabel("به سبک مسعود!")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("font-size: 18px; font-family:doran; color: gray;")
        layout.addWidget(subtitle)
        layout.addSpacing(50)
        
        btn_friend = GlassButton("بازی با دوست", lambda: self.start_callback('friend'))
        layout.addWidget(btn_friend)
        layout.addSpacing(20)

        btn_ai = GlassButton("بازی با ربات", lambda: self.start_callback('ai'), color="#00C48C")
        layout.addWidget(btn_ai)

        self.setLayout(layout)
