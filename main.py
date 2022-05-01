from pygame import *
from random import uniform
init()

W_mw = 500
H_mw = 500
mw = display.set_mode((W_mw, H_mw))
back = (123, 231, 213)
mw.fill(back)
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y, self.speed = x, y, speed

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))    

RC1 = GameSprite('rc.png', 10, H_mw/2 - 53, 16, 106, 5)
RC2 = GameSprite('rc.png', W_mw - 26, H_mw/2 - 53, 16, 106, 5)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game == False
    mw.fill(back)
    RC1.reset()
    display.update()
    clock.tick(60)