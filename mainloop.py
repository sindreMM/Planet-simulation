from main_py.planetsimulation import Window, AnimatedBody
import main_py.planetsimulation
import cv2
import sys


def loop(screen_size=None):
    win = Window("Simulation", screen_size)
    while True:
        if cv2.waitKey(1) + 0x00 == ord('q'):
            sys.exit()

        AnimatedBody.update_simulation(0.02)
        win.update_screen(AnimatedBody.bodies)
        AnimatedBody.update_bodies()
        win.show_screen()


AnimatedBody(50000, (0, 0), (900, 500), (0, 200, 255), size=40)
AnimatedBody(500, (0, 200), (300, 300), (120, 255, 0), size=11)
AnimatedBody(1000, (-200, -200), (1200, 500), (100, 120, 200), size=15)
AnimatedBody(20, (-250, 100), (800, 400), (0, 255, 0), size=3)
AnimatedBody(1000, (100, -100), (0, 500), (0, 255, 0), size=30)

loop()
