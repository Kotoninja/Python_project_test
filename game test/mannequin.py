from settings import *
import pygame


class BoxTest: # поменять название
    def __init__(self):
        self.wight = 100
        self.x_man, self.y_man = coord_line_stop_x - self.wight , screenY - 2 * indentation

        self.velocity_box_test = 0  # Добавляем параметр скорости
        self.weight = 5

        self.font_box_test = pygame.font.SysFont('arial', 40)
        self.text_box_test = self.font_box_test.render(f"{self.velocity_box_test}", True, 'red')
        self.pos_box_test = self.text_box_test.get_rect(center=(self.x_man + self.wight // 2, self.y_man + self.wight // 2))

    def draw_box(self):
        pygame.draw.rect(screen, 'red', [self.x_man, self.y_man, self.wight, self.wight], 6)
        screen.blit(self.text_box_test, self.pos_box_test)

    def pulse(self, box_weight, box_velocity, box_flag):
        if self.velocity_box_test > 0:
            self.velocity_box_test -= 0.1

        self.velocity_box_test = round(self.velocity_box_test, 1)

        if box_flag:
            self.velocity_box_test = box_velocity * box_weight / self.weight

        new_x = self.x_man + self.velocity_box_test
        if 0 <= new_x <= screenX - self.wight:
            self.x_man = new_x
        else:
            if new_x < 0:
                self.x_man = 0
                self.velocity_box_test -= self.velocity_box_test
            if new_x + self.wight > screenX:
                self.x_man = screenX - self.wight
                self.velocity_box_test -= self.velocity_box_test

        self.text_box_test = self.font_box_test.render(f"{self.velocity_box_test}", True, 'red')
        self.pos_box_test = self.text_box_test.get_rect(center=(self.x_man + self.wight // 2, self.y_man + self.wight // 2))

    def return_cords(self):
        return [self.x_man, self.y_man, self.wight, self.wight]