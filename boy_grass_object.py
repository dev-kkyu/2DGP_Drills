import random

from pico2d import *


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 599
        ball_kind = random.randint(0, 1)
        if ball_kind == 0:
            self.image = load_image('ball21x21.png')
            self.width = 10
        elif ball_kind == 1:
            self.image = load_image('ball41x41.png')
            self.width = 20
        self.speed = random.randint(5, 15)

    def update(self):
        if self.y > self.width + 60:
            self.y -= self.speed
        else:
            self.y = self.width + 60

    def draw(self):
        self.image.draw(self.x, self.y)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global balls
    global world

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team

    balls = [Ball() for i in range(20)]
    world += balls


def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
