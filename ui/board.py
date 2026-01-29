from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
from .theme import BG_COLOR, PRIMARY_COLOR, SECONDARY_COLOR, FONT, BTN_RADIUS
from game.logic import TicTacToe
from .components import GlassButton
import random

class BoardScreen(QWidget):
    def __init__(self, mode='friend', go_back_callback=None):
        super().__init__()
        self.mode = mode
        self.go_back_callback = go_back_callback
        self.game = TicTacToe()
        self.cells = [[None]*3 for _ in range(3)]
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet(f"background-color: {BG_COLOR};")
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel(f"بازیکن: {self.game.current_player}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size:24px; font-family: iranyekan;")
        layout.addWidget(self.label)

        grid = QGridLayout()
        for r in range(3):
            for c in range(3):
                btn = QPushButton("")
                btn.setFixedSize(100,100)
                btn.setStyleSheet(f"""
                    QPushButton {{
                        border-radius: {BTN_RADIUS}px;
                        background-color: white;
                        font-size: 36px;
                    }}
                    QPushButton:hover {{
                        background-color: #cccccc;
                    }}
                """)
                btn.clicked.connect(lambda _, row=r, col=c: self.click(row,col))
                grid.addWidget(btn, r, c)
                self.cells[r][c] = btn
        layout.addLayout(grid)
        self.setLayout(layout)

    def click(self,row,col):
        valid, winner = self.game.make_move(row,col)
        if valid:
            symbol = self.game.board[row][col]
            color = PRIMARY_COLOR if symbol=='X' else SECONDARY_COLOR
            self.cells[row][col].setText(symbol)
            self.cells[row][col].setStyleSheet(f"""
                QPushButton {{
                    border-radius: {BTN_RADIUS}px;
                    background-color: white;
                    font-size: 36px;
                    color: {color};
                }}
                QPushButton:hover {{
                    background-color: #f0f0f0;
                }}
            """)
            self.label.setText(f"بازیکن: {self.game.current_player}")
            if winner:
                self.show_winner(winner)
            elif self.mode=='ai' and self.game.current_player=='O' and not winner:
                self.ai_move()

    def ai_move(self):
        empty = [(r,c) for r in range(3) for c in range(3) if self.game.board[r][c]=='']
        if empty:
            row,col = random.choice(empty)
            valid,winner = self.game.make_move(row,col)
            if valid:
                symbol = self.game.board[row][col]
                color = PRIMARY_COLOR if symbol=='X' else SECONDARY_COLOR
                self.cells[row][col].setText(symbol)
                self.cells[row][col].setStyleSheet(f"""
                    QPushButton {{
                        border-radius: {BTN_RADIUS}px;
                        background-color: white;
                        font-size: 36px;
                        color: {color};
                    }}
                    QPushButton:hover {{
                        background-color: #f0f0f0;
                    }}
                """)
                self.label.setText(f"بازیکن: {self.game.current_player}")
                if winner:
                    self.show_winner(winner)

    def show_winner(self, winner):

        msg = "مساوی!" if winner == 'Draw' else f"بازیکن {winner} برنده شد!"
        QMessageBox.information(self, "پایان بازی", msg)


        for r in range(3):
            for c in range(3):
                self.cells[r][c].setEnabled(False)


        if not hasattr(self, "back_btn"):

            self.back_btn = GlassButton(
                "بازگشت به منو",
                callback=self.go_back_callback,
                color="#7D5FFF"
            )
            self.layout().addWidget(self.back_btn)

            self.retry_btn = GlassButton(
                "بازی مجدد",
                callback=self.reset_board,
                color="#00C48C"
            )
            self.layout().addWidget(self.retry_btn)

    def reset_board(self):

        self.game.reset()
        for r in range(3):
            for c in range(3):
                cell = self.cells[r][c]
                cell.setText("")
                cell.setEnabled(True)
                cell.setStyleSheet(f"""
                    QPushButton {{
                        border-radius: {BTN_RADIUS}px;
                        background-color: white;
                        font-size: 36px;
                        font-family: iranyekan;
                        color: black;
                    }}
                    QPushButton:hover {{
                        background-color: #f0f0f0;
                    }}
                """)

        if hasattr(self, "back_btn"):
            self.back_btn.setParent(None)
            del self.back_btn
        if hasattr(self, "retry_btn"):
            self.retry_btn.setParent(None)
            del self.retry_btn

        self.label.setText(f"بازیکن: {self.game.current_player}")

        
