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

def animate_sheet(state):
	global x, y, frame, minus
	if state == 'idle':
		frame = frame % 3
		character.clip_draw(23 + (frame * 33), 546, 33, 36, x, y, 80, 85)
		frame += 1
	elif state == 'right':
		frame = frame % 10
		character.clip_draw(45 + (frame * 30), 799, 30, 27, x, y, 80, 75)
		frame += 1
	elif state == 'left':
		frame = frame % 10
		character.clip_composite_draw(45 + (frame * 30), 799, 30, 27, 0, 'h', x, y, 80, 75)
		frame += 1
	elif state == 'up':
		frame = frame % 4
		character.clip_draw(44 + (frame * 34), 431, 28, 32, x, y, 80, 85)
		if minus:
			frame -= 1
			if frame <= 0:
				minus = False
		else:
			frame += 1
			if frame >= 3:
				minus = True
	elif state == 'down':
		frame = frame % 4
		character.clip_draw(8 + (frame * 33), 109, 30, 27, x, y, 80, 70)
		if minus:
			frame -= 1
			if frame <= 0:
				minus = False
		else:
			frame += 1
			if frame >= 3:
				minus = True

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dirx, diry = 0, 0
minus = False
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
	if x >= TUK_WIDTH - 30:
		x = TUK_WIDTH - 31
	elif x < 30:
		x = 30
	if y >= TUK_HEIGHT - 30:
		y = TUK_HEIGHT - 31
	elif y < 30:
		y = 30
	delay(0.05)

close_canvas()
