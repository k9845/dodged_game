import pygame
import time
import random

pygame.init()

display_width =800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Racing')
clock = pygame.time.Clock()

carImg = pygame.image.load('transportation.png')

def things_dodged(count):
	font = pygame.font.SysFont(None,20)
	text = font.render("Dodged:" +str(count),True,black)
	gameDisplay.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh,color):
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])


def car(x,y):
	gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
	textSurface = font.render(text,True,black)
	return textSurface ,textSurface.get_rect()

def message_display(text):
	ltext = pygame.font.Font('freesansbold.ttf', 115) 
	TextSurf , TextRect = text_objects(text,ltext)
	TextRect.center =((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf , TextRect)
	pygame.display.update()
	
	time.sleep(2)
	
	game_loop()
def crash():
	message_display('You Crashed')


def game_loop():
	
	x = (display_width * 0.45)
	y = (display_height * 0.72)

	x_change = 0

	thing_startx = random.randrange(0,display_width)
	thing_starty = -600
	thing_speed = 7
	thing_width = 50
	thing_height = 50

	dodged = 0

	gameExit = False

	while not gameExit:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
			if event.type == pygame.KEYUP:	
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0


		x += x_change
		gameDisplay.fill((255,60,70))

		#things(thingx,thingy,thingw,thingh,color)
		things(thing_startx,thing_starty,thing_width,thing_height,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
		thing_starty+= thing_speed


		car(x,y)

		things_dodged(dodged)
		
		if x > (display_width - car_width) or x < 0:
			crash()

		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,display_width)
			dodged += 1
		
		if y < thing_starty+thing_height:
			print('y crossover')

			if x + car_width > thing_startx and x < thing_startx + thing_width:
				print('x crossover')
				crash()





		pygame.display.update()
		clock.tick(70)
game_loop()

pygame.quit()
quit()
