from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_img = load_image('hand_arrow.png')


def handle_events():
	global running
	# global x, y
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			running = False
		# elif event.type == SDL_MOUSEMOTION:
		#     x, y = event.x, TUK_HEIGHT - 1 - event.y
		elif event.type == SDL_KEYDOWN:
			if event.key == SDLK_ESCAPE:
				running = False
	pass

def random_position():
	global rx, ry
	global is_arrived

	if (is_arrived == True):
		is_arrived = False
		rx, ry = (random.randint(0, TUK_WIDTH - 1), random.randint(0, TUK_HEIGHT - 1))

def go_hand():
	global x, y, rx, ry
	global is_arrived, look

	x1, y1 = x, y
	x2, y2 = rx, ry

	if x1 < x2:
		look = 'right'
	elif x1 > x2:
		look = 'left'

	t = 1 / 150
	x = (1 - t) * x1 + t * x2
	y = (1 - t) * y1 + t * y2
	if x > rx - 1 and x < rx + 1 and y > ry - 1 and y < ry + 1:
		is_arrived = True




running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
rx, ry = x, y
is_arrived = True
look = 'right'
frame = 0
frame_time = 30
# hide_cursor()

while running:
	clear_canvas()
	TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
	hand_img.clip_composite_draw(0, 0, 50, 52, 0, 'n', rx, ry)
	if look == 'right':
		character.clip_draw((frame // frame_time) * 100, 100 * 1, 100, 100, x, y)
	elif look == 'left':
		character.clip_draw((frame // frame_time) * 100, 100 * 0, 100, 100, x, y)
	update_canvas()
	frame = (frame + 1) % (8 * frame_time)
	random_position()
	go_hand()

	handle_events()

close_canvas()




