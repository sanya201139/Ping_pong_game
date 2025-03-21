from pygame import *
from random import *


win_width = 700
win_height = 500
FPS = 60

run = True
Finish = False

window = display.set_mode((win_width , win_height))
display.set_caption('Ping-pong game')
window.fill((29, 205, 245))
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y += speed
        if keys_pressed[K_DOWN] and self.rect.y < 495:
            self.rect.y -= speed
    def update2(self):
        keys = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= speed
        if keys_pressed[K_s] and self.rect.y < 495:
            self.rect.y += speed
    

class Enemy(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0

racket1 = Player('ping-pong.py\racket.jpg', 50, 250, 5)
racket2 = Player('ping-pong.py\racket.jpg', 650, 250, 5)

while run:
    
    for i in event.get():
        if i.type == QUIT:
            run = False
    clock.tick(FPS)
    display.update()

