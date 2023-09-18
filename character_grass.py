from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
flag = True

direct = 0
def draw_rect():
	global x, y, direct, flag, angle
	if direct == 0 and x >= 750:
		direct = 1
		x = 750
	elif direct == 1 and y >= 550:
		direct = 2
		y = 550
	elif direct == 2 and x <= 50:
		direct = 3
		x = 50
	elif direct == 3 and y <= 90:
		direct = 0
		y = 90
	if direct == 0:
		x = x + 2
	elif direct == 1:
		y = y + 2
	elif direct == 2:
		x = x - 2
	elif direct == 3:
		y = y - 2
	else:
		print('direct error')
	if y > 89 and y < 91 and x > 399 and x < 401:
		x = 400
		y = 90
		flag = False
		angle = -90

angle = -90
def draw_circle():
	global x, y, flag, angle, direct
	lenth = 220
	x = 400 + math.cos(angle / 180 * math.pi) * lenth
	y = 320 + math.sin(angle / 180 * math.pi) * lenth
	angle = angle - 1
	if angle <= -360:
		angle = 1
	if angle == -90:
		flag = True
		direct = 0
		x = 400
		y = 90
	

while True:
	clear_canvas_now()
	grass.draw_now(400, 30)
	character.draw_now(x, y)
	if flag:
		draw_rect()
	else:
		draw_circle()
	delay(0.0001)

close_canvas()