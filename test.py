#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import pygame
import pygame.gfxdraw
from pygame.locals import *

from configLoader import configLoader
from menu import Menu, MENU_BACK, MENU_EXIT
from textmenu import textMenu, TEXT_NEWLINE

# constantes
WIN_SIZE = (1000, 600)
FPS = 60
COLOR_BACKGROUND = (236, 237, 238)
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Clase ventana
class Window:
    def __init__(self, winsize):
        self.window = winsize

    def getWindowWidth(self):
        return self.window[0]

    def getWindowHeight(self):
        return self.window[1]

# MAIN ELEMENTS TEST
font = "nevis.ttf"
window = Window(WIN_SIZE)
pygame.init()
display = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("Test menu")
surface = pygame.display.get_surface()
clock = pygame.time.Clock()
image = pygame.image.load("background.jpg").convert_alpha()
global options
options = configLoader("window.ini", verbose=True)
track = [0]

def playTrack(index):
    track[0] = index

def dummyconfig(element, *args):
    options.setParameter(args[0], element)
    options.export()

# MENU TESTING
menu_jugar = Menu(window, font, "Jugar", centered=False, draw_region_x=10)
menu_jugar.addSelector("Pista", [("Adelaide rw", 0), ("El origen", 1)], playTrack, None)
menu_jugar.addOption("Volver", MENU_BACK)

# Config
menu_config = Menu(window, font, "Configuraciones", centered=False, draw_region_x=10)
menu_config.addSelector("Modo ventana", [("Activado", "TRUE"), ("Desactivado", "FALSE")], dummyconfig, None, "WINDOWED")
menu_config.addOption("Volver", MENU_BACK)

# Ayuda menu
menu_ayuda = textMenu(window, font, "Ayuda")
menu_ayuda.addOption("Volver", MENU_BACK)
menu_ayuda.addText("Para acelerar pulsa la tecla W")
menu_ayuda.addText("Para frenar pulsa la tecla W")
menu_ayuda.addText(TEXT_NEWLINE)

# Acerca de menu
menu_about = textMenu(window, font, "Acerca de")
menu_about.addOption("Volver", MENU_BACK)
menu_about.addText("Menu para Python")
menu_about.addText("Autor: Pablo Pizarro")
menu_about.addText(TEXT_NEWLINE)

# Se arma menu
menu = Menu(window, font, "Menu principal")
menu.addOption("Jugar", menu_jugar)
menu.addOption("Configuraciones", menu_config)
menu.addOption("Ayuda", menu_ayuda)
menu.addOption("Acerca de", menu_about)
menu.addOption("Cerrar", MENU_EXIT)

inmenu = True

while True:
    surface.fill(COLOR_BACKGROUND)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if inmenu:
                if event.key == K_UP:
                    menu.down()
                elif event.key == K_DOWN:
                    menu.up()
                elif event.key == K_RETURN:
                    menu.select()
                elif event.key == K_LEFT:
                    menu.left()
                elif event.key == K_RIGHT:
                    menu.right()
                elif event.key == K_BACKSPACE:
                    menu.reset(1)
            else:
                print "NO_MENU"
    surface.blit(image, (0, 0))
    menu.draw(surface)
    pygame.display.flip()
