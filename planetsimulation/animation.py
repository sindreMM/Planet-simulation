import cv2
import numpy as np
from win32api import GetSystemMetrics
from main_py.planetsimulation.physics import Body


class AnimatedBody(Body):
    def __init__(self, mass, starting_speed, starting_position, color, size=11):
        super().__init__(mass, starting_speed, starting_position)
        self.color = color
        self.size = size


class Window:
    def __init__(self, name, size=None):
        self.name = name
        if size is None:
            self.screen = np.zeros((GetSystemMetrics(1), GetSystemMetrics(0), 3), np.uint8)
            cv2.namedWindow(name, cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty(name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        else:
            self.screen = np.zeros((size[1], size[0], 3), np.uint8)

    def erase_body(self, body):
        x = round(body.old_position[0])
        y = round(body.old_position[1])
        position = (x, y)
        print("erase at: ", position)
        self.screen = cv2.circle(self.screen, position, body.size, (0, 0, 0), -1)

    def draw_body(self, body):
        x = round(body.position[0])
        y = round(body.position[1])
        position = (x, y)
        print("draw at: ", position)
        self.screen = cv2.circle(self.screen, position, body.size, body.color, -1)

    def update_screen(self, bodies):
        for body in bodies:
            self.erase_body(body)
            self.draw_body(body)

    def show_screen(self):
        cv2.imshow(self.name, self.screen)


if __name__ == "__main__":
    class bod(object):
        pass
    i = bod()
    u = bod()
    i.position = (100, 100)
    u.position = (200, 200)
    win = Window("window")
    win.draw_body(i, (255, 0, 0))
    win.draw_body(u, (0, 0, 255))
    win.show_screen()
    while True:
        if cv2.waitKey() + 0x00 == ord('q'):
            break



