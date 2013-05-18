import pygame

pygame.init()

size = [ 700, 500 ]
white = (255, 255, 255)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("So You Think You Know Greek Mythology, eh?")
done = False

clock = pygame.time.Clock()

pygame.mixer.music.load('music/bg_music.mp3')
pygame.mixer.music.play()

bg_image = pygame.image.load('img/bg_img.jpg').convert()



while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	screen.blit(bg_image, [0,0])
	pygame.display.flip()
	clock.tick(20)
	
pygame.quit()