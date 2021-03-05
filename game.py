from pathlib import Path
import sys, pygame



class Background(pygame.sprite.DirtySprite):
    def __init__(self, image_file,location):
        super().__init__()  #call Sprite initializer
        self.image = pygame.image.load(Path(__file__).parent / 'assests' / image_file)
        self.image = pygame.transform.scale(self.image, (800, 600))
        self.rect = self.image.get_rect()

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((800,600),0,32)

#fonts
font = pygame.font.SysFont('times new roman', 40)
font2 = pygame.font.SysFont('times new roman', 20)
font3 = pygame.font.SysFont('ariel', 20)
font4 = pygame.font.SysFont('ariel', 30)
font5 = pygame.font.SysFont('ariel', 40)
font6 = pygame.font.SysFont('times new roman', 15)

room1b = Background('room1b.jpg', [0,0])
stairs = Background('stairs.jpg', [0,0])
three_doors = Background('three doors.jpg', [0,0])
corridor_1 = Background('corridor1.jpg',[0,0])
pond = Background('pond.jpg',[0,0])

def draw_text(text,font,color,surface,x,y):
    textobj = font.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj,textrect)

def main_menu():
    while True:

        pygame.display.flip()
        screen.fill((0,0,0))
        draw_text('Welcome to the Hunt',font, (255,255,255), screen,210,50)

        mx, my = pygame.mouse.get_pos()

        startbutton_1 = pygame.Rect(300,350,150,50)

        if startbutton_1.collidepoint((mx,my)):
            if click:
                story()
        
        pygame.draw.rect(screen, (255,255,255), startbutton_1)

        draw_text('Start Story',font2, (0,0,0), screen,330,360)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def story():
    running = True
    click = False

    while running:

        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()
        
        draw_text('Wake Up...',font3, (255,0,0), screen,340,250)

        startbutton_2 = pygame.Rect(300,400,150,50)

        if startbutton_2.collidepoint((mx,my)):
            if click:
                story1()

        pygame.draw.rect(screen, (255,255,255), startbutton_2)

        draw_text('Continue',font2, (0,0,0), screen,335,410)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)  

def story1():
    running = True
    click = False

    while running:
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()
        
        draw_text('Wake Up...',font4, (255,0,0), screen,320,210)

        startbutton_3 = pygame.Rect(300,400,150,50)

        if startbutton_3.collidepoint((mx,my)):
            if click:
                story2()

        pygame.draw.rect(screen, (255,255,255), startbutton_3)

        draw_text('Continue',font2, (0,0,0), screen,335,410)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)  

def story2():
    running = True
    click = False

    while running:
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()
        
        draw_text('Wake Up!',font5, (255,0,0), screen,320,210)

        startbutton_4 = pygame.Rect(300,400,150,50)

        if startbutton_4.collidepoint((mx,my)):
            if click:
                room_1()

        pygame.draw.rect(screen, (255,255,255), startbutton_4)

        draw_text('Continue',font2, (0,0,0), screen,335,410)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def room_1():
    running = True
    click = False

    while running:

        pygame.display.flip()
        screen.blit(room1b.image, room1b.rect)

        mx, my = pygame.mouse.get_pos()
        
        draw_text("You open your eyes. With no memory of what has happened you find youself stuck in this closet.",font2, (255,255,255), screen,10,110)
        draw_text("What do you want to do next?",font2, (255,255,255), screen,280,150)

        room_1_button = pygame.Rect(100,400,150,50)
        room_1_button2 = pygame.Rect(500,400,150,50)

        if room_1_button.collidepoint((mx,my)):
            if click:
                room_1_2()
        
        if room_1_button2.collidepoint((mx,my)):
            if click:
                gameover()

        pygame.draw.rect(screen, (255,255,255), room_1_button)
        pygame.draw.rect(screen, (255,255,255), room_1_button2)

        draw_text('Break Out',font2, (0,0,0), screen,120,410)
        draw_text('Give Up',font2, (0,0,0), screen,535,410)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def room_1_2():
    running = True
    click = False

    while running:

        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()
        
        draw_text("You break out but in the process you make a large noise",font2, (255,255,255), screen,160,110)

        con_room_1_button = pygame.Rect(300,400,150,50)

        if con_room_1_button.collidepoint((mx,my)):
            if click:
                room_1_3()
        

        pygame.draw.rect(screen, (255,255,255), con_room_1_button)

        draw_text('Continue',font2, (0,0,0), screen,335,410)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def room_1_3():
    running = True
    click = False

    while running:
        
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()
        
        draw_text("You're finally awake? Better run I'm coming...",font5, (255,0,0), screen,120,110)
        draw_text("You hear the voice speak, you must do something before they get there",font2, (255,255,255), screen,120,240)

        con_room_1_button2 = pygame.Rect(100,400,150,50)
        con_room_1_button3 = pygame.Rect(500,400,150,50)

        if con_room_1_button2.collidepoint((mx,my)):
            if click:
                hide1()
        
        if con_room_1_button3.collidepoint((mx,my)):
            if click:
                stairs1()

        pygame.draw.rect(screen, (255,255,255), con_room_1_button2)
        pygame.draw.rect(screen, (255,255,255), con_room_1_button3)

        draw_text('Hide',font2, (0,0,0), screen,145,410)
        draw_text('Stairs',font2, (0,0,0), screen,545,410)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def hide1():

    running = True
    click = False

    while running:
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()
        
        draw_text('You look around for a place to hide... but there are none',font2, (255,255,255), screen,125,210)

        hide1_button = pygame.Rect(300,400,150,50)

        if hide1_button.collidepoint((mx,my)):
            if click:
                hide2()

        pygame.draw.rect(screen, (255,255,255), hide1_button)

        draw_text('Continue',font2, (0,0,0), screen,335,410)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)  

def hide2():

    running = True
    click = False

    while running:
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()
        
        draw_text('STOMP STOMP STOMP',font4, (255,0,0), screen,250,150)

        hide1_button = pygame.Rect(300,400,150,50)

        if hide1_button.collidepoint((mx,my)):
            if click:
                hide3()

        pygame.draw.rect(screen, (255,255,255), hide1_button)

        draw_text('Continue',font2, (0,0,0), screen,335,410)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)  

def hide3():

    running = True
    click = False

    while running:
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()
        
        draw_text('Found you',font4, (255,0,0), screen,320,175)

        hide1_button = pygame.Rect(300,400,150,50)

        if hide1_button.collidepoint((mx,my)):
            if click:
                gameover()

        pygame.draw.rect(screen, (255,255,255), hide1_button)

        draw_text('Continue',font2, (0,0,0), screen,335,410)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)  

def stairs1():

    running = True
    click = False

    while running:
        
        pygame.display.flip()
        screen.blit(stairs.image, stairs.rect)

        mx, my = pygame.mouse.get_pos()
        
        draw_text('You quicky go down the stairs',font2, (255,255,255), screen,270,80)

        hide1_button = pygame.Rect(300,400,150,50)

        if hide1_button.collidepoint((mx,my)):
            if click:
                stairs2()

        pygame.draw.rect(screen, (255,255,255), hide1_button)

        draw_text('Continue',font2, (0,0,0), screen,335,410)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)  

def stairs2():

    running = True
    click = False

    while running:
        
        pygame.display.flip()
        screen.blit(three_doors.image, three_doors.rect)

        mx, my = pygame.mouse.get_pos()
        
        draw_text('You find yourself in front of three doors',font2, (255,255,255), screen,230,20)
        draw_text('Which door will you take?',font2, (255,255,255), screen,270,50)

        room_a_button = pygame.Rect(130,420,150,50)
        room_b_button = pygame.Rect(330,420,150,50)
        room_c_button = pygame.Rect(530,420,150,50)

        if room_a_button.collidepoint((mx,my)):
            if click:
                room_a()
        if room_b_button.collidepoint((mx,my)):
            if click:
                room_b()
        if room_c_button.collidepoint((mx,my)):
            if click:
                room_c()

        pygame.draw.rect(screen, (255,255,255), room_a_button)
        pygame.draw.rect(screen, (255,255,255), room_b_button)
        pygame.draw.rect(screen, (255,255,255), room_c_button)

        draw_text('Door 1',font2, (0,0,0), screen,170,430)
        draw_text('Door 2',font2, (0,0,0), screen,370,430)
        draw_text('Door 3',font2, (0,0,0), screen,570,430)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)  

def room_a():

    running = True
    click = False

    while running:

        pygame.display.flip()
        screen.blit(corridor_1.image, corridor_1.rect)

        mx, my = pygame.mouse.get_pos()
        
        draw_text('You open the door and quickly head inside.',font2, (255,255,255), screen,210,120)
        draw_text('It is dark but you must keep going.',font2, (255,255,255), screen,240,160)

        pond_button = pygame.Rect(300,400,150,50)

        if pond_button.collidepoint((mx,my)):
            if click:
                pond_1()

        pygame.draw.rect(screen, (255,255,255), pond_button)

        draw_text('Continue',font2, (0,0,0), screen,335,410)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)  

def pond_1():

    running = True
    click = False

    while running:

        pygame.display.flip()
        screen.blit(pond.image, pond.rect)

        mx, my = pygame.mouse.get_pos()
        
        draw_text('You find yourself in a sea cavern.',font2, (255,255,255), screen,330,120)
        draw_text('Will you climb the vines or keep going forard?',font2, (255,255,255), screen,280,160)

        pond_button = pygame.Rect(300,400,150,50)

        vines_button = pygame.Rect(130,420,150,50)
        forward_button = pygame.Rect(330,420,150,50)

        if vines_button.collidepoint((mx,my)):
            if click:
                vines()
        if forward_button.collidepoint((mx,my)):
            if click:
                cave()

        pygame.draw.rect(screen, (255,255,255), vines_button)
        pygame.draw.rect(screen, (255,255,255), forward_button)

        draw_text('Door 1',font2, (0,0,0), screen,170,430)
        draw_text('Door 2',font2, (0,0,0), screen,370,430)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)  

def vines():
    running = True
    click = False

    while running:
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()
        
        draw_text('You start climbing until you hear something below you',font2, (255,255,255), screen,170,150)

        vines2_button = pygame.Rect(300,400,150,50)

        if vines2_button.collidepoint((mx,my)):
            if click:
                vines2()

        pygame.draw.rect(screen, (255,255,255), vines2_button)

        draw_text('Continue',font2, (0,0,0), screen,335,410)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def vines2():
    running = True
    click = False

    while running:
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()
        
        draw_text("It's not that easy",font5, (255,0,0), screen,260,150)

        hide1_button = pygame.Rect(300,400,150,50)

        if hide1_button.collidepoint((mx,my)):
            if click:
                gameover()

        pygame.draw.rect(screen, (255,255,255), hide1_button)

        draw_text('Continue',font2, (0,0,0), screen,335,410)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60) 

def cave():
    running = True
    click = False

    while running:

        pygame.display.flip()
        screen.blit(chest.image, chest.rect)

        mx, my = pygame.mouse.get_pos()
        
        draw_text('You open the door and quickly head inside.',font2, (255,255,255), screen,210,120)
        draw_text('It is dark but you must keep going.',font2, (255,255,255), screen,240,160)

        pond_button = pygame.Rect(300,400,150,50)

        if pond_button.collidepoint((mx,my)):
            if click:
                pond_1()

        pygame.draw.rect(screen, (255,255,255), pond_button)

        draw_text('Continue',font2, (0,0,0), screen,335,410)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)  

def room_b():
    running = True
    click = False

    while running:
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()
        
        draw_text('Bad Choice',font5, (255,0,0), screen,300,250)

        hide1_button = pygame.Rect(300,400,150,50)

        if hide1_button.collidepoint((mx,my)):
            if click:
                gameover()

        pygame.draw.rect(screen, (255,255,255), hide1_button)

        draw_text('Continue',font2, (0,0,0), screen,335,410)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)  

def room_c():
    pass


def room_2():
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text('Free Play',font, (255,255,255), screen,300,50)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
        pygame.display.update()
        mainClock.tick(60)  

def room_3():
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text('Options',font, (255,255,255), screen,300,50)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
        pygame.display.update()
        mainClock.tick(60)  

def gameover():
    running = True
    click = False

    while running:
        
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()
        
        draw_text("Game over",font, (255,0,0), screen,280,100)

        gameover_button = pygame.Rect(300,400,150,50)

        if gameover_button.collidepoint((mx,my)):
            if click:
                main_menu()

        pygame.draw.rect(screen, (255,255,255), gameover_button)

        draw_text('Start Over',font2, (0,0,0), screen,330,410)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

main_menu()