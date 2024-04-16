from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('IQ экстрасенс')

but = QPushButton('Сгенерировать')
text = QLabel('Нажми, чтобы узнать IQ ученика 8Б класса')
winner = QLabel('?')
line = QVBoxLayout()

line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(but, alignment = Qt.AlignCenter)
main_win.setLayout(line)

students = [
    'Илья',
    'Назар',
    'Катя',
    'Анжела',
    'Жанна',
    'Дима',
    'Игорь',
    'Даша',
    'Катя Смирнова',
    'Лиза',
    'Настя Оффница',
    'Валера'
]

iq = [
    66,
    228,
    200,
    66,
    120,
    1,
    200,
    200,
    150,
    66,
    66,
    66
]

iqq = [
    0,
    120,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
]

def show_winner():
    student = randint(0, 11)
    number = randint(iqq[student], iq[student])
    text.setText(students[student])
    if(number == 0):
        rnd = randint(0,1)
        if rnd == 0:
            s = "инфузория"
        else:
            s = "амёба"
    elif(number < 10):
        s = "червяк"
    elif(number < 20):
        rnd = randint(0,1)
        if rnd == 0:
            s = "рак"
        else:
            s = "гриб (моя собака умнее :+) )"
    elif(number < 30):
        s = "суслик"
    elif(number < 40):
        s = "паразит"
    elif(number < 50):
        s = "рыба"
    elif(number < 55):
        s = "боевой хомячок"
    elif(number < 60):
        s = "петух"
    elif(number < 65):
        s = "выхухоль"
    elif(number < 70):
        s = "скибиди-туалет"
    elif(number < 80):
        s = "макака"
    elif(number < 90):
        s = "гамадрил"
    elif(number < 95):
        s = "гиббон"
    elif(number < 100):
        s = "уга-чага"
    elif(number < 105):
        s = "орангутанг"
    elif(number < 110):
        s = "горилла"
    elif(number < 120):
        s = "лучше чем горилла"
    elif(170 < number < 180):
        s = "СВЕРХРАЗУМ"
    elif(180 < number < 227):
        s = "ЭКСТАСЕНС"
    elif(number == 228):
        s = "это 100% Назарыч"
    else:
        s = "человек"
    winner.setText(str(number) + " IQ, уровень развития - " +  s)

but.clicked.connect(show_winner)
main_win.show()
app.exec_()
