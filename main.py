import sys
from PyQt6.QtWidgets import QApplication, QWidget, QStackedLayout
from ui.menu import MenuScreen
from ui.board import BoardScreen

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("⭕بازی دوز❌")
        self.setFixedSize(500,700)
        self.stack = QStackedLayout()
        self.setLayout(self.stack)

        self.menu = MenuScreen(self.start_game)
        self.stack.addWidget(self.menu)

    def start_game(self, mode):
        self.board = BoardScreen(mode=mode, go_back_callback=self.go_back_to_menu)
        self.stack.addWidget(self.board)
        self.stack.setCurrentWidget(self.board)

    def go_back_to_menu(self):
        self.stack.setCurrentWidget(self.menu)

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
