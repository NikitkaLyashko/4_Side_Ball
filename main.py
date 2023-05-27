import time,model,View,controller

import Controller2
import View2

while True:
    time.sleep(1/60)

    if model.slid=="menu":
        View2.background()
        Controller2.controller()

    if model.slid=="game":
        View.background()
        controller.controller()
        model.drive_rect()


