from display import *
from draw import *

screen = new_screen()

x = -1
x1 = 0

while (x <= 1):
    draw_line(screen, int(250*x)+250, int(250*x*x*x)+250, int(250*x1)+250, int(250*x1*x1*x1)+250, [255, 255, 255] )
    draw_line(screen, int(-250*x)+250, int(250*x*x*x)+250, int(-250*x1)+250, int(250*x1*x1*x1)+250, [255, 255, 255] )
    x += 0.016
    x1 += 0.016

"""
x = 0
y = 0
while (y<500):
    draw_line(screen, 250, 250, x, y, [255, 255, 255] )
    y += 50
while (x<500):
    draw_line(screen, 250, 250, x, y, [255, 255, 255] )
    x += 50
while (y>0):
    draw_line(screen, 250, 250, x, y, [255, 255, 255] )
    y -= 50
while (x>0):
    draw_line(screen, 250, 250, x, y, [255, 255, 255] )
    x -= 50
"""