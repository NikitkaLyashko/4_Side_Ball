import pygame

rect_ball=pygame.Rect(300, 300, 70, 70)

rect_plat=pygame.Rect(0,770,800,30)


octaloc_ottalk=5
polojenie_pl="down"
px_y=3
px_x=-5
oct_live=3
slid="menu"


def drive_rect():
    global px_y, px_x, octaloc_ottalk, oct_live,slid

    rect_ball.left+=px_x
    rect_ball.bottom+=px_y

    if rect_ball.bottom>=800:
        rect_ball.bottom=800
        px_y=-px_y
        octaloc_ottalk_def()
        oct_live-=1



    if rect_ball.top<=0:
        rect_ball.top=0
        px_y=-px_y
        octaloc_ottalk_def()
        oct_live -= 1


    if rect_ball.left<=0:
        rect_ball.left=0
        px_x=-px_x
        octaloc_ottalk_def()
        oct_live -= 1


    if rect_ball.right>=800:
        rect_ball.right=800
        px_x=-px_x
        octaloc_ottalk_def()
        oct_live -= 1

    if oct_live<=0:
        oct_live=3
        slid="menu"



    otbitie()
def otbitie():
    global px_y, px_x,polojenie_pl,octaloc_ottalk
    if rect_ball.left<=rect_plat.right and polojenie_pl=="left":
        rect_ball.left=rect_plat.right
        px_x = -px_x
        octaloc_ottalk_def()



    if rect_ball.right>=rect_plat.left and polojenie_pl=="right":
        rect_ball.right=rect_plat.left
        px_x =-px_x
        octaloc_ottalk_def()


    if rect_ball.top<=rect_plat.bottom and polojenie_pl=="top":
        rect_ball.top=rect_plat.bottom
        px_y =-px_y
        octaloc_ottalk_def()


    if rect_ball.bottom>=rect_plat.top and polojenie_pl=="down":
        rect_ball.bottom=rect_plat.top
        px_y =-px_y
        octaloc_ottalk_def()

# px_y=3
# px_x=-5
znak_x=1
znak_y=1

def octaloc_ottalk_def():
    global octaloc_ottalk,px_x,px_y
    octaloc_ottalk -= 1
    if octaloc_ottalk <= 0:
        octaloc_ottalk = 5
        print(px_x, px_y)


        if px_x>0:
            px_x+=znak_x
        if px_x<0:
            px_x-=znak_x


        if px_y>0:
            px_y+=znak_y
        if px_y<0:
            px_y-=znak_y


def platforma_right():
    global  rect_plat, polojenie_pl
    rect_plat.width=30
    rect_plat.height=800
    rect_plat.top=0
    rect_plat.right=800
    polojenie_pl="right"


def platforma_top():
    global  rect_plat,polojenie_pl
    rect_plat.width=800
    rect_plat.height=30
    rect_plat.top=0
    rect_plat.left=0
    polojenie_pl="top"

def platforma_left():
    global  rect_plat,polojenie_pl
    rect_plat.width=30
    rect_plat.height=800
    rect_plat.top=0
    rect_plat.left=0
    polojenie_pl="left"

def platforma_down():
    global  rect_plat,polojenie_pl
    rect_plat.width=800
    rect_plat.height=30
    rect_plat.top=770
    rect_plat.left=0
    polojenie_pl="down"

