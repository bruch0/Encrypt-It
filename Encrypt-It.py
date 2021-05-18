# Importing libraries
import sys
import pyperclip
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout, QTextEdit, QMessageBox
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtCore
import webbrowser

# Declaring variables
widgets = {
    "logo": [],
    "slogo": [],
    "buttonfen": [],
    "buttonfde": [],
    "buttonfab": [],
    "buttonnext": [],
    "buttonback": [],
    "textbox": [],
    "buttonen": [],
    "buttonde": [],
    "buttongit": []
}
alphabet = ['j', 'Á', 'W', 'J', 'E', 'P', 'u', '^', 'k', 'â', 't', 'ì', 's', 'a', 'ê', '>', 'F', 'Z',
            'I', 'y', '[', 'Y', 'l', 'ñ', 'S', 'f', 'ó', 'o', 'Ê', 'h', '6', 'r', '%', '+', 'Û', 'X',
            'È', 'A', 'í', '/', 'c', 'Ô', '0', 'H', 'Ú', 'i', 'ù', '5', '=', 'g', ';', '$', 'e', 'T',
            'O', 'û', 'R', '!', '~', 'Ó', 'C', '(', 'U', 'ô', '{', '&', 'á', 'Ñ', 'Ã', '4', '}', '9',
            '#', '<', 'K', 'd', '1', 'L', 'w', 'n', 'À', 'Í', '|', 'm', '-', '2', ')', 'N', 'î', 'É',
            'b', 'Ò', '7', '8', 'Î', 'q', 'G', 'Ù', 'z', ',', 'à', '*', 'ò', 'Â', 'è', 'Ì', 'V', 'ã',
            '3', 'ú', ':', 'x', 'D', '?', 'é', '"', 'B', '@', '.', '`', 'p', ']', 'Q', 'v', '_', 'M']
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Encrypt-It")
window.setFixedWidth(1000)
window.setFixedHeight(500)
window.setStyleSheet("background-color: #161219;")
grid = QGridLayout()
window.setLayout(grid)


# Defining encrypting and decrypting functions
def encryptfunction(texto):
    global crypt
    global cont
    crypt = ''
    cont = 0
    for i in range(0, len(texto)):
        for j in range(0, len(alphabet)):
            cont += 1
            if texto[i] == alphabet[j]:
                if j + 3 >= len(alphabet):
                    crypt += alphabet[j - 26 + 3]
                    cont = 0
                else:
                    crypt += alphabet[j + 3]
                    cont = 0
            if cont == 125:
                crypt += ' '
                cont = 0
        cont = 0
    return crypt


def decryptfunction(texto):
    global decrypt
    global cont
    decrypt = ''
    cont = 0
    for i in range(0, len(texto)):
        for j in range(0, len(alphabet)):
            cont += 1
            if texto[i] == alphabet[j]:
                if j + 3 >= len(alphabet):
                    decrypt += alphabet[j - 26 - 3]
                    cont = 0
                else:
                    decrypt += alphabet[j - 3]
                    cont = 0
            if cont == 125:
                decrypt += ' '
                cont = 0
        cont = 0
    return decrypt


# Functions to make the program actually work
# Function to clear all widgets
def ClearWidgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

# Function to call 'How to use' screen
def CallAB():
    ClearWidgets()
    HowToUseFrame1()

# Function to call 'Encrypt' screen
def CallEn():
    ClearWidgets()
    EncryptFrame()

# Function to call 'Decrypt' screen
def CallDe():
    ClearWidgets()
    DecryptFrame()

# Function to call 'Initial' screen
def CallIn():
    ClearWidgets()
    InicialFrame()

# Function to update constantly the content of the encrypt textbox and copy to the user
def updateencrypt(document):
    text = document.toPlainText()
    x = encryptfunction(text)
    pyperclip.copy(x)

# Function to update constantly the content of the decrypt textbox and copy to the user
def updatedecrypt(document):
    text = document.toPlainText()
    x = decryptfunction(text)
    pyperclip.copy(x)

# Functions to tell the user that his content is copied
def messageen():
    msg = QMessageBox()
    msg.setWindowTitle("Encrypted!")
    msg.setText("Your text is encrypted and copied in your Ctrl + C")

    x = msg.exec_()

def messagede():
    msg = QMessageBox()
    msg.setWindowTitle("Decrypted!")
    msg.setText("Your text is decrypted and copied in your Ctrl + C")

    x = msg.exec_()

# Function to make a button lead to my GitHub account
def Git():
    webbrowser.open('https://github.com/bruch0')

# Defining Functions for Frames
def InicialFrame():
    # Display logo
    image = QPixmap("logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 0px;")
    widgets["logo"].append(logo)

    # Button encrypt
    buttonfen = QPushButton("ENCRYPT")
    buttonfen.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    buttonfen.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 0;" +
        "margin: 5px 200px;"
    )

    # Button decrypt
    buttonfde = QPushButton("DECRYPT")
    buttonfde.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    buttonfde.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 0;" +
        "margin: 5px 200px;"
    )

    # Button about
    buttonab = QPushButton("HOW TO USE")
    buttonab.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    buttonab.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 0px;" +
        "margin: 5px 200px;"
    )
    widgets["buttonfen"].append(buttonfen)
    widgets["buttonfde"].append(buttonfde)
    widgets["buttonfab"].append(buttonab)

    grid.addWidget(widgets["logo"][-1], 0, 0)
    grid.addWidget(widgets["buttonfen"][-1], 1, 0)
    grid.addWidget(widgets["buttonfde"][-1], 2, 0)
    grid.addWidget(widgets["buttonfab"][-1], 3, 0)
    buttonfen.clicked.connect(CallEn)
    buttonfde.clicked.connect(CallDe)
    buttonab.clicked.connect(CallAB)


def EncryptFrame():
    # Display bottom logo
    simage = QPixmap("enclogo.png")
    slogo = QLabel()
    slogo.setPixmap(simage)
    slogo.setAlignment(QtCore.Qt.AlignCenter)
    slogo.setStyleSheet("margin-top: 0px;")
    widgets["slogo"].append(slogo)

    # Display user input area
    textbox = QTextEdit()
    textbox.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "margin: 5px 200px;"
    )
    widgets["textbox"].append(textbox)

    # Button Encrypt
    buttonen = QPushButton("ENCRYPT!")
    buttonen.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    buttonen.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 0px;" +
        "margin: 5px 200px;"
    )
    widgets["buttonen"].append(buttonen)

    # Button back
    buttonback = QPushButton("BACK")
    buttonback.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    buttonback.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 0px;" +
        "margin: 5px 200px;"
    )
    widgets["buttonback"].append(buttonback)

    document = textbox.document()
    document.contentsChange.connect(lambda: updateencrypt(document))

    grid.addWidget(widgets["slogo"][-1], 0, 0)
    grid.addWidget(widgets["textbox"][-1], 1, 0)
    grid.addWidget(widgets["buttonen"][-1], 2, 0)
    grid.addWidget(widgets["buttonback"][-1], 3, 0)
    buttonen.clicked.connect(lambda: updateencrypt(document))
    buttonen.clicked.connect(messageen)
    buttonback.clicked.connect(CallIn)


def DecryptFrame():
    # Display bottom logo
    simage = QPixmap("declogo.png")
    slogo = QLabel()
    slogo.setPixmap(simage)
    slogo.setAlignment(QtCore.Qt.AlignCenter)
    slogo.setStyleSheet("margin-top: 0px;")
    widgets["slogo"].append(slogo)

    # Display user input area
    textbox = QTextEdit()
    textbox.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "margin: 5px 200px;"
    )
    widgets["textbox"].append(textbox)

    # Button Encrypt
    buttonde = QPushButton("DECRYPT!")
    buttonde.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    buttonde.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 0px;" +
        "margin: 5px 200px;"
    )
    widgets["buttonde"].append(buttonde)

    # Button back
    buttonback = QPushButton("BACK")
    buttonback.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    buttonback.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 0px;" +
        "margin: 5px 200px;"
    )
    widgets["buttonback"].append(buttonback)

    document2 = textbox.document()

    document2.contentsChange.connect(lambda: updatedecrypt(document2))

    grid.addWidget(widgets["slogo"][-1], 0, 0)
    grid.addWidget(widgets["textbox"][-1], 1, 0)
    grid.addWidget(widgets["buttonde"][-1], 2, 0)
    grid.addWidget(widgets["buttonback"][-1], 3, 0)
    buttonde.clicked.connect(lambda: updatedecrypt(document2))
    buttonde.clicked.connect(messagede)
    buttonback.clicked.connect(CallIn)


def HowToUseFrame1():
    # Display bottom logo
    simage = QPixmap("howtouse1.png")
    slogo = QLabel()
    slogo.setPixmap(simage)
    slogo.setAlignment(QtCore.Qt.AlignCenter)
    slogo.setStyleSheet("margin-top: 0px;")
    widgets["slogo"].append(slogo)

    # Button next
    buttonnext = QPushButton("NEXT")
    buttonnext.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    buttonnext.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 0px;" +
        "margin: 5px 200px;"
    )
    widgets["buttonnext"].append(buttonnext)

    # Button back
    buttonback = QPushButton("BACK")
    buttonback.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    buttonback.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 0px;" +
        "margin: 5px 200px;"
    )
    widgets["buttonback"].append(buttonback)

    grid.addWidget(widgets["slogo"][-1], 0, 0)
    grid.addWidget(widgets["buttonnext"][-1], 1, 0)
    grid.addWidget(widgets["buttonback"][-1], 2, 0)
    buttonnext.clicked.connect(ClearWidgets)
    buttonnext.clicked.connect(HowToUseFrame2)
    buttonback.clicked.connect(CallIn)


def HowToUseFrame2():
    # Display bottom logo
    simage = QPixmap("howtouse2.png")
    slogo = QLabel()
    slogo.setPixmap(simage)
    slogo.setAlignment(QtCore.Qt.AlignCenter)
    slogo.setStyleSheet("margin-top: 0px;")
    widgets["slogo"].append(slogo)

    # Button next
    buttonnext = QPushButton("NEXT")
    buttonnext.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    buttonnext.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 0px;" +
        "margin: 5px 200px;"
    )
    widgets["buttonnext"].append(buttonnext)

    # Button back
    buttonback = QPushButton("BACK")
    buttonback.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    buttonback.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 0px;" +
        "margin: 5px 200px;"
    )
    widgets["buttonback"].append(buttonback)

    grid.addWidget(widgets["slogo"][-1], 0, 0)
    grid.addWidget(widgets["buttonnext"][-1], 1, 0)
    grid.addWidget(widgets["buttonback"][-1], 2, 0)
    buttonnext.clicked.connect(ClearWidgets)
    buttonnext.clicked.connect(HowToUseFrame3)
    buttonback.clicked.connect(ClearWidgets)
    buttonback.clicked.connect(HowToUseFrame1)


def HowToUseFrame3():
    # Display bottom logo
    simage = QPixmap("howtouse3.png")
    slogo = QLabel()
    slogo.setPixmap(simage)
    slogo.setAlignment(QtCore.Qt.AlignCenter)
    slogo.setStyleSheet("margin-top: 0px;")
    widgets["slogo"].append(slogo)

    # Button next
    buttonnext = QPushButton("NEXT")
    buttonnext.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    buttonnext.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 0px;" +
        "margin: 5px 200px;"
    )
    widgets["buttonnext"].append(buttonnext)

    # Button back
    buttonback = QPushButton("BACK")
    buttonback.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    buttonback.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 0px;" +
        "margin: 5px 200px;"
    )
    widgets["buttonback"].append(buttonback)

    grid.addWidget(widgets["slogo"][-1], 0, 0)
    grid.addWidget(widgets["buttonnext"][-1], 1, 0)
    grid.addWidget(widgets["buttonback"][-1], 2, 0)
    buttonnext.clicked.connect(ClearWidgets)
    buttonnext.clicked.connect(HowToUseFrame4)
    buttonback.clicked.connect(ClearWidgets)
    buttonback.clicked.connect(HowToUseFrame2)


def HowToUseFrame4():
    # Display bottom logo
    simage = QPixmap("howtouse4.png")
    slogo = QLabel()
    slogo.setPixmap(simage)
    slogo.setAlignment(QtCore.Qt.AlignCenter)
    slogo.setStyleSheet("margin-top: 0px;")
    widgets["slogo"].append(slogo)

    # Button next
    buttonnext = QPushButton("NEXT")
    buttonnext.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    buttonnext.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 0px;" +
        "margin: 5px 200px;"
    )
    widgets["buttonnext"].append(buttonnext)

    # Button back
    buttonback = QPushButton("BACK")
    buttonback.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    buttonback.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 0px;" +
        "margin: 5px 200px;"
    )
    widgets["buttonback"].append(buttonback)

    grid.addWidget(widgets["slogo"][-1], 0, 0)
    grid.addWidget(widgets["buttonnext"][-1], 1, 0)
    grid.addWidget(widgets["buttonback"][-1], 2, 0)
    buttonnext.clicked.connect(ClearWidgets)
    buttonnext.clicked.connect(HowToUseFrame5)
    buttonback.clicked.connect(ClearWidgets)
    buttonback.clicked.connect(HowToUseFrame3)


def HowToUseFrame5():
    # Display bottom logo
    simage = QPixmap("howtouse5.png")
    slogo = QLabel()
    slogo.setPixmap(simage)
    slogo.setAlignment(QtCore.Qt.AlignCenter)
    slogo.setStyleSheet("margin-top: 0px;")
    widgets["slogo"].append(slogo)

    # GitHub account button
    buttongit = QPushButton("MY GITHUB ACCOUNT")
    buttongit.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    buttongit.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 0px;" +
        "margin: 5px 200px;"
    )
    widgets["buttongit"].append(buttongit)

    # Button back
    buttonback = QPushButton("BACK")
    buttonback.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    buttonback.setStyleSheet(
        "border: 4px solid '#8A2BE2';" +
        "border-radius: 5px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 0px;" +
        "margin: 5px 200px;"
    )
    widgets["buttonback"].append(buttonback)

    grid.addWidget(widgets["slogo"][-1], 0, 0)
    grid.addWidget(widgets["buttongit"][-1], 1, 0)
    grid.addWidget(widgets["buttonback"][-1], 2, 0)
    buttongit.clicked.connect(Git)
    buttonback.clicked.connect(CallIn)


InicialFrame()

window.show()
sys.exit(app.exec())
