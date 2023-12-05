import socket
import install_pyqt


from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt

def show_banner():
    # Gets Server Name
    server_name = socket.gethostname()

    app = QApplication([])

    # Create overlay window
    window = QWidget()
    window.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
    window.setAttribute(Qt.WA_TranslucentBackground, True)

    # Set the window position and size
    window.setGeometry(0, 0, QApplication.desktop().screenGeometry().width(), 50)

    # Add a label with the banner text
    label = QLabel(window)
    label.setText(f"Server: {server_name}")
    label.setAlignment(Qt.AlignCenter)
    label.setStyleSheet("background-color: rgba(0, 0, 0, 0.7); color: white; font-size: 20px;")

    # Show the window
    window.show()

    # Run the event loop
    app.exec_()

try:
    show_banner()
except Exception as e:
    print(f"An error occurred: {e}")
