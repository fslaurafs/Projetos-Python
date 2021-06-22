# TOCANDO UM MP3
import pygame
pygame.init()
pygame.mixer.music.load('ex21.m4a')
pygame.mixer.music.play()
pygame.event.wait()

''' Colar o arquivo de música na área dos exercícios antes de iniciar'''