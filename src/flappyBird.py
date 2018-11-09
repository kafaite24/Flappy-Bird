import pygame
import random
import time

#Initializing
pygame.init()
pygame.mixer.init()

#Loading game sounds
sounda= pygame.mixer.Sound('./assets/sounds/sfx_wing.wav')
soundb=pygame.mixer.Sound('./assets/sounds/sfx_point.wav')
soundc=pygame.mixer.Sound('./assets/sounds/sfx_die.wav')
soundd=pygame.mixer.Sound('./assets/sounds/Applause.wav')

#Game over and total score message appearance function
def msg(message,color):
	font=pygame.font.SysFont(None,100)
	text=font.render(message,True,color)
	display.blit(text,[300,200])
	pygame.display.update()

#Score appearance at the top left during the game function
def scoreMsg(message,color):
	font=pygame.font.SysFont(None,40)
	text=font.render(message,True,color)
	display.blit(text,[20,20])
	pygame.display.update()

def levelMsg(message,color):
	font=pygame.font.SysFont(None,40)
	text=font.render(message,True,color)
	display.blit(text,[1085,20])
	pygame.display.update()

#Setting display and Caption
display= pygame.display.set_mode((1200, 600))
clock=pygame.time.Clock()
caption= pygame.display.set_caption('Flying Birdie!')

#Main game function to call when pressed ENTER
def main():

	#Setting backgrounds
	background = pygame.image.load('./assets/images/fl.jpg')
	background2=pygame.image.load('./assets/images/level2.png')
	background3=pygame.image.load('./assets/images/level3.png')
	background4=pygame.image.load('./assets/images/level4.jpg')
	background5=pygame.image.load('./assets/images/level5.jpg')

	backgroundSize = background.get_size()
	backgroundRect = background.get_rect()
	screen = pygame.display.set_mode((1200,600))
	width, height = backgroundSize

	#Main game loop flag
	flag= True

	#Positions of the pipes to choose randomly from
	listOfDimensions=[125,225,325]

	#Initializing Pipe coordinates and positions
	x1=400
	y1=0
	var1=225
	x2=400
	y2=375

	x3=800
	y3=0
	var2=125
	x4=800
	y4=275

	x5=1200
	y5=0
	var3=325
	x6=1200
	y6=475

	#Loading bird image and initializing its height
	bird=pygame.image.load('./assets/images/birdj.gif')
	y=270

	#Initializing jump,level and score
	jump=0
	score=0
	level=1


	#Main game loop
	while flag:

		gameLost=False

		for event in pygame.event.get():

			if event.type==pygame.QUIT:
				flag=False

			if event.type==pygame.KEYDOWN:
				if (event.key==pygame.K_UP) and(jump==0):
					jump=100
					sounda.play()

		if(jump!=0):
			y-=10
			jump-=10

		y+=5

		#Changing background with levels
		if(level==1):
			screen.blit(background,backgroundRect)
			color=(122,69,154)
		elif(level==2):
			screen.blit(background2,backgroundRect)
			color=(30,157,68)
		elif(level==3):
			screen.blit(background3,backgroundRect)
			color=(141,136,35)
		elif(level==4):
			screen.blit(background4,backgroundRect)
			color=(154,176,201)
		elif(level==5):
			screen.blit(background5,backgroundRect)
			color=(208,78,15)

		display.blit(bird,(200,y))

		#Drawing pipes as obstacles
		pygame.draw.rect(display,color,[x1,y1,50,var1])
		pygame.draw.rect(display,color,[x2,y2,50,1000])
		pygame.draw.rect(display,color,[x3,y3,50,var2])
		pygame.draw.rect(display,color,[x4,y4,50,1000])
		pygame.draw.rect(display,color,[x5,y5,50,var3])
		pygame.draw.rect(display,color,[x6,y6,50,1000])

		#Changing speed of pipes with levels
		if(level==1):
			change=5
		elif(level==2):
			change=7
		elif(level==3):
			change=9
		elif(level==4):
			change=11
		elif(level==5):
			change=13

		#Moving pipes
		x1-=change
		x2-=change
		x3-=change
		x4-=change
		x5-=change
		x6-=change

		#Disappearance and reappearance of pipes and score addition
		if(x1+50<=0):
			x1=width
			ind1=random.randint(0,2)
			x2=width
			var1=listOfDimensions[ind1]
			y2=var1+150
			score+=1
			soundb.play()

		if(x3+50<=0):
			x3=width
			ind2=random.randint(0,2)
			x4=width
			var2=listOfDimensions[ind2]
			y4=var2+150
			score+=1
			soundb.play()

		if(x5+50<=0):
			x5=width
			ind3=random.randint(0,2)
			x6=width
			var3=listOfDimensions[ind3]
			y6=var3+150
			score+=1
			soundb.play()

		#Hitting the obstacles and losing the game
		if(x1<=240)and(x1+40>=200)and((y<=var1)or(y+35>=var1+150)):
			gameLost=True
		if(x3<=240)and(x3+40>=200)and((y<=var2)or(y+35>=var2+150)):
			gameLost=True
		if(x5<=240)and(x5+40>=200)and((y<=var3)or(y+35>=var3+150)):
			gameLost=True

		#Hitting top and bottom
		if(y==600)or(y==0):
			gameLost=True

		#Game lost events
		if(gameLost):
			message='Game Over! Score='+str(score)
			msg(message,(97,12,58))
			soundc.play()
			time.sleep(3)
			exit()

		#Determining level
		if(score>=20)and(score<=100):
			level=(score//20)+1

		#Displaying instructions to play
		if(score==0):
			message='Press UP key to Jump'
			msg(message,(0,0,0))

		#Winning message
		if(score==100):
			message1='YOU WON! CONGRATS'
			msg(message1,(255,255,255))
			soundd.play()
			time.sleep(10)
			exit()



		#Top left score card
		scoreCard='Score '+str(score)
		scoreMsg(scoreCard,(97,97,97))

		#Top right level card
		levelNumber='Level '+str(level)
		levelMsg(levelNumber,(97,97,97))

		pygame.display.update()
		clock.tick(20)

#Front page function
def myFunc():

	#Front background set
	background1 = pygame.image.load('./assets/images/front.gif')
	backgroundSize1 = background1.get_size()
	backgroundRect1 = background1.get_rect()
	screen = pygame.display.set_mode((1200,600))

	flag=True
	
	while flag:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				flag=False

			if event.type==pygame.KEYDOWN:
				if (event.key==pygame.K_RETURN):
					#Calling main game function
					main()

		screen.blit(background1,backgroundRect1)
		pygame.display.update()

	clock.tick(20)

myFunc()
