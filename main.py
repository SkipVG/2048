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
size = 4
cell_size = 100
margin = 10
board_width = size * cell_size + (size - 1) * margin
board_left = (win_width - board_width) // 2
board_top = (win_height - board_width) // 2
font.init()
font2= font.SysFont('Arial', 36)
FPS = 60
game = True
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, x, y, width, height, color=None, image=None):
        super().__init__()
        if image:
            self.image = transform.scale(image.load(image), (width, height))
        else:
            self.image = Surface((width, height))
            if color:
                self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Tile(GameSprite):
    def __init__(self, value, row, col):
        x = BOARD_LEFT + col * (CELL_SIZE + MARGIN)
        y = BOARD_TOP + row * (CELL_SIZE + MARGIN)
        super().__init__(x, y, CELL_SIZE, CELL_SIZE)
        self.value = value
        self.update_color()

    def update_color(self):
        color = cell_colors.get(self.value, (60, 58, 50))
        self.image.fill(color)
        # Рисуем текст, если число не ноль
        if self.value != 0:
            text = font_small.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=(CELL_SIZE//2, CELL_SIZE//2))
            self.image.blit(text, text_rect)

    def set_value(self, new_value):
        self.value = new_value
        self.update_color()

class game2048:
    def __init__(self):

while game:
    for e.type in event.get():
        if e.type == QUIT:
            game = False
