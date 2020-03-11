import curses

screen = curses.initscr()

screen.addch(2, 2, "@")
screen.addch(2, 2, "@")
screen.addch(2, 2, "@")

screen.refresh()
screen.getch()
rows, cols = screen.getmaxyx()
print("Rows:    %d" % rows)
print("Columns: %d" % cols)
curses.resizeterm(20, 20)

print("Rows:    %d" % rows)
print("Columns: %d" % cols)
