import pygame
import os

def pause():
    if pressed[pygame.K_p]:
        pygame.mixer.music.pause()

def unpause():
    if pressed[pygame.K_SPACE]:
        pygame.mixer.music.unpause()

def stop():
    if pressed[pygame.K_s]:
        pygame.mixer.music.stop()

def start_from_first_song():
    if pressed[pygame.K_g]:
        pygame.mixer.music.load(songs[0])
        pygame.mixer.music.play()

def next_song():
    global songs
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        songs = songs[1:] + [songs[0]]
        pygame.mixer.music.load(songs[0])
        pygame.mixer.music.play()

def previous_song():
    global songs
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        pygame.mixer.music.load(songs[len(songs) - 1])
        songs = [songs[len(songs) - 1]] + songs[:len(songs) - 1]
        pygame.mixer.music.play()

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

song1 = 'lab7\music\KE PLAYA X PSYCHOMANE - LVL - DEATH.mp3'
song2 = 'lab7\music\Zodivk - Devil Eyes.mp3'
song3 = 'lab7\music\PHONK EDITION - Режиссер (Phonk remix by.Eves x Kahenko).mp3'
songs = [song1, song2, song3]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        next_song()
        previous_song()
            
    pressed = pygame.key.get_pressed()
    screen.fill((255, 255, 255))

    pause()
    unpause()
    stop()
    start_from_first_song()
    
    pygame.display.flip()
#done