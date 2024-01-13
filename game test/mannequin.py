from settings import *
import pygame


class Mannequin:
    def __init__(self):
        self.length = 100
        self.x_man, self.y_man = coord_line_stop_x - self.length, screenY - 2 * indentation

        self.velocity_man = 0  # add speed parameter
        self.weight = 5

        # text settings
        self.font_box_test = pygame.font.SysFont('arial', 40)
        # text velocity
        self.text_box_test = self.font_box_test.render(f"{self.velocity_man}", True, 'red')
        self.pos_box_test = self.text_box_test.get_rect(center=(self.x_man + self.length // 2, self.y_man + self.length // 2))

    def draw_box(self):
        pygame.draw.rect(screen, 'red', [self.x_man, self.y_man, self.length, self.length], 6)
        screen.blit(self.text_box_test, self.pos_box_test)

    def pulse(self, box_weight, box_velocity, box_flag):
        if self.velocity_man > 0:   # reduce speed
            self.velocity_man -= 0.1

        self.velocity_man = round(self.velocity_man, 1)

        if box_flag:
            self.velocity_man = (box_velocity * box_weight
                                 / self.weight)
            # sound_sliding.play(fade_ms=500)

        new_x = self.x_man + self.velocity_man
        if 0 <= new_x <= screenX - self.length:
            self.x_man = new_x
        else:
            if new_x < 0:
                self.x_man = 0
                self.velocity_man -= self.velocity_man

            if new_x + self.length > screenX:
                self.x_man = screenX - self.length
                self.velocity_man -= self.velocity_man

        # update text
        self.text_box_test = self.font_box_test.render(f"{self.velocity_man}", True, 'red')
        self.pos_box_test = self.text_box_test.get_rect(center=(self.x_man + self.length // 2, self.y_man + self.length // 2))

    def return_cords(self):
        return [self.x_man, self.y_man, self.length, self.length]