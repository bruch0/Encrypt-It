# Importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import random
import webbrowser
import pyperclip

list1 = ['C', 'î', '?', 'a', 'k', 'ã', 'í', 'à', 'É', '>', 'ú', 'Q', 'W', '=', '4', 'y', '^', 'n',
         'ù', 'û', '3', 'Ò', 'Ó', 'r', 'd', 'K', 'T', '|', 'Y', 'v', 'á', ',', 'ò', 'V', 'ó', 'A',
         's', 'è', 'm', 'O', '0', 'l', '{', 'ô', 'Ù', '}', ';', '&', 'c', 'é', 'ñ', 'Ì', 'Í', 'i',
         '+', 'P', 'Ú', 'Z', 'N', 'ì', '(', 'H', 'x', 'B', 'G', 'Ã', 'g', 'Û', 'f', '6', 'j', '.',
         '-', 'M', 'F', ':', 't', '8', '$', 'º', '°', '<', 'È', '2', 'Ô', 'Â', '_', '1', 'e', 'Î',
         '5', 'ê', ')', 'h', '9', 'Ñ', 'w', 'Á', 'R', '7', 'X', 'S', 'E', '!', '@', 'â', '[', 'u',
         '"', 'p', 'q', 'D', 'À', '~', 'ª', 'Ê', '%', 'L', '`', 'z', '/', 'I', '*', 'U', 'o', '#',
         'b', ']', 'J', 'ç']

list2 = ['`', '7', '(', 'T', 'ã', 'i', 'Ô', ']', '-', 'H', '}', 'ó', 'ì', '1', 'w', '6', 'ú', 't',
         'é', 'I', '9', 'ç', 'Ù', 'B', 'Y', '{', '0', '[', '_', 's', 'Ñ', 'Ó', 'j', 'p', '"', '!', 'U',
         'g', 'Q', 'm', 'k', 'E', 'Ì', 'í', '.', 'O', 'n', '=', 'Ò', 'C', 'Í', 'Â', '?', 'Ú', 'c',
         'W', '~', 'A', 'à', '+', 'e', '4', 'â', 'S', 'ê', '#', 'q', 'Û', '°', 'f', 'è', 'ù', 'Ã',
         'D', 'Î', 'û', 'u', 'F', 'º', 'z', 'X', 'G', 'V', 'É', 'ñ', '|', '$', ';', 'J', '&', 'd',
         'N', 'h', '>', ')', 'Á', 'á', '5', '2', 'r', 'ô', 'ò', 'Z', '*', 'b', '%', 'y', 'l', '@',
         'L', 'À', '8', 'M', 'K', 'È', 'a', '^', ':', 'Ê', '/', 'x', 'î', 'R', 'v', '<', 'o', ',',
         'ª', 'P', '3']

list3 = ['î', '6', 'f', 'í', 'm', 'I', 'F', 'Á', '#', '}', 'r', 'x', 'è', '"', '`', 'é', 'd', 'g',
         's', 'c', 'e', 'Î', 'U', 'Â', 'w', '>', '(', '@', 'a', 'ì', '|', 'L', '1', 'S', '8', '~',
         'Û', 'i', '4', 'b', 'O', 'À', 'E', '{', ':', 'l', 'º', '<', 'A', 'K', 'Ã', '$', 'C', 'ù',
         '9', '0', '%', 'T', 'È', 'Í', 'ò', 'j', 'Ì', 'û', 'Ù', 'u', 'Z', 't', '?', 'ê', 'J', 'G',
         'Ô', 'z', '!', '7', '*', '5', 'Y', '.', '^', 'ã', 'k', 'v', 'Ñ', 'ª', '/', ',', ')', '2',
         'É', '-', 'ô', 'q', 'n', 'Q', 'B', '&', '_', 'Ú', 'ñ', 'Ó', ';', 'W', 'Ê', ']', '=', 'o',
         'p', 'ó', 'á', 'P', '[', 'H', 'M', 'R', '°', 'y', 'ú', 'D', 'N', 'à', '3', '+', 'X', 'V',
         'h', 'â', 'Ò', 'ç']

list4 = ['{', '2', 'ç', 't', '/', '3', 'º', 'X', 'í', 'Ó', 'Q', 'f', 'â', 'l', 'o', 'ú', 'ù', 'û', 'ó',
         'Û', '-', 'É', 'Ì', 'Z', 'î', 'È', 'n', '`', 'h', '=', 'D', ',', 'm', 'y', '7', '9', '$',
         'Ù', ']', 'I', ';', 'q', '%', '1', 'C', '5', 's', 'E', 'z', 'B', '_', 'Y', 'J', 'O', 'A',
         'M', 'j', 'b', 'S', 'Ñ', 'r', ':', 'Ê', 'ì', 'ª', 'T', '~', 'à', 'k', 'a', 'i', 'G', 'ò',
         'd', '4', 'Â', 'Á', '@', 'Ô', 'u', 'ñ', '#', 'Í', 'e', 'w', '^', '.', '?', '>', 'Ú', 'N',
         'À', 'L', 'è', '[', 'Ò', 'á', 'Ã', '(', 'P', 'V', 'K', 'H', '&', '"', '8', '!', '<', '*',
         'ê', 'U', '}', ')', 'ã', 'c', 'F', 'p', 'R', '0', 'ô', 'é', 'g', '°', 'W', 'x', 'Î', '+',
         '6', 'v', '|']

list5 = ['q', ';', '/', 'Î', 'C', '}', 'z', '6', '<', 'd', '+', 'ù', 'R', 'W', 'í', 'Ù', 'I', 'm',
         '0', 'h', 'Â', 'b', 'E', 'A', 'o', '|', '?', 'w', 'ú', 'T', 'û', '`', 'l', '{', '@', 'J',
         'L', 'Á', 'è', 'P', '4', 'á', '>', 'e', 'X', 's', '=', '.', 'é', 'j', 'H', 'Ó', '!', '*',
         '7', 'n', 'K', 'Û', 'u', 'B', 'O', 't', 'r', 'a', '~', '8', 'M', '°', 'Ñ', '3', 'È', 'Z',
         'N', 'Y', 'Ú', 'ç', 'ã', 'Ô', ']', 'U', '$', '5', '#', 'Í', 'F', 'S', 'â', 'y', 'î', 'D', 'ñ',
         'x', '[', 'ê', 'k', ',', 'à', '9', '-', 'É', '^', 'G', 'ª', 'ò', '"', '&', 'g', '(', 'Ò',
         'Ã', 'À', 'Ê', 'c', 'ì', 'ó', 'i', ':', 'º', 'p', 'ô', 'Q', 'Ì', 'f', 'v', ')', '%', '_',
         '2', '1', 'V']

list6 = ['E', 'd', 'Z', 'È', 'Y', 'ç', 'm', '_', 'Ê', 'Ã', 'M', 'T', '$', '~', 'Ú', '3', 'a', '2', 'J',
         'H', 'ù', 'n', 'o', '!', 'ô', 'Â', 'ò', 't', '6', 'û', 'ã', 'À', '/', 'ì', 'Á', 'B', '.',
         'G', '#', 'Q', 'v', 'S', '|', 'r', 'í', 'É', '4', 'w', ')', '=', 'X', 'l', '*', '8', '"',
         'Ù', 'W', 'L', ':', '<', 'â', 'i', 'Î', 'é', 'ñ', '`', 'I', '@', 'c', 'C', 'h', '[', 'U',
         '5', 'F', 'y', 'f', 'O', ']', 'Û', 'Ì', 'à', 'b', '%', 'x', 'j', '{', 'Í', 'Ò', 'q', '^',
         'ê', 'D', 'u', 'ª', 'Ô', 'N', '7', 'P', 'R', '(', 'A', '°', ',', '+', 'p', '?', 'k', '9',
         '&', 'Ó', 'Ñ', '-', 'è', 'e', '1', 'V', 'g', 'K', 's', '>', 'î', '}', ';', 'z', 'á', 'º',
         'ú', '0', 'ó']

list7 = ['ò', 'ú', 'Ù', 'S', '#', '6', 'Z', 'M', 'Â', 'à', 'á', '+', '|', 'l', 'Û', 'È', 's', '5',
         'I', '^', 'q', '<', 'K', 'Q', '}', 'v', 'x', '(', '~', 'r', 'À', 'J', 'N', '9', 'O', '"',
         'ñ', '?', 'a', 'A', 'ã', 'Á', '&', '%', 'ç', 'â', 'T', 'Y', 'Ã', 'f', 'L', '$', 'é', 'C', 'k',
         '>', 'u', '=', 'd', 'è', '3', 'h', '8', 'X', 'º', '@', 'D', 'R', 'î', 'ª', 'P', ')', 'z',
         'H', '2', 'Î', 'ó', 'ù', 'Ñ', 't', '°', 'G', '{', 'Ê', '[', 'Ó', 'V', 'B', 'Ú', 'í', '`',
         '7', '4', 'û', 'y', 'ô', 'w', 'i', 'F', 'W', 'c', ',', '_', 'ì', 'Ì', 'U', 'p', 'o', 'ê',
         'É', 'Ò', 'n', '1', '/', 'E', 'b', ':', 'j', ';', '*', '-', '0', '!', 'm', 'Ô', 'g', ']',
         'Í', 'e', '.']

list8 = ['O', 'W', 'ó', 'ù', 'S', 'É', '7', '6', '{', 'á', 's', 'H', 'k', 'u', 'B', '0', '8', 'È',
         'j', 'è', 'º', '_', '=', 'h', 'Î', 'ì', '1', '}', 'i', 'â', ';', 'C', 'ò', '3', 'w', '$',
         ',', '4', 'f', '.', '@', 'ô', '?', 'D', 'p', ':', '+', 'a', 'J', 'V', 'Ñ', 'Ô', 'N', '-',
         'r', 'G', '5', 'î', '°', 'ú', 'X', 'Ú', 't', 'I', 'T', 'ã', 'L', 'é', 'g', 'ñ', 'Q', '*',
         '(', 'e', '2', 'v', 'Z', 'Ê', 'R', 'o', 'Ó', 'û', 'F', 'Ù', 'K', '%', 'M', ')', 'À', 'z',
         'Ã', 'Á', 'Í', '<', '|', 'U', 'x', '>', 'ç', 'm', '!', '9', '#', 'ê', 'í', 'n', 'E', '^', '~',
         '/', 'b', '&', 'Û', 'ª', 'à', 'q', 'P', '"', 'd', ']', 'l', 'Y', 'Â', 'y', 'Ì', '[', 'c',
         '`', 'Ò', 'A']

list9 = ['Ù', 'g', 'V', '3', ',', 'ù', 'è', 'Ã', '9', '<', 'Q', 'ú', '.', '-', 'È', '|', 'd', '%',
         'j', 'Z', '{', 'ª', 'Û', 'I', 'Ô', 'Y', 'Î', 'A', '/', '#', 'ê', 'ñ', '8', 'k', 'É', 'E',
         ':', 'p', 'Ñ', 'Ú', '*', ']', 'z', 'w', 'R', 'î', 'Á', '[', 'S', 'J', 'í', 'r', '?', 'b',
         'B', 'l', '^', 'm', 'ô', 'q', '0', '}', 'à', 'F', 'G', '~', '+', 'Ó', '6', '2', 'º', ')',
         'Í', 'U', 'u', 'Ò', 'L', 't', 'i', '(', '$', 'e', '4', '@', 'K', '1', '"', 'Ê', '=', 'ã',
         '°', '7', 'O', 'N', 'f', 'c', 'ç', 'é', 'x', 'â', 'T', 'D', 'v', '_', '!', 'P', 'X', 'a', 'Â',
         '5', '>', 'M', 'H', ';', 'À', 'y', 'n', 'ò', 'û', 'h', 'C', 'W', 'Ì', 'ó', 's', '&', 'á',
         'o', '`', 'ì']

list10 = ['j', 'Á', 'W', 'J', 'E', 'P', 'u', '^', 'k', 'â', 't', 'ì', 's', 'a', 'ê', '>', 'F', 'Z',
          'I', 'y', '[', 'Y', 'l', 'ñ', 'S', 'f', 'ó', 'o', 'Ê', 'h', '6', 'r', '%', '+', 'Û', 'X',
          'È', 'A', 'í', '/', 'c', 'Ô', '0', 'H', 'Ú', 'i', 'ù', '5', '=', 'g', ';', '$', 'e', 'T',
          'O', 'û', 'R', '!', '~', 'Ó', 'C', '(', 'U', 'ô', '{', '&', 'á', 'Ñ', 'Ã', '4', '}', '9',
          '#', '<', 'K', 'd', '1', 'L', 'ç', 'w', 'n', 'À', 'Í', '|', 'm', '-', '2', ')', 'N', 'î', 'É',
          'b', 'Ò', '7', '8', 'Î', 'q', 'G', 'Ù', 'z', ',', 'à', '*', 'ò', 'Â', 'è', 'Ì', 'V', 'ã',
          '3', 'ú', ':', 'x', 'D', '?', 'é', '"', 'B', '@', '.', '`', 'p', ']', 'Q', 'v', '_', 'M',
          'º', 'ª', '°']

symbols = []

listkey = random.randint(1, 10)

if listkey == 1:
    symbols = list1[:]
if listkey == 2:
    symbols = list2[:]
if listkey == 3:
    symbols = list3[:]
if listkey == 4:
    symbols = list4[:]
if listkey == 5:
    symbols = list5[:]
if listkey == 6:
    symbols = list6[:]
if listkey == 7:
    symbols = list7[:]
if listkey == 8:
    symbols = list8[:]
if listkey == 9:
    symbols = list9[:]
if listkey == 10:
    symbols = list10[:]

minorkey = ['ʍ', 'µ', '±', 'Ð', 'Ø', '÷', '¾', '¿', '¶', '²', '¼', 'Ģ', 'Ŋ', 'Ż', 'Ʒ', 'ǆ', 'ǩ', 'ǽ']


# Encrypt and Decrypt functions
def EncryptFunction(texto):
    key = random.randint(1, 65)
    crypt = ''
    cont = 0
    for i in range(0, len(texto)):
        for j in range(0, len(symbols)):
            cont += 1
            if texto[i] == symbols[j]:
                if j + key >= len(symbols):
                    crypt += symbols[j - len(symbols) + key]
                    cont = 0
                else:
                    crypt += symbols[j + key]
                    cont = 0
            if cont == len(symbols):
                crypt += ' '
                cont = 0
        cont = 0
    crypt += str(key)
    if key > 9:
        crypt += minorkey[random.randint(0, len(minorkey) - 1)]
    crypt += str(listkey)

    return crypt


def DecryptFunction(texto):
    global symbols
    global minorkey
    decrypt = ''
    key = 0
    cont = 0
    flag = 0

    if texto[len(texto) - 1] == 1:
        symbols = list1[:]
    if texto[len(texto) - 1] == 2:
        symbols = list2[:]
    if texto[len(texto) - 1] == 3:
        symbols = list3[:]
    if texto[len(texto) - 1] == 4:
        symbols = list4[:]
    if texto[len(texto) - 1] == 5:
        symbols = list5[:]
    if texto[len(texto) - 1] == 6:
        symbols = list6[:]
    if texto[len(texto) - 1] == 7:
        symbols = list7[:]
    if texto[len(texto) - 1] == 8:
        symbols = list8[:]
    if texto[len(texto) - 1] == 9:
        symbols = list9[:]
    if texto[len(texto) - 1] == 10:
        symbols = list10[:]

    texto = texto[:-1]

    for i in range(0, len(minorkey)):
        if (texto[len(texto) - 1]) == minorkey[i]:
            texto = texto[:-1]
            key = int(texto[-2:])
            flag = 1
    if flag == 0:
        key = int(texto[-1:])
    for i in range(0, len(texto)):
        for j in range(0, len(symbols)):
            cont += 1
            if texto[i] == symbols[j]:
                if j + key >= len(symbols):
                    decrypt += symbols[j - len(symbols) - key]
                    cont = 0
                else:
                    decrypt += symbols[j - key]
                    cont = 0
            if cont == len(symbols):
                decrypt += ' '
                cont = 0
        cont = 0
    if key > 9:
        decrypt = decrypt[:-2]
    else:
        decrypt = decrypt[:-1]

    return decrypt


# Function to update constantly the content of the encrypt textbox and copy to the user
def UpdateTextEncrypt(document):
    global textEn
    textEn = document.toPlainText()


def CopyEn():
    global textEn
    x = EncryptFunction(textEn)
    pyperclip.copy(x)


def MsgEncrypt():
    msg = QMessageBox()
    msg.setWindowTitle("Encrypted!")
    msg.setText("Your text is encrypted and copied in your Ctrl + C")

    msg.exec_()


def UpdateTextDecrypt(document):
    global textDe
    textDe = document.toPlainText()


def CopyDe():
    global textDe
    y = DecryptFunction(textDe)
    pyperclip.copy(y)


def MsgDecrypt():
    msg = QMessageBox()
    msg.setWindowTitle("Decrypted!")
    msg.setText("Your text is decrypted and copied in your Ctrl + C")

    msg.exec_()


# Function to close the App
def Close():
    sys.exit(App.exec())


# Function to minimize the App
def Minimize():
    window.showMinimized()


# noinspection PyArgumentList
def GitHub():
    webbrowser.open('https://github.com/bruch0')


class Window(QMainWindow):
    def __init__(self):
        global DocumentDe
        global DocumentEn

        super().__init__()

        # Setting geometry
        self.setFixedWidth(1000)
        self.setFixedHeight(500)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # MAIN FRAME

        # Display Background
        self.Background = QLabel(self)
        self.Background.setPixmap(QPixmap("Backgroud.png"))
        self.Background.setFixedHeight(500)
        self.Background.setFixedWidth(1000)
        self.Background.setStyleSheet(
            "margin: 0px;" +
            "border: 4px solid '#161219';" +
            "border-radius: 10px;"
        )

        # Display Top Bar
        self.TopBar = QLabel(self)
        self.TopBar.setPixmap(QPixmap("TopBar.png"))
        self.TopBar.setFixedHeight(40)
        self.TopBar.setFixedWidth(1000)
        self.TopBar.setStyleSheet(
            "margin: 0px;" +
            "border: 4px solid '#2F3136';" +
            "border-radius: 5px;"
        )

        # Display App name
        self.Name = QLabel(self)
        self.Name.setText("ENCRYPT - IT")
        self.Name.setFixedWidth(150)
        self.Name.move(5, 4)
        self.Name.setStyleSheet(
            "background: transparent;"
            "font-size: 20px;" +
            "color: #c2c0bc;" +
            "border: 0px;"
        )

        # Display Main logo
        self.MainLogo = QLabel(self)
        self.MainLogo.setPixmap(QPixmap("logo.png"))
        self.MainLogo.setFixedHeight(150)
        self.MainLogo.setFixedWidth(500)
        self.MainLogo.move(250, 50)
        self.MainLogo.setStyleSheet("margin-top: 0px;")

        # Button to Encrypt Frame
        self.ButtonEncryptFrame = QPushButton("ENCRYPT", self)
        self.ButtonEncryptFrame.move(250, 230)
        self.ButtonEncryptFrame.setFixedHeight(85)
        self.ButtonEncryptFrame.setFixedWidth(500)
        self.ButtonEncryptFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonEncryptFrame.setStyleSheet(
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )

        # Button Decrypt Frame
        self.ButtonDecryptFrame = QPushButton("DECRYPT", self)
        self.ButtonDecryptFrame.move(250, 320)
        self.ButtonDecryptFrame.setFixedHeight(85)
        self.ButtonDecryptFrame.setFixedWidth(500)
        self.ButtonDecryptFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonDecryptFrame.setStyleSheet(
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )

        # Button about
        self.ButtonAboutFrame = QPushButton("HOW TO USE", self)
        self.ButtonAboutFrame.move(250, 410)
        self.ButtonAboutFrame.setFixedHeight(85)
        self.ButtonAboutFrame.setFixedWidth(500)
        self.ButtonAboutFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonAboutFrame.setStyleSheet(
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )

        # Button close
        self.ButtonClose = QPushButton("x", self)
        self.ButtonClose.move(965, 5)
        self.ButtonClose.setFixedHeight(30)
        self.ButtonClose.setFixedWidth(30)
        self.ButtonClose.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonClose.setStyleSheet(
            '''*{
            background: '#2F3136';
            border: 2px solid '#2F3136';
            border-radius: 5px;
            font-size: 20px;
            color: '#c2c0bc';
        }
        *:hover{
            background: '#8A2BE2';
        }'''
        )

        # Button minimize
        self.ButtonMinimize = QPushButton("-", self)
        self.ButtonMinimize.move(935, 5)
        self.ButtonMinimize.setFixedHeight(30)
        self.ButtonMinimize.setFixedWidth(30)
        self.ButtonMinimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonMinimize.setStyleSheet(
            '''*{
            background: '#2F3136';
            border: 2px solid '#2F3136';
            border-radius: 5px;
            font-size: 20px;
            color: '#c2c0bc';
        }
        *:hover{
            background: '#8A2BE2';
        }'''
        )

        # ENCRYPT FRAME

        # Display Encrypt logo
        self.EncLogo = QLabel(self)
        self.EncLogo.setPixmap(QPixmap("enclogo.png"))
        self.EncLogo.setFixedHeight(85)
        self.EncLogo.setFixedWidth(500)
        self.EncLogo.move(250, 50)
        self.EncLogo.setStyleSheet("margin-top: 0px;")
        self.EncLogo.hide()

        # Display user input area
        self.TextBoxEncrypt = QTextEdit(self)
        self.TextBoxEncrypt.setFixedHeight(150)
        self.TextBoxEncrypt.setFixedWidth(500)
        self.TextBoxEncrypt.move(250, 165)
        self.TextBoxEncrypt.setStyleSheet(
            "background: '#161219';" +
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )
        self.TextBoxEncrypt.hide()

        DocumentEn = self.TextBoxEncrypt.document()
        DocumentEn.contentsChange.connect(lambda: UpdateTextEncrypt(DocumentEn))

        # Button Encrypt
        self.ButtonEncrypt = QPushButton(self)
        self.ButtonEncrypt.setText("ENCRYPT!")
        self.ButtonEncrypt.move(250, 320)
        self.ButtonEncrypt.setFixedHeight(85)
        self.ButtonEncrypt.setFixedWidth(500)
        self.ButtonEncrypt.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonEncrypt.setStyleSheet(
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )
        self.ButtonEncrypt.hide()

        # Button back Encrypt
        self.ButtonBackEncrypt = QPushButton(self)
        self.ButtonBackEncrypt.setText("BACK")
        self.ButtonBackEncrypt.move(250, 410)
        self.ButtonBackEncrypt.setFixedHeight(85)
        self.ButtonBackEncrypt.setFixedWidth(500)
        self.ButtonBackEncrypt.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonBackEncrypt.setStyleSheet(
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )
        self.ButtonBackEncrypt.hide()

        # DECRYPT FRAME

        # Display Decrypt logo
        self.DecLogo = QLabel(self)
        self.DecLogo.setPixmap(QPixmap("declogo.png"))
        self.DecLogo.setFixedHeight(85)
        self.DecLogo.setFixedWidth(500)
        self.DecLogo.move(250, 50)
        self.DecLogo.setStyleSheet("margin-top: 0px;")
        self.DecLogo.hide()

        # Display user input area
        self.TextBoxDecrypt = QTextEdit(self)
        self.TextBoxDecrypt.setFixedHeight(150)
        self.TextBoxDecrypt.setFixedWidth(500)
        self.TextBoxDecrypt.move(250, 165)
        self.TextBoxDecrypt.setStyleSheet(
            "background: '#161219';" +
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )
        self.TextBoxDecrypt.hide()

        DocumentDe = self.TextBoxDecrypt.document()
        DocumentDe.contentsChange.connect(lambda: UpdateTextDecrypt(DocumentDe))

        # Button Decrypt
        self.ButtonDecrypt = QPushButton(self)
        self.ButtonDecrypt.setText("DECRYPT!")
        self.ButtonDecrypt.move(250, 320)
        self.ButtonDecrypt.setFixedHeight(85)
        self.ButtonDecrypt.setFixedWidth(500)
        self.ButtonDecrypt.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonDecrypt.setStyleSheet(
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )
        self.ButtonDecrypt.hide()

        # Button back Decrypt
        self.ButtonBackDecrypt = QPushButton(self)
        self.ButtonBackDecrypt.setText("BACK")
        self.ButtonBackDecrypt.move(250, 410)
        self.ButtonBackDecrypt.setFixedHeight(85)
        self.ButtonBackDecrypt.setFixedWidth(500)
        self.ButtonBackDecrypt.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonBackDecrypt.setStyleSheet(
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )
        self.ButtonBackDecrypt.hide()

        # HOW TO USE FRAMES
        # HOW TO USE FRAME 1
        # Display How to use part 1
        self.HowToUse1 = QLabel(self)
        self.HowToUse1.setPixmap(QPixmap("howtouse1.png"))
        self.HowToUse1.setFixedHeight(250)
        self.HowToUse1.setFixedWidth(510)
        self.HowToUse1.move(250, 50)
        self.HowToUse1.setStyleSheet("margin-top: 0px;")
        self.HowToUse1.hide()

        # Button NextToHowToUse part 2
        self.NextToHowToUse2 = QPushButton(self)
        self.NextToHowToUse2.setText("NEXT")
        self.NextToHowToUse2.move(250, 320)
        self.NextToHowToUse2.setFixedHeight(85)
        self.NextToHowToUse2.setFixedWidth(500)
        self.NextToHowToUse2.setCursor(QCursor(Qt.PointingHandCursor))
        self.NextToHowToUse2.setStyleSheet(
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )
        self.NextToHowToUse2.hide()

        # Button Back to Initial from How To Use part 1
        self.BackFromHTU1 = QPushButton(self)
        self.BackFromHTU1.setText("BACK")
        self.BackFromHTU1.move(250, 410)
        self.BackFromHTU1.setFixedHeight(85)
        self.BackFromHTU1.setFixedWidth(500)
        self.BackFromHTU1.setCursor(QCursor(Qt.PointingHandCursor))
        self.BackFromHTU1.setStyleSheet(
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )
        self.BackFromHTU1.hide()

        # HOW TO USE FRAME 2
        # Display How to use part 2
        self.HowToUse2 = QLabel(self)
        self.HowToUse2.setPixmap(QPixmap("howtouse2.png"))
        self.HowToUse2.setFixedHeight(250)
        self.HowToUse2.setFixedWidth(510)
        self.HowToUse2.move(250, 50)
        self.HowToUse2.setStyleSheet("margin-top: 0px;")
        self.HowToUse2.hide()

        # Button NextToHowToUse part 2
        self.NextToHowToUse3 = QPushButton(self)
        self.NextToHowToUse3.setText("NEXT")
        self.NextToHowToUse3.move(250, 320)
        self.NextToHowToUse3.setFixedHeight(85)
        self.NextToHowToUse3.setFixedWidth(500)
        self.NextToHowToUse3.setCursor(QCursor(Qt.PointingHandCursor))
        self.NextToHowToUse3.setStyleSheet(
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )
        self.NextToHowToUse3.hide()

        # Button Back to HTU1 from How To Use part 2
        self.BackFromHTU2 = QPushButton(self)
        self.BackFromHTU2.setText("BACK")
        self.BackFromHTU2.move(250, 410)
        self.BackFromHTU2.setFixedHeight(85)
        self.BackFromHTU2.setFixedWidth(500)
        self.BackFromHTU2.setCursor(QCursor(Qt.PointingHandCursor))
        self.BackFromHTU2.setStyleSheet(
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )
        self.BackFromHTU2.hide()

        # HOW TO USE FRAME 3
        # Display How to use part 3
        self.HowToUse3 = QLabel(self)
        self.HowToUse3.setPixmap(QPixmap("howtouse3.png"))
        self.HowToUse3.setFixedHeight(250)
        self.HowToUse3.setFixedWidth(510)
        self.HowToUse3.move(250, 50)
        self.HowToUse3.setStyleSheet("margin-top: 0px;")
        self.HowToUse3.hide()

        # Button NextToHowToUse part 2
        self.NextToHowToUse4 = QPushButton(self)
        self.NextToHowToUse4.setText("NEXT")
        self.NextToHowToUse4.move(250, 320)
        self.NextToHowToUse4.setFixedHeight(85)
        self.NextToHowToUse4.setFixedWidth(500)
        self.NextToHowToUse4.setCursor(QCursor(Qt.PointingHandCursor))
        self.NextToHowToUse4.setStyleSheet(
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )
        self.NextToHowToUse4.hide()

        # Button Back to HTU2 from How To Use part 3
        self.BackFromHTU3 = QPushButton(self)
        self.BackFromHTU3.setText("BACK")
        self.BackFromHTU3.move(250, 410)
        self.BackFromHTU3.setFixedHeight(85)
        self.BackFromHTU3.setFixedWidth(500)
        self.BackFromHTU3.setCursor(QCursor(Qt.PointingHandCursor))
        self.BackFromHTU3.setStyleSheet(
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )
        self.BackFromHTU3.hide()

        # HOW TO USE FRAME 4
        # Display How to use part 4
        self.HowToUse4 = QLabel(self)
        self.HowToUse4.setPixmap(QPixmap("howtouse4.png"))
        self.HowToUse4.setFixedHeight(250)
        self.HowToUse4.setFixedWidth(510)
        self.HowToUse4.move(250, 50)
        self.HowToUse4.setStyleSheet("margin-top: 0px;")
        self.HowToUse4.hide()

        # Button NextToHowToUse part 4
        self.NextToHowToUse5 = QPushButton(self)
        self.NextToHowToUse5.setText("NEXT")
        self.NextToHowToUse5.move(250, 320)
        self.NextToHowToUse5.setFixedHeight(85)
        self.NextToHowToUse5.setFixedWidth(500)
        self.NextToHowToUse5.setCursor(QCursor(Qt.PointingHandCursor))
        self.NextToHowToUse5.setStyleSheet(
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )
        self.NextToHowToUse5.hide()

        # Button Back to HTU3 from How To Use part 4
        self.BackFromHTU4 = QPushButton(self)
        self.BackFromHTU4.setText("BACK")
        self.BackFromHTU4.move(250, 410)
        self.BackFromHTU4.setFixedHeight(85)
        self.BackFromHTU4.setFixedWidth(500)
        self.BackFromHTU4.setCursor(QCursor(Qt.PointingHandCursor))
        self.BackFromHTU4.setStyleSheet(
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )
        self.BackFromHTU4.hide()

        # HOW TO USE FRAME 4
        # Display How to use part 4
        self.HowToUse5 = QLabel(self)
        self.HowToUse5.setPixmap(QPixmap("howtouse5.png"))
        self.HowToUse5.setFixedHeight(250)
        self.HowToUse5.setFixedWidth(510)
        self.HowToUse5.move(250, 50)
        self.HowToUse5.setStyleSheet("margin-top: 0px;")
        self.HowToUse5.hide()

        # Button GitHub
        self.Git = QPushButton(self)
        self.Git.setText("MY GITHUB ACCOUNT")
        self.Git.move(250, 320)
        self.Git.setFixedHeight(85)
        self.Git.setFixedWidth(500)
        self.Git.setCursor(QCursor(Qt.PointingHandCursor))
        self.Git.setStyleSheet(
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )
        self.Git.hide()

        # Button Back to HTU3 from How To Use part 4
        self.BackFromHTU5 = QPushButton(self)
        self.BackFromHTU5.setText("BACK")
        self.BackFromHTU5.move(250, 410)
        self.BackFromHTU5.setFixedHeight(85)
        self.BackFromHTU5.setFixedWidth(500)
        self.BackFromHTU5.setCursor(QCursor(Qt.PointingHandCursor))
        self.BackFromHTU5.setStyleSheet(
            "border: 4px solid '#8A2BE2';" +
            "border-radius: 5px;" +
            "font-size: 35px;" +
            "color: 'white';"
        )
        self.BackFromHTU5.hide()

        # Connecting method when button get clicked
        self.ButtonEncryptFrame.clicked.connect(self.CallEncryptFrame)
        self.ButtonDecryptFrame.clicked.connect(self.CallDecryptFrame)
        self.ButtonAboutFrame.clicked.connect(self.CallHowToUseFrames)

        # Connecting to Encrypt function
        self.ButtonEncrypt.clicked.connect(lambda: UpdateTextEncrypt(DocumentEn))
        self.ButtonEncrypt.clicked.connect(CopyEn)
        self.ButtonEncrypt.clicked.connect(MsgEncrypt)
        self.ButtonBackEncrypt.clicked.connect(self.ClearTextBoxEn)
        self.ButtonBackEncrypt.clicked.connect(self.CallInitialFrameFromEncrypt)

        # Connecting to Decrypt function
        self.ButtonDecrypt.clicked.connect(lambda: UpdateTextDecrypt(DocumentDe))
        self.ButtonDecrypt.clicked.connect(CopyDe)
        self.ButtonDecrypt.clicked.connect(MsgDecrypt)
        self.ButtonBackDecrypt.clicked.connect(self.ClearTextBoxDe)
        self.ButtonBackDecrypt.clicked.connect(self.CallInitialFrameFromDecrypt)

        # Connecting to How to Use frame 1
        self.NextToHowToUse2.clicked.connect(self.CallHowToUse2)
        self.BackFromHTU1.clicked.connect(self.CallInitialFrameFromHowToUse)

        # Connecting to How to Use frame 2
        self.NextToHowToUse3.clicked.connect(self.CallHowToUse3)
        self.BackFromHTU2.clicked.connect(self.CallBackHowToUse1)

        # Connecting to How to Use frame 3
        self.NextToHowToUse4.clicked.connect(self.CallHowToUse4)
        self.BackFromHTU3.clicked.connect(self.CallBackHowToUse2)

        # Connecting to How to Use frame 4
        self.NextToHowToUse5.clicked.connect(self.CallHowToUse5)
        self.BackFromHTU4.clicked.connect(self.CallBackHowToUse3)

        # Connecting to How to Use frame 5
        self.Git.clicked.connect(GitHub)
        self.BackFromHTU5.clicked.connect(self.CallInitialFrameFromHowToUse5)

        # Connecting to the close app function
        self.ButtonClose.clicked.connect(Close)

        # Connecting to the minimize app function
        self.ButtonMinimize.clicked.connect(Minimize)

        # showing all the widgets
        self.show()

    # Functions to call frames

    def CallInitialFrameFromEncrypt(self):
        # Hiding the encrypt frame
        self.EncLogo.hide()
        self.TextBoxEncrypt.hide()
        self.ButtonEncrypt.hide()
        self.ButtonBackEncrypt.hide()

        # Showing the initial frame
        self.MainLogo.show()
        self.ButtonEncryptFrame.show()
        self.ButtonDecryptFrame.show()
        self.ButtonAboutFrame.show()

    def CallInitialFrameFromDecrypt(self):
        # Hiding the encrypt frame
        self.DecLogo.hide()
        self.TextBoxDecrypt.hide()
        self.ButtonDecrypt.hide()
        self.ButtonBackDecrypt.hide()

        # Showing the initial frame
        self.MainLogo.show()
        self.ButtonEncryptFrame.show()
        self.ButtonDecryptFrame.show()
        self.ButtonAboutFrame.show()

    def CallInitialFrameFromHowToUse(self):
        # Hiding the How to Use Frame
        self.HowToUse1.hide()
        self.NextToHowToUse2.hide()
        self.BackFromHTU1.hide()

        # Showing the initial frame
        self.MainLogo.show()
        self.ButtonEncryptFrame.show()
        self.ButtonDecryptFrame.show()
        self.ButtonAboutFrame.show()

    def CallInitialFrameFromHowToUse5(self):
        # Hiding the How to Use Frame
        self.HowToUse5.hide()
        self.Git.hide()
        self.BackFromHTU5.hide()

        # Showing the initial frame
        self.MainLogo.show()
        self.ButtonEncryptFrame.show()
        self.ButtonDecryptFrame.show()
        self.ButtonAboutFrame.show()

    def CallEncryptFrame(self):
        # Hiding the main frame
        self.MainLogo.hide()
        self.ButtonEncryptFrame.hide()
        self.ButtonDecryptFrame.hide()
        self.ButtonAboutFrame.hide()

        # Showing the encrypt frame
        self.EncLogo.show()
        self.TextBoxEncrypt.show()
        self.ButtonEncrypt.show()
        self.ButtonBackEncrypt.show()

    def ClearTextBoxEn(self):
        self.TextBoxEncrypt.clear()

    def ClearTextBoxDe(self):
        self.TextBoxDecrypt.clear()

    def CallDecryptFrame(self):
        # Hiding the main frame
        self.MainLogo.hide()
        self.ButtonEncryptFrame.hide()
        self.ButtonDecryptFrame.hide()
        self.ButtonAboutFrame.hide()

        # Showing the encrypt frame
        self.DecLogo.show()
        self.TextBoxDecrypt.show()
        self.ButtonDecrypt.show()
        self.ButtonBackDecrypt.show()

    def CallHowToUseFrames(self):
        # Hiding the main frame
        self.MainLogo.hide()
        self.ButtonEncryptFrame.hide()
        self.ButtonDecryptFrame.hide()
        self.ButtonAboutFrame.hide()

        # Showing the encrypt frame
        self.HowToUse1.show()
        self.NextToHowToUse2.show()
        self.BackFromHTU1.show()

    def CallHowToUse2(self):
        # Hiding the HTU frame 1
        self.HowToUse1.hide()
        self.NextToHowToUse2.hide()
        self.BackFromHTU1.hide()

        # Showing the HTU frame 2
        self.HowToUse2.show()
        self.NextToHowToUse3.show()
        self.BackFromHTU2.show()

    def CallBackHowToUse1(self):
        # Showing the HTU frame 1
        self.HowToUse2.hide()
        self.NextToHowToUse3.hide()
        self.BackFromHTU2.hide()

        # Hiding the HTU frame 2
        self.HowToUse1.show()
        self.NextToHowToUse2.show()
        self.BackFromHTU1.show()

    def CallHowToUse3(self):
        # Hiding the HTU frame 2
        self.HowToUse2.hide()
        self.NextToHowToUse3.hide()
        self.BackFromHTU2.hide()

        # Showing the HTU frame 3
        self.HowToUse3.show()
        self.NextToHowToUse4.show()
        self.BackFromHTU3.show()

    def CallBackHowToUse2(self):
        # Showing the HTU frame 2
        self.HowToUse3.hide()
        self.NextToHowToUse4.hide()
        self.BackFromHTU3.hide()

        # Hiding the HTU frame 3
        self.HowToUse2.show()
        self.NextToHowToUse3.show()
        self.BackFromHTU2.show()

    def CallHowToUse4(self):
        # Hiding the HTU frame 3
        self.HowToUse3.hide()
        self.NextToHowToUse4.hide()
        self.BackFromHTU3.hide()

        # Showing the HTU frame 4
        self.HowToUse4.show()
        self.NextToHowToUse5.show()
        self.BackFromHTU4.show()

    def CallBackHowToUse3(self):
        # Showing the HTU frame 2
        self.HowToUse4.hide()
        self.NextToHowToUse5.hide()
        self.BackFromHTU4.hide()

        # Hiding the HTU frame 3
        self.HowToUse3.show()
        self.NextToHowToUse4.show()
        self.BackFromHTU3.show()

    def CallHowToUse5(self):
        # Hiding the HTU frame 4
        self.HowToUse4.hide()
        self.NextToHowToUse5.hide()
        self.BackFromHTU4.hide()

        # Showing the HTU frame 5
        self.HowToUse5.show()
        self.Git.show()
        self.BackFromHTU5.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
