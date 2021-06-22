# pip install pyqt5
# pip install pyqtwebengine


# Importa tutte le classi per costruire GUI con Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


# Crea un'applicazione Qt
app = QApplication([])
# Crea una finestra (ma non e' visibile)
window = QWidget()
# Imposta dimensione e titolo della finestra
window.resize(500, 300)
window.setWindowTitle('Fondamenti di Programmazione')
# Mostra la finestra
window.show()
# Lancia l'interazione con l'utente
app.exec_()
# Out: 0



