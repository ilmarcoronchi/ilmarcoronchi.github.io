# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# pip install pyqt5
# pip install pyqtwebengine


# Importa tutte le classi per costruire GUI con Qt

from PyQt5.QtWidgets import *


def init():
    # verifica se l'applicazione è già esistente
    app = QApplication.instance()
    if not app: app = QApplication([])
    window = QWidget()
    window.resize(500, 300)
    window.setWindowTitle('LS Mapelli')
    return app, window


def run(app, window):
    window.show()
    app.exec_()


# Definisce la callback del bottone
def btn_exit_onclick():
    print('Clicked Exit Button')


def btn_print_onclick():
    print('Clicked Print Button')


# CALL to init()
app, window = init()  # Crea un bottone sulla finestra

layout = QVBoxLayout()  # Crea un layout verticale
# Crea due bottoni
btn_exit = QPushButton('Exit')
btn_print = QPushButton('Print')
# Aggiunge i bottoni al layout
layout.addWidget(btn_print)
layout.addWidget(btn_exit)

window.setLayout(layout)  # Imposta il layout come layout della finestra

# Imposta le callback in risposta all'evento clicked dei bottons
btn_print.clicked.connect(btn_print_onclick)
btn_exit.clicked.connect(btn_exit_onclick)

# CALL to run()
run(app, window)
