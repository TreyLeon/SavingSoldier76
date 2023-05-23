from multiprocessing.context import SpawnContext
from sre_constants import MIN_REPEAT
from time import time
from tkinter import Menu
from tracemalloc import stop
from turtle import position, tracer
import pygame
import random
import time
from sys import exit
pygame.init()
pygame.mixer.init
seconds = round(pygame.time.get_ticks()/1000)
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Saving soldier76") 
pygame.display.set_icon(pygame.image.load("icon.png"))
clock = pygame.time.Clock()

#background and music

background = pygame.image.load("graphics/background.png").convert_alpha()
background2 = pygame.image.load("graphics/loading_screen.png").convert_alpha()
background3 = pygame.image.load("graphics/winstoncall.jpg").convert()
background4 = pygame.image.load("graphics/end.jpg").convert()
display = 0
theme = pygame.mixer.Sound("audio/theme.wav")
res_audio = pygame.mixer.Sound("audio/res.wav")
intro = pygame.mixer.Sound("audio/intro.wav")
call = pygame.mixer.Sound("audio/call.wav")
morrison = pygame.mixer.Sound("audio/morrison.wav")
lena =pygame.mixer.Sound("audio/tracer.wav")
phara = pygame.mixer.Sound("audio/phara.wav")
widow = pygame.mixer.Sound("audio/widow.wav")
end = pygame.mixer.Sound("audio/end.wav")

#Cards and buttons

jackcard_surface = pygame.image.load("graphics/soldier/jackcard.jpg").convert_alpha()
jackcard_rectangle = jackcard_surface.get_rect(midbottom=(100,280))
tracercard_surface = pygame.image.load("graphics/tracer/tracercard.jpg").convert_alpha()
tracercard_rectangle = tracercard_surface.get_rect(midbottom=(250,280))
pharacard_surface = pygame.image.load("graphics/phara/pharacard.jpg").convert_alpha()
pharacard_rectangle = pharacard_surface.get_rect(midbottom=(550,280))
widowcard_surface = pygame.image.load("graphics/widow/widowcard.jpg").convert_alpha()
widowcard_rectangle = widowcard_surface.get_rect(midbottom=(700,280))
back_surface = pygame.image.load("graphics/backbutton.png").convert_alpha()
back_rectangle = back_surface.get_rect(midbottom=(370,390))
call_surface = pygame.image.load("graphics/callbutton.png").convert_alpha()
call_rectangle = back_surface.get_rect(midbottom=(430,390))

#text

menu_font = pygame.font.Font("font/overwatch.ttf", 30)
game_font = pygame.font.Font("font/overwatch.ttf", 40)
title_font = pygame.font.Font("font/overwatch.ttf", 50)
titletext_surface = title_font.render("Saving Soldier 76", False, "White")
titletext_rectangle = titletext_surface.get_rect(topleft =(25,25))
menu1text1_surface = menu_font.render("Play", False, "White")
menu1text1_rectangle = menu1text1_surface.get_rect(topleft =(25,115))
menu1text2_surface = menu_font.render("Hero Backstory", False, "White")
menu1text2_rectangle = menu1text2_surface.get_rect(topleft =(25,155))

gametext_surface = game_font.render(" ",False, "White")
gametext_rectangle = gametext_surface.get_rect(center =(400,200))

#jack Morrison

life = pygame.image.load("graphics/soldier/lifes.png").convert_alpha()
lifes = 3
player_surface = pygame.image.load("graphics/soldier/76.png").convert_alpha()
player_y_position = 390
player_x_position= 750
player_rectangle = player_surface.get_rect(midbottom =(player_x_position,player_y_position))
killer = 9
res = False
res_cd = 0
player_gravity = 0
player_x_movement = 0
sight = True

#Lena Oxton

tracer_surface = pygame.image.load("graphics/tracer/tracer2.png").convert_alpha()
tracer_x_position = 650
tracer_rectangle = tracer_surface.get_rect(midbottom =(tracer_x_position,378))
core = True
Tracer_Secs = 0

#Fareha Amari

phara_surface = pygame.image.load("graphics/phara/phara.png").convert_alpha()
phara_x_position = 70
phara_y_position = 115
phara_rectangle = phara_surface.get_rect(midbottom =(phara_x_position,phara_y_position))

#Amelie Lacroix

widow_surface = pygame.image.load("graphics/widow/widow.png").convert_alpha()
widow_x_position = 30
widow_rectangle = widow_surface.get_rect(midbottom =(widow_x_position,210))
power = 0

#Font

test_font = pygame.font.Font("font/overwatch.ttf", 25)

#Initial Screen

while True:
    if display == 0:
        screen.blit(background2,(0,0))
        intro.play()
        morrison.stop()
        lena.stop()
        phara.stop()
        widow.stop()
        screen.blit(titletext_surface,titletext_rectangle)
        screen.blit(menu1text1_surface,menu1text1_rectangle)
        screen.blit(menu1text2_surface,menu1text2_rectangle)
    elif display == 1:
        screen.blit (background3,(0,0))
        intro.stop()
        screen.blit(call_surface, call_rectangle)
        screen.blit(jackcard_surface, jackcard_rectangle)
        screen.blit(tracercard_surface,tracercard_rectangle)
        screen.blit(pharacard_surface,pharacard_rectangle)
        screen.blit(widowcard_surface,widowcard_rectangle)
        screen.blit(back_surface,back_rectangle)
    elif display == 4:
        end.play()
        time.sleep(end.get_length())
        pygame.quit()
        exit()
    else:
    
    #Game Screen
        #Timings
    
        seconds = round(pygame.time.get_ticks()/1000)

        #renew background, start music and lifes
        
        display = 3
        theme.play()
        intro.stop()
        pygame.mouse.set_cursor(*pygame.cursors.broken_x)
        screen.blit(background,(0,0))
        if lifes == 3:
            screen.blit(life,(750,10))
            screen.blit(life,(700,10))
            screen.blit(life,(650,10))
            if seconds >= 60:
                display = 4
                screen.blit(background4,(0,0))
                widow_x_position = -100
                player_x_position = -100
                tracer_x_position = -100
                phara_x_position = -100
                theme.stop()
        elif lifes == 2:
            screen.blit(life,(750,10))
            screen.blit(life,(700,10))
        elif lifes == 1:
            screen.blit(life,(750,10))
        if lifes == 0: 
            player_surface = pygame.image.load("graphics/soldier/76rip.png").convert_alpha()
            widow_x_position = -100
            tracer_x_position = -100
            phara_x_position = -100
            theme.stop()
        if lifes <= 0: player_x_movement = 0
    
        #Player ingame
    
        player_gravity += 1
        player_y_position += player_gravity
        if player_y_position >= 390: player_y_position= 390
        player_rectangle = player_surface.get_rect(midbottom =(player_x_position,player_y_position))
        screen.blit(player_surface,player_rectangle)
        if res == True: res_cd += 0.02
        if res_cd >= 1.02:
            res = False
            res_cd = 0
        if res == False: player_surface = pygame.image.load("graphics/soldier/76.png").convert_alpha()
        if res == True: 
            pygame.mixer.Channel(1).play(res_audio)
            player_surface = pygame.image.load("graphics/soldier/76res.png").convert_alpha()
        if sight == False: player_surface = pygame.image.load("graphics/soldier/76r.png").convert_alpha()
        player_x_position += player_x_movement
    
        #Lena Oxton ingame
    
        tracer_rectangle = tracer_surface.get_rect(midbottom =(tracer_x_position,378))
        screen.blit(tracer_surface,tracer_rectangle)
        Tracer_Secs += 0.08
        if Tracer_Secs >= 3 and Tracer_Secs < 3.08 : tracer_x_position = random.randint(20, 730)  
        if Tracer_Secs >= 5 and Tracer_Secs < 6:
            tracer_surface = pygame.image.load("graphics/tracer/tracer1.png").convert_alpha()
            core = False
            Tracer_Secs = 0
        if Tracer_Secs > 3: 
            tracer_surface = pygame.image.load("graphics/tracer/tracer2.png").convert_alpha() 
            core = True
        if  tracer_rectangle.collidepoint(player_rectangle.center) and core == False and res == False and  lifes != 0:
            lifes -= 1
            Tracer_Secs = 0
            if lifes >= 0:
                killer = 2
            if lifes > 0: 
                res = True

        #Fareha Amari ingame

        phara_rectangle = phara_surface.get_rect(midbottom =(phara_x_position,phara_y_position))
        screen.blit(phara_surface,phara_rectangle)
        phara_x_position += 8.5 
        if phara_x_position > 800:
            phara_x_position = 20
            phara_y_position = 115
        if phara_x_position >= 300 and phara_y_position != 215: phara_y_position += 12.5 
        if phara_rectangle.collidepoint(player_rectangle.center) and res == False and  lifes != 0 :
            lifes -= 1
            phara_x_position = 20
            phara_y_position = 115
            if lifes >= 0:
                killer = 1
            if lifes > 0:
                res = True

        #Amelie Lacroix ingame
    
        widow_rectangle = widow_surface.get_rect(midbottom =(widow_x_position,210))
        screen.blit(widow_surface,widow_rectangle)
        if widow_x_position != 30: widow_x_position += 2.5
        if widow_x_position == 30: power += 0.175
        if power >=80: widow_surface = pygame.image.load("graphics/widow/widow2.png").convert_alpha()
        if power >= 100 and widow_x_position == 30 and res == False and  lifes != 0:
            lifes -= 1
            power = 0
            widow_surface = pygame.image.load("graphics/widow/widow.png").convert_alpha()
            if lifes >= 0:
                killer = 0
            if lifes > 0:
                res = True

        #Game text

        if lifes <= 0 and killer == 0:
            screen.blit(gametext_surface,gametext_rectangle)
            gametext_surface = test_font.render("La punteria de Widow es perfecta, aturdela para que no te dispare", False, "Red")
            gametext_rectangle = gametext_surface.get_rect(center =(400,30))
        if lifes <= 0 and killer == 1:
            screen.blit(gametext_surface,gametext_rectangle)
            gametext_surface = test_font.render("Phara esta reposicionandose, ten cuidado de no golpearla en el aire o ambos morireis", False, "Red")
            gametext_rectangle = gametext_surface.get_rect(center =(400,30))
        if lifes <= 0 and killer == 2:
            screen.blit(gametext_surface,gametext_rectangle)
            gametext_surface = test_font.render("si chocas con Tracer, el nucleo de su pecho explotara y moriras", False, "Red")
            gametext_rectangle = gametext_surface.get_rect(center =(400,30))
    #Events
    
    for event in pygame.event.get():

        #Exit

        if event.type == pygame.QUIT: 
            pygame.quit() 
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and lifes == 0:
            pygame.quit() 
            exit()
        
        #Shoot and menu selecting

        if event.type == pygame.MOUSEBUTTONDOWN:
            if phara_rectangle.collidepoint(pygame.mouse.get_pos()):
                phara_x_position = 20  
                phara_y_position = 115
            if widow_rectangle.collidepoint(pygame.mouse.get_pos()):
                widow_surface = pygame.image.load("graphics/widow/widow.png").convert_alpha()
                widow_x_position = -75
                power = 0
            if menu1text1_rectangle.collidepoint(pygame.mouse.get_pos()) and display == 0:
                display = 3
                theme.play()
                theme.set_volume(0.125)
                lifes = 3
                intro.stop()
            if menu1text2_rectangle.collidepoint(pygame.mouse.get_pos()) and display == 0:
                display = 1
                intro.stop()
            if back_rectangle.collidepoint(pygame.mouse.get_pos()) and display == 1:
                display = 0
                call.stop()
                morrison.stop()
                lena.stop()
                phara.stop()
                widow.stop()
            if call_rectangle.collidepoint(pygame.mouse.get_pos()) and display == 1:
                call.play()
                morrison.stop()
                lena.stop()
                phara.stop()
                widow.stop()
            if jackcard_rectangle.collidepoint(pygame.mouse.get_pos()) and display == 1:
                morrison.play()
                lena.stop()
                phara.stop()
                widow.stop()
                call.stop()
            if tracercard_rectangle.collidepoint(pygame.mouse.get_pos()) and display == 1:
                lena.play()
                morrison.stop()
                phara.stop()
                widow.stop()
                call.stop()
            if pharacard_rectangle.collidepoint(pygame.mouse.get_pos()) and display == 1:
                phara.play()
                morrison.stop()
                lena.stop()
                widow.stop()
                call.stop()
            if widowcard_rectangle.collidepoint(pygame.mouse.get_pos()) and display == 1:
                widow.play()
                morrison.stop()
                lena.stop()
                phara.stop()
                call.stop()

        
        #Movement

        if event.type == pygame.KEYDOWN and lifes != 0:
            if event.key == pygame.K_SPACE and player_y_position == 390: player_gravity = -22.5
            if event.key == pygame.K_a:
                player_surface = pygame.image.load("graphics/soldier/76r.png").convert_alpha()
                player_x_movement = -5
                if player_x_position < 0:
                    player_x_position = 800
                sight = True
            if event.key == pygame.K_d:
                player_surface = pygame.image.load("graphics/soldier/76.png").convert_alpha()
                player_x_movement = 5
                if player_x_position > 800:
                    player_x_position = 0
                sight = False
        if event.type == pygame.KEYUP and lifes != 0:
            if event.key == pygame.K_a:
                player_x_movement = 0
            if event.key == pygame.K_d:
                player_x_movement = 0

    pygame.display.update()
    clock.tick(60)