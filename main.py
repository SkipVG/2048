from pygame import *
import random
win_wight = 700
win_height = 500
windows = display.set_mode((win_wight, win_height))
display.set_caption('2048')
background_color = (255,255,255)
cell_colors = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200), 
    9: (242, 177, 121),
    16: (245, 149, 99),
    32: (28, 107, 114),
    64: (79, 121, 66),
    128: (132, 195, 190),
    256: (176, 183, 198),
    512: (255, 209, 220),
    1024: (255, 200, 168),
    2048: (171, 205, 239)
}

font.init()
font2= font.SysFont('Arial', 36)
FPS = 60
game = True
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class game2048:
    def __init__(self):

while game:
    for e.type in event.get():
        if e.type == QUIT:
            game = False
