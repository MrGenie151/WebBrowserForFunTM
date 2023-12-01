import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5 import QtGui
from PyQt5.QtWebEngineWidgets import QWebEngineView

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Genie's Stupid Browser")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QtGui.QIcon("genie_unimpressed.png"))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.browser = QWebEngineView()
        self.browser.urlChanged.connect(self.changeURL)
        self.browser.loadFinished.connect(self.load_finished)

        self.navigation_bar = QHBoxLayout()

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.go_button = QPushButton('Go')
        self.go_button.clicked.connect(self.navigate_to_url)

        #Navigation buttons
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)

        self.navigation_bar.addWidget(self.back_button)
        self.navigation_bar.addWidget(self.url_bar)
        self.navigation_bar.addWidget(self.go_button)

        self.layout.addLayout(self.navigation_bar)
        self.layout.addWidget(self.browser)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        qurl = QUrl(url)
        self.browser.setUrl(qurl)
    
    def go_back(self):
        self.browser.back()
    
    def changeURL(self):
        self.url_bar.setText(self.browser.url().toString())
    
    def load_finished(self):
        self.setWindowTitle(self.browser.page().title() + " - Genie's Stupid Browser")

def main():
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
