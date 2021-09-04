from PyQt5 import QtWidgets
import sys
import json

def show_text_word():
    window = QtWidgets.QWidget()
    filename = "words.json"
    with open(filename,"r", encoding = 'utf8') as read_file: 
        data = json.load(read_file)
    if len(data) != 0:
        for row in data:
            print(row['WORD'] + '     ' + row['READING'] + '     ' + row['TRANSLATION'] + ';')

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Первая программа на PyQt")
window.resize(300, 70)
label = QtWidgets.QLabel("<center>Словарь</center>")
btn1 = QtWidgets.QPushButton("Добавить кандзи")
btn2 = QtWidgets.QPushButton("Добавить слово для кандзи")
btn3 = QtWidgets.QPushButton("Повторить кандзи")
btn4 = QtWidgets.QPushButton("Добавить слово")
btn5 = QtWidgets.QPushButton("Посмотреть все слова")
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btn1)
vbox.addWidget(btn2)
vbox.addWidget(btn3)
vbox.addWidget(btn4)
vbox.addWidget(btn5)
window.setLayout(vbox)
btn5.clicked.connect(show_text_word)
window.show()
sys.exit(app.exec_())