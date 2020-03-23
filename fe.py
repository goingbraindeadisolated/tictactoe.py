import curses

a = int(input())
switch = {
    a > 0: "most than zero",
    a == 0: "equals zero",
    a < 0: "less then zero"
}
print(switch[True])
