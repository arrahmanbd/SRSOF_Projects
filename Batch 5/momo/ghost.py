import pygame
from time import sleep

pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('assets/zombie.wav')
pygame.mixer.music.play()

image_files = ['assets/image1.jpg', 'assets/image2.jpg','assets/image3.jpg','assets/image4.jpg']
for filename in image_files:
    image = pygame.image.load(filename)
    window.blit(image, image.get_rect(center=window.get_rect().center))
    pygame.display.update()
    sleep(2)

sleep(5)

pygame.mixer.music.stop()
pygame.quit()
