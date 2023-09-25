from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')

character = load_image('kirby_sheet.png')

def handle_events():
	global running
	global dirx, diry

	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN:
			if event.key == SDLK_RIGHT:
				dirx += 1
			elif event.key == SDLK_LEFT:
				dirx -= 1
			elif event.key == SDLK_UP:
				diry += 1
			elif event.key == SDLK_DOWN:
				diry -= 1
			elif event.key == SDLK_ESCAPE:
				running = False
		elif event.type == SDL_KEYUP:
			if event.key == SDLK_RIGHT:
				dirx -= 1
			elif event.key == SDLK_LEFT:
				dirx += 1
			elif event.key == SDLK_UP:
				diry -= 1
			elif event.key == SDLK_DOWN:
				diry += 1
# 404 898
def animate_sheet(state):
	global x, y, frame
	if state == 'idle':
		frame = frame % 3
		character.clip_draw(23 + (frame * 33), 546, 33, 36, x, y, 80, 85)
		delay(0.05)
		pass
	elif state == 'right':
		frame = frame % 10
		character.clip_draw(45 + (frame * 30), 799, 30, 27, x, y, 80, 75)
		pass
	elif state == 'left':
		frame = frame % 10
		character.clip_composite_draw(45 + (frame * 30), 799, 30, 27, 0, 'h', x, y, 80, 75)
		pass
	elif state == 'up':
		pass
	elif state == 'down':
		pass
	frame += 1

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dirx, diry = 0, 0
frame = 0

while running:
	clear_canvas()
	tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

	if dirx > 0:
		animate_sheet('right')
	elif dirx < 0:
		animate_sheet('left')
	elif diry > 0:
		animate_sheet('up')
	elif diry < 0:
		animate_sheet('down')
	else:
		animate_sheet('idle')

	update_canvas()
	handle_events()
	x += dirx * 10
	y += diry * 10
	delay(0.05)

close_canvas()
