import pygame, sys
from pygame.locals import *
import webbrowser

link_color = (0,0,255)


pygame.init()

#font
font = pygame.font.SysFont('Agency fb', 23)
font1 = pygame.font.SysFont('algerian', 50)

#Headings
heading = "Software Sorcerers"
#names
bayot = "Khent Ryan Jay Bayot"
aribal = "Christian Aribal"
apostol = "Brenard Jairuz Apostol"
balusada = "Mary Gold Balusada"
baslan = "Christy Mae Baslan"
mons = "Dairel Monsuller"

#position
bayot_position = "Team Leader"
aribal_position = "Back End Developer"
apostol_position = "Back End Developer"
balusada_position = "User Interface Designer"
baslan_position = "Back End Developer"
mons_position = "User Interface Designer"

#pictures
bayot_pic = pygame.image.load("D:/bayot.png")
aribal_pic = pygame.image.load("D:/aribal.png")
apostol_pic = pygame.image.load("D:/apostol.png")
balusada_pic = pygame.image.load("D:/balusada.png")
baslan_pic = pygame.image.load("D:/baslan.png")
mons_pic = pygame.image.load("D:/monsuller.png")


#fb links
bayot_link = r"https://www.facebook.com/khentrj.tuppal"
aribal_link = r'''https://www.facebook.com/profile.php?id=100075138132589'''
apostol_link = r"https://www.facebook.com/skim.carme"
balusada_link = r"https://www.facebook.com/profile.php?id=100076475830733"
baslan_link = r"https://www.facebook.com/ytsirhc.nalsab.5"
mons_link = r"https://www.facebook.com/"
default_link = "Facebook.com"

############################################################################################################
ui = pygame.display.set_mode((1320,680))
ui.fill((0,100,0))

#inerting position
bayot_font_position = font.render(bayot_position, True, (255,255,255))
ui.blit(bayot_font_position, (618,325))
aribal_font_position = font.render(aribal_position, True, (255,255,255))
ui.blit(aribal_font_position, (96, 580))
apostol_font_position = font.render(apostol_position, True, (255,255,255))
ui.blit(apostol_font_position, (346, 580))
balusada_font_position = font.render(balusada_position, True, (255,255,255))
ui.blit(balusada_font_position, (579,580))
baslan_font_position = font.render(baslan_position, True, (255,255,255))
ui.blit(baslan_font_position, (846, 580))
mons_font_position = font.render(mons_position, True, (255,255,255))
ui.blit(mons_font_position, (1098,580))

#inserting links

bayot_font_link = ui.blit(font.render(default_link, True, link_color), (615,350))
aribal_hyperlink = ui.blit(font.render(default_link, True, link_color), (110, 605))
apostol_hyperlink = ui.blit(font.render(default_link, True, link_color), (363, 605))
balusada_hyperlink = ui.blit(font.render(default_link, True, link_color), (615, 605))
baslan_hyperlink = ui.blit(font.render(default_link, True, link_color), (867, 605))
mons_hyperlink = ui.blit(font.render(default_link, True, link_color), (1115, 605))

#inserting heading
heading_font = font1.render(heading, True, (0,255,255))
ui.blit(heading_font, (400, 50))

#inserting names
bayot_name = font.render(bayot, True, (255,255,0))
ui.blit(bayot_name, (590, 300))
aribal_name = font.render(aribal, True, (255,255,0))
ui.blit(aribal_name, (107, 555))
apostol_name = font.render(apostol, True, (255,255,0))
ui.blit(apostol_name, (331, 555))
balusada_name = font.render(balusada, True, (255,255,0))
ui.blit(balusada_name, (596, 555))
baslan_name = font.render(baslan, True, (255,255,0))
ui.blit(baslan_name, (846,555))
mons_name = font.render(mons, True, (255,255,0))
ui.blit(mons_name, (1106,555))


#inserting image
ui.blit(bayot_pic, (600,200))
ui.blit(aribal_pic, (100, 450))
ui.blit(apostol_pic, (350, 450))
ui.blit(balusada_pic, (600, 450))
ui.blit(baslan_pic, (850, 450))
ui.blit(mons_pic, (1100, 450))

#click me
color_ = (0,0,0)
color_1 = (0,0,0)
cfont = pygame.font.SysFont("Agency fb", 45)
click_me = ui.blit(cfont.render("Click me to continue", True, color_), (160,225))
click_me1 = ui.blit(cfont.render("Click space to continue", True, color_1), (900, 230))


    
############################################################################################################

run = True
while run:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
            if event.key == K_SPACE:
                run = False
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if bayot_font_link.collidepoint(pos):
                webbrowser.open(bayot_link)
            if aribal_hyperlink.collidepoint(pos):
                webbrowser.open(aribal_link)
            if apostol_hyperlink.collidepoint(pos):
                webbrowser.open(apostol_link)
            if balusada_hyperlink.collidepoint(pos):
                webbrowser.open(balusada_link)
            if baslan_hyperlink.collidepoint(pos):
                webbrowser.open(baslan_link)
            if mons_hyperlink.collidepoint(pos):
                webbrowser.open(mons_link)

            if click_me.collidepoint(pos):
                run = False

    if click_me.collidepoint(pygame.mouse.get_pos()):
        link_color = (255,255,255)
    else:
        link_color = (255,255,255)
        
    pygame.display.update()
