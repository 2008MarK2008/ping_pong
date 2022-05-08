from pygame import *
from random import *
init()

W_mw = 500
H_mw = 300
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

    def move(self, k1, k2):
        key_pressed = key.get_pressed()
        if key_pressed[k1] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if key_pressed[k2] and self.rect.y <= H_mw-self.rect.height:
            self.rect.y += self.speed

class Ball(GameSprite):
    def init(self, startpos, velocity, startdir):
        super().init('ball.png', W_mw/2 - 15, H_mw/2 - 15, 30, 30, 7)
        self.pos = math.Vector2(startpos)
        self.velocity = velocity
        self.dir = math.Vector2(startdir).normalize()
        self.rect = self.image.get_rect(center = (round(self.pos.x), round(self.pos.y)))
    def reflect(self, NV):
        self.dir = self.dir.reflect(math.Vector2(NV))
    def update(self):
        self.pos += self.dir * self.velocity
        self.rect.center = round(self.pos.x), round(self.pos.y)

RC1 = GameSprite('rc.png', 10, H_mw/2 - 53, 16, 106, 5)
RC2 = GameSprite('rc.png', W_mw - 26, H_mw/2 - 53, 16, 106, 5)

ball = GameSprite('ball.png', W_mw/2 - 15, H_mw/2 - 15, 30, 30, 7)
ball = Ball(mw.get_rect().center, 3, (random(), random()))

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    RC1.move(K_UP, K_DOWN)
    RC2.move(K_w, K_s)
    if ball.rect.left <= 0:
        ball.reflect((1, 0))
    if ball.rect.right >= W_mw:
        ball.reflect((-1, 0))
    if ball.rect.top <= 0:
        ball.reflect((0, 1))
    if ball.rect.bottom >= H_mw:
        ball.reflect((0, -1))
    mw.fill(back)
    RC1.reset()
    RC2.reset()
    ball.reset()
    ball.update()
    display.update()
    clock.tick(60)