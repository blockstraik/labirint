from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from random import randint

#создаем объект приложения
app = QApplication([])
#создаем главное окно
main_win = QWidget()

#задаем название окну
main_win.setWindowTitle('Win Randomizer')
#задаем размер окну
main_win.resize(400, 200)

#надпись
main_label = QLabel('Нажми, чтобы узнать победителя')
#надпись
winner_label = QLabel('?')
#кнопка
checker_button = QPushButton('Сгенерировать')

#создаем главный лейаут
main_layout = QVBoxLayout()
#добавляем виджеты в лейаут
main_layout.addWidget(main_label, alignment = Qt.AlignCenter)
main_layout.addWidget(winner_label, alignment = Qt.AlignCenter)
main_layout.addWidget(checker_button, alignment = Qt.AlignCenter)
#задаем окну лейаут, который будет отображаться
main_win.setLayout(main_layout)

def rand_win():
    num = randint(0, 100)
    winner_label.setText(str(num))
    main_label.setText('Победитель:')
    
checker_button.clicked.connect(rand_win)
#отображаем окно
main_win.show()
#оставляем приложение на экране, пока не нажат крестик
app.exec_()
