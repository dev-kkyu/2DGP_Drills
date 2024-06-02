from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_img = load_image('hand_arrow.png')

def handle_events():
	global running, mouse_list
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN:
			if event.key == SDLK_ESCAPE:
				running = False
		elif event.type == SDL_MOUSEBUTTONDOWN:
			if event.button == 1:	# 왼쪽버튼
				mouse_list.append((event.x, TUK_HEIGHT - 1 - event.y))
	pass

def find_dest():
	global is_arrived, mouse_list
	global x, y, t, look
	global start_x, start_y, end_x, end_y

	if is_arrived == True:
		if mouse_list:
			start_x = x
			start_y = y
			end_x = mouse_list[0][0]
			end_y = mouse_list[0][1]
			is_arrived = False
			t = 0
			if start_x < end_x:
				look = 'right'
			elif start_x > end_x:
				look = 'left'


def go_hand():
	global x, y, t
	global start_x, start_y, end_x, end_y
	global is_arrived, look, mouse_list

	if not is_arrived:
		x = (1 - t) * start_x + t * end_x
		y = (1 - t) * start_y + t * end_y

		length = (((end_x - start_x) ** 2) + ((end_y - start_y) ** 2)) ** 0.5
		
		t += (1 / length)

	if t > 1:
		x, y = end_x, end_y
		if mouse_list:
			del mouse_list[0]
		is_arrived = True


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
t = 0
start_x, start_y = x, y
end_x, end_y = x, y
is_arrived = True
look = 'right'
frame = 0
frame_time = 30
mouse_list = []


while running:
	clear_canvas()
	TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

	for m in mouse_list:
		hand_img.clip_draw(0, 0, 50, 52, m[0], m[1])
	if look == 'right':
		character.clip_draw((frame // frame_time) * 100, 100 * 1, 100, 100, x, y)
	elif look == 'left':
		character.clip_draw((frame // frame_time) * 100, 100 * 0, 100, 100, x, y)
	update_canvas()
	frame = (frame + 1) % (frame_time * 8)

	find_dest()
	go_hand()

	handle_events()

close_canvas()


