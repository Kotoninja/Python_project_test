from settings import *
import pygame,random,math
class Win_cube:
    def __init__(self):
        self.length = 100
        self.color = "green"
        self.x_win = random.randint(450, screenX - self.length)
        self.y_win = screenY - 2 * indentation

        # text settings
        self.size = 30
        self.color_difference = 255 / self.length
        self.color_txt=(255,0,0)
        self.font = pygame.font.SysFont('couriernew', self.size)
        self.text = 0


    def draw(self):
        self.text = self.font.render(f"{self.text}% ", True, self.color_txt)     # update text
        pygame.draw.rect(screen, self.color, [self.x_win, self.y_win, self.length, self.length], 6)
        screen.blit(self.text, (self.x_win + self.size // 2 + 15, self.y_win - self.size))

    def contact_with_mannequin(self, x_man):
        # copying mannequin coordinates
        pos1=x_man
        pos2=x_man + self.length
        percent=0   # variable for percent

        if self.x_win < pos1 < self.x_win + self.length:
            percent = 100 - ((self.x_win - pos1) * -1)
            self.color_txt = (255 - (self.color_difference * percent), 0 + (self.color_difference * percent),0)

        if self.x_win < pos2 < self.x_win + self.length:
            percent = pos2 - self.x_win
            self.color_txt = (255 - (self.color_difference * percent), 0 + (self.color_difference * percent), 0)

        self.text = int(math.fabs(percent))
