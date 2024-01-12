from settings import *
from character import *
from mannequin import *
from win_cube import *

pygame.init()

list_line = []
for x in range(0, screenX + degree_line_indentation, degree_line_indentation):
    list_line.append([[x, screenY - indentation], [x - degree_line_indentation, screenY]])


def all_init():
    box.__init__()
    box_man.__init__()
    win_box.__init__()
    # sound_sliding.stop()


def Win_text():
    font = pygame.font.SysFont('couriernew', 100)
    text = font.render(str('! YOU WIN !'), True, "green")
    screen.blit(text, (screenX // 2 - 250, 100))


if __name__ == "__main__":
    box = Character()
    box_man = Mannequin()
    win_box = Win_cube()
    while True:
        clock.tick(60)
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
                    all_init()
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    box.moveflag(False, False)

        box.check_box_mannequin(box_man.return_cords())
        box.movement()
        box.draw_box()

        # rendering line to stop the cube
        pygame.draw.line(screen, "grey", [coord_line_stop_x, 0], [coord_line_stop_x, y_coord_main_line], 4)

        box_man.pulse(box.weight, box.velocity, box.flag_box_contact)
        box_man.draw_box()
        win_box.draw()
        win_box.contact_with_mannequin(box_man.x_man, box_man.y_man)

        # surface rendering for cubes
        pygame.draw.line(screen, 'black', [0, screenY - indentation], [screenX, screenY - indentation], 5)

        for line in list_line:
            pygame.draw.line(screen, 'black', line[0], line[1], 5)

        if win_box.txt >= 90 and box_man.velocity_box_test == 0:
            Win_text()
        pygame.display.update()
