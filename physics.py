import pygame

pygame.init()

screenX, screenY = 1920, 800
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
indentation = 100
degree_line_indentation = 40

list_line = []
for x in range(0, screenX + degree_line_indentation, degree_line_indentation):
    list_line.append([[x, screenY - indentation], [x - 40, screenY]])


class Box:
    def __init__(self):
        self.wight = 100
        self.x, self.y = 200, screenY - 2 * indentation

        self.left = False
        self.right = False
        self.velocity = 0  # Добавляем параметр скорости

        self.weight = 10
        self.flag_box_contact = False

        self.font_box = pygame.font.SysFont('arial', 40)
        self.text_box = self.font_box.render(f"{self.velocity}", True, 'black')
        self.pos_box = self.text_box.get_rect(center=(self.x + self.wight // 2, self.y + self.wight // 2))

    def draw_box(self):
        pygame.draw.rect(screen, 'black', [self.x, self.y, self.wight, self.wight], 6)
        screen.blit(self.text_box, self.pos_box)

    def moveflag(self, left, right):
        self.left = left
        self.right = right

    def movement(self):
        # print(self.velocity)
        friction = 0.1  # Коэффициент трения
        if self.left:
            self.velocity -= 0.1  # Увеличиваем скорость влево
        if self.right:
            self.velocity += 0.1  # Увеличиваем скорость вправо

        # Применяем трение
        if not self.left and not self.right:
            if self.velocity > 0:
                self.velocity -= friction
            elif self.velocity < 0:
                self.velocity += friction
        self.velocity = round(self.velocity, 1)

        new_x = self.x + self.velocity

        if 0 <= new_x <= screenX - self.wight:
            self.x = new_x
        else:
            # Если выходит за границы, корректируем позицию, чтобы кубик остался в пределах экрана
            if new_x < 0:
                self.x = 0
                self.velocity -= self.velocity
            elif new_x > screenX - self.wight:
                self.x = screenX - self.wight
                self.velocity -= self.velocity

        self.text_box = self.font_box.render(f"{self.velocity}", True, 'black')
        self.pos_box = self.text_box.get_rect(center=(self.x + self.wight // 2, self.y + self.wight // 2))

    def check_box_test(self, *coord_rect):
        if pygame.Rect([self.x, self.y, self.wight, self.wight]).colliderect(coord_rect):
            self.flag_box_contact = True
            self.x -= self.velocity + 1
            self.right = False
        else:
            self.flag_box_contact = False
        # print(self.flag_box_contact)


class BoxTest:
    def __init__(self):
        self.wight = 100
        self.x, self.y = 400, screenY - 2 * indentation

        self.velocity_box_test = 0  # Добавляем параметр скорости
        self.weight = 10

        self.font_box_test = pygame.font.SysFont('arial', 40)
        self.text_box_test = self.font_box_test.render(f"{self.velocity_box_test}", True, 'red')
        self.pos_box_test = self.text_box_test.get_rect(center=(self.x + self.wight // 2, self.y + self.wight // 2))

    def draw_box(self):
        pygame.draw.rect(screen, 'red', [self.x, self.y, self.wight, self.wight], 6)
        screen.blit(self.text_box_test, self.pos_box_test)

    def pulse(self, box_weight, box_velocity, box_flag):
        if self.velocity_box_test > 0:
            self.velocity_box_test -= 1

        self.velocity_box_test = round(self.velocity_box_test, 1)

        if box_flag:
            self.velocity_box_test = box_velocity * box_weight / self.weight
        self.x += self.velocity_box_test  # Применяем скорость к позиции куба

        self.text_box_test = self.font_box_test.render(f"{self.velocity_box_test}", True, 'red')
        self.pos_box_test = self.text_box_test.get_rect(center=(self.x + self.wight // 2, self.y + self.wight // 2))

    def return_cords(self):
        return [self.x, self.y, self.wight, self.wight]


if __name__ == "__main__":
    box = Box()
    box_test = BoxTest()
    while True:
        clock.tick(20)
        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    box.moveflag(True, False)
                if event.key == pygame.K_RIGHT:
                    box.moveflag(False, True)
                if event.key == pygame.K_F2:
                    box.__init__()
                    box_test.__init__()
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    box.moveflag(False, False)

        box_test.pulse(box.weight, box.velocity, box.flag_box_contact)
        box_test.draw_box()
        box.check_box_test(box_test.return_cords())
        box.movement()
        box.draw_box()
        pygame.draw.line(screen, 'black', [0, screenY - indentation], [screenX, screenY - indentation], 5)

        for line in list_line:
            pygame.draw.line(screen, 'black', line[0], line[1], 5)

        pygame.display.update()
