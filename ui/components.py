from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt

class GlassButton(QPushButton):
    def __init__(self, text, callback=None, color="#7D5FFF"):
        super().__init__(text)
        self.callback = callback
        self.color = color
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.color};
                color: white;
                border-radius: 20px;
                padding: 15px;
                font-size: 20px;
                font-family: iranyekan;
            }}
            QPushButton:hover {{
                background-color: #A080FF;
            }}
            QPushButton:pressed {{
                background-color: #5E3FFF;
            }}
        """)
        if self.callback:
            self.clicked.connect(self.callback)
