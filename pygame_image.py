import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False) #練習2
    bg_fl_img = pg.image.load("fig/pg_bg.jpg")
    bg_fl_img = pg.transform.flip(bg_fl_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    tmr = 0
    while True:
        fps = 200
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed() #キーの押下状態を取得
        if key_lst[pg.K_UP]:
            kk_rct.move_ip((0,-1))
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip((0,+1))
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip((+2,0))
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip((-1,0))
        kk_rct.move_ip((-1, 0)) #演習1
        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_fl_img, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(kk_img, kk_rct)
        # screen.blit(kk_img, [300, 200]) #練習4
        pg.display.update()
        tmr += 1        
        clock.tick(fps) #練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()