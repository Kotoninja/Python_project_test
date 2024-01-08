from settings import *

class Box:
    def __init__(self):
        self.wight = 100
        self.x_box, self.y_box = 200, screenY - 2 * indentation

        self.left = False
        self.right = False
        self.velocity = 0  # add speed parameter

        self.weight = 10
        self.flag_box_contact = False

        self.font_box = pygame.font.SysFont('arial', 40)
        self.text_box = self.font_box.render(f"{self.velocity}", True, 'black')
        self.pos_box = self.text_box.get_rect(center=(self.x_box + self.wight // 2, self.y_box + self.wight // 2))

    def draw_box(self):
        pygame.draw.rect(screen, 'black', [self.x_box, self.y_box, self.wight, self.wight], 6)
        screen.blit(self.text_box, self.pos_box)

    def moveflag(self, left, right):
        self.left = left
        self.right = right

    def movement(self):
        friction = 0.1
        if self.left:
            self.velocity -= 0.5  # - speed left
        if self.right:
            self.velocity += 0.5  # + speed right

        if not self.left and not self.right:
            if self.velocity > 0:
                self.velocity -= friction
            elif self.velocity < 0:
                self.velocity += friction

        self.velocity = round(self.velocity, 1)

        new_x = self.x_box + self.velocity

        if 0 <= new_x <= coord_line_stop_x - self.wight:
            self.x_box = new_x
        else:
            if new_x < 0:
                self.x_box = 0
                self.velocity -= self.velocity
            elif new_x > coord_line_stop_x - self.wight:
                self.x_box = coord_line_stop_x - self.wight
                self.velocity -= self.velocity

        self.text_box = self.font_box.render(f"{self.velocity}", True, 'black')
        self.pos_box = self.text_box.get_rect(center=(self.x_box + self.wight // 2, self.y_box + self.wight // 2))

    def check_box_test(self, *coord_rect):
        if pygame.Rect([self.x_box, self.y_box, self.wight, self.wight]).colliderect(coord_rect):
            self.flag_box_contact = True
            self.x_box -= self.velocity + 1
            self.right = False
        else:
            self.flag_box_contact = False

