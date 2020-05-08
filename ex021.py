import pygame
pygame.init() #inicia
pygame.mixer.music.load('ex021.mp3') #carrega o arquivo
pygame.mixer.music.play() #toca a musica
pygame.event.wait() # espera a musica acabar