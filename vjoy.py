import pygame
import sys
import math


pygame.init()

s
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
JOYSTICK_RADIUS = 50

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


def draw_joystick_knob(screen, pos):
    pygame.draw.circle(screen, RED, pos, JOYSTICK_RADIUS)


def constrain_point(point, rect):
    x = max(rect.left, min(point[0], rect.right))
    y = max(rect.top, min(point[1], rect.bottom))
    return x, y


def main():

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Virtual Joystick")


    joystick_area = pygame.Rect((SCREEN_WIDTH - JOYSTICK_RADIUS * 2) // 2,
                                (SCREEN_HEIGHT - JOYSTICK_RADIUS * 2) // 2,
                                JOYSTICK_RADIUS * 2, JOYSTICK_RADIUS * 2)


    joystick_pos = (joystick_area.centerx, joystick_area.centery)


    dragging = False


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and joystick_area.collidepoint(event.pos):
                    dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging = False

                    joystick_pos = (joystick_area.centerx, joystick_area.centery)
                    print("Joystick released. Centering...")
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    joystick_pos = constrain_point(event.pos, joystick_area)
               
                    dx = joystick_pos[0] - joystick_area.centerx
                    dy = joystick_pos[1] - joystick_area.centery
                    if dx == 0 and dy == 0:
                        direction = "Center"
                    else:
                        angle = math.atan2(-dy, dx)
                        direction = math.degrees(angle)
                        if direction < 0:
                            direction += 360
                        if direction < 45 or direction > 315:
                            direction = "Right"
                        elif 45 <= direction <= 135:
                            direction = "Up"
                        elif 135 < direction < 225:
                            direction = "Left"
                        else:
                            direction = "Down"
                    print("Joystick moved:", direction)

        screen.fill(WHITE)

        draw_joystick_knob(screen, joystick_pos)

        pygame.display.flip()

if __name__ == "__main__":
    main()
