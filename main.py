import random
import os
import sys

import pygame
import time
from pygame.locals import *

hats = []

with open(os.path.join(sys.path[0], "hats.txt"), "r") as file:
    for hat in file:
        hat = hat.strip('\n')
        hats.append(hat)
    print(hats)
random_index = random.randrange(len(hats))

a_file = open("last.txt")
file_contents = a_file.read()
print("Last was: " + file_contents)

while (file_contents == hats[random_index]):
    random_index = random.randrange(len(hats))

with open(os.path.join(sys.path[0], "last.txt"), 'w') as f:
    f.write(hats[random_index])

hat = hats[random_index]
print("The chosen Hat is: " + hat)

pygame.init()
display_surf = pygame.display.set_mode((1050, 1050))
image_surf = pygame.image.load(os.path.join(sys.path[0], "wheel.png")).convert()
imagerect = image_surf.get_rect()
display_surf.blit(image_surf, (5, 5))
pygame.display.flip()
start = time.time()
new = time.time()
angle = 0
while True:
    end = time.time()
    if end - start > 5:
        surf = pygame.image.load(os.path.join(sys.path[0], hat + ".png")).convert()
        display_surf.blit(surf, (5, 5))
        pygame.display.flip()
        time.sleep(10)
        break
    elif end - new > 0.05:
        print
        "rotating"
        new = time.time()
        # increase angle
        angle += 90
        # ensure angle does not increase indefinitely
        angle %= 360
        # create a new, rotated Surface
        surf = pygame.transform.rotate(image_surf, angle)
        # and blit it to the screen
        display_surf.blit(surf, (5, 5))
        pygame.display.flip()

