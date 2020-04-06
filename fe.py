import curses
'''
Тестовый файл. Не должен попадать в проект, но если попадет, то я дурачёк
'''

screen = curses.initscr()
curses.mousemask(1)
screen.keypad(1)

m = ((1, 2), (3, 4))
screen.addstr(str(m[1][1]))
screen.refresh()