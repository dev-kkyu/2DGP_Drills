# 이것은 각 상태들을 객체로 구현한 것임.

import random
from pico2d import load_image, clamp
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0   # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# Boy Action Speed
# fill here
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100, 1500), random.randint(100, 500)
        self.frame = random.randint(0, 13)  # 0~13, 0~4/5~9/10~13(5, 5, 4)
        self.dir = 1
        self.image = load_image('bird_animation.png')

        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(25, self.x, 1600-25)
        if self.x > 1550:
            self.dir = -1
        elif self.x < 50:
            self.dir = 1

    def handle_event(self, event):
        pass

    def draw(self):
        frame_num = 0
        if int(self.frame) < 5:
            frame_num = 2
        elif int(self.frame) < 10:
            frame_num = 1
        if self.dir == 1:
            self.image.clip_composite_draw((int(self.frame) % 5) * 183, frame_num * 168, 183, 168,
                                          0, '', self.x, self.y, 100, 100)
        else:
            self.image.clip_composite_draw((int(self.frame) % 5) * 183, frame_num * 168, 183, 168,
                                           0, 'h', self.x, self.y, 100, 100)

