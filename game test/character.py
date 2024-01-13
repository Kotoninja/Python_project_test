from settings import *
import pygame


class Character:
    def __init__(self):
        self.length = 100  # length of cube
        self.x_char, self.y_char = 200, screenY - 2 * indentation

        # flag turn left or right
        self.left = False
        self.right = False
        self.velocity = 0  # add speed parameter

        self.weight = 10
        self.flag_box_contact = False    # with mannequin

        # text settings
        self.font_box = pygame.font.SysFont('arial', 40)
        # text speed
        self.text_box = self.font_box.render(f"{self.velocity}", True, 'black')
        self.pos_box = self.text_box.get_rect(center=(self.x_char + self.length // 2, self.y_char + self.length // 2))

    def draw_box(self):
        pygame.draw.rect(screen, 'black', [self.x_char, self.y_char, self.length, self.length], 6)
        screen.blit(self.text_box, self.pos_box)

    def move_flag(self, left, right):   # check movement player
        self.left = left
        self.right = right

    def movement(self):
        friction = 0.1    # friction coefficient
        if self.left:
            self.velocity -= 0.5  # move to left
        if self.right:
            self.velocity += 0.5  # move to right

        if not self.left and not self.right:
            if self.velocity > 0:
                self.velocity -= friction
            elif self.velocity < 0:
                self.velocity += friction

        self.velocity = round(self.velocity, 1)

        # new coordinate to check for screen collision
        new_x = self.x_char + self.velocity

        if 0 <= new_x <= coord_line_stop_x - self.length:
            self.x_char = new_x
        else:
            if new_x < 0:
                self.x_char = 0
                self.velocity -= self.velocity

            elif new_x > coord_line_stop_x - self.length:
                self.x_char = coord_line_stop_x - self.length
                self.velocity -= self.velocity

        # update text
        self.text_box = self.font_box.render(f"{self.velocity}", True, 'black')
        self.pos_box = self.text_box.get_rect(center=(self.x_char + self.length // 2, self.y_char + self.length // 2))

    def check_collision_mannequin(self, *coord_rect):
        if pygame.Rect([self.x_char, self.y_char, self.length, self.length]).colliderect(coord_rect):
            self.flag_box_contact = True
            self.x_char -= self.velocity + 1
            self.right = False
        else:
            self.flag_box_contact = False
