import time,model,View,controller


while True:
    time.sleep(1/60)
    View.background()
    controller.controller()
    model.drive_rect()
