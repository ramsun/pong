import sys, pygame, time
pygame.init()
myFont = pygame.font.SysFont("wingdings2", 150)

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255
PADDLE_WIDTH = 8
PADDLE_HEIGHT = 100
DISTANCE_SCREEN = 8


screen = pygame.display.set_mode(size)

# def drawSolidLine(screen, width, height):
	# pygame.draw.lines(screen, white, False, [(width/2, 0), (width/2, height)], 3)

def equalSpaceDashGen(screen, numSegments, startPoint, endPoint):
	"""Creates a dashed line that is meant to represent the net for the tennis match"""
	RATIO = 0.66
	fullSize = endPoint[1] - startPoint[1]
	black_white_seg = fullSize/numSegments

	whiteSegment = RATIO * black_white_seg
	
	segmentStart = startPoint[1];
	while  segmentStart < endPoint[1]:
		pygame.draw.lines(screen, white, False, [(width/2, segmentStart), (width/2, segmentStart + whiteSegment )], 3)
		segmentStart += black_white_seg

def paddleMovement(screen, heightLeft, heightRight):
	"""Creates the initial positions of the two rectangles """

	pygame.draw.rect(screen, white, (DISTANCE_SCREEN,heightLeft,PADDLE_WIDTH, PADDLE_HEIGHT), 0)
	pygame.draw.rect(screen, white, ((width-(DISTANCE_SCREEN+PADDLE_WIDTH)),heightRight,PADDLE_WIDTH,PADDLE_HEIGHT), 0)


def playerScores(leftScore, rightScore):
	""" Prints the scores of each player onto the game """
	leftLabel = myFont.render(str(leftScore), 1, white)
	rightLabel = myFont.render(str(rightScore), 1, white)

	screen.blit(leftLabel, (width/2-150, 8))
	screen.blit(leftLabel, (width/2+77, 8))

def main():

	print pygame.font.get_fonts()

	ball = pygame.image.load("ball.gif")
	ballrect = ball.get_rect()
	INITIAL_POSITION = height/2
	heightLeft = INITIAL_POSITION
	heightRight = INITIAL_POSITION
	SPEED = 3

	while 1:
		key = pygame.key.get_pressed()
		if key[pygame.K_UP] and heightRight>0:
			heightRight -=  SPEED
		if key[pygame.K_DOWN] and heightRight < (height-PADDLE_HEIGHT):
			heightRight += SPEED
		if key[pygame.K_w] and heightLeft>0:
			heightLeft -=  SPEED
		if key[pygame.K_s] and heightLeft < (height-PADDLE_HEIGHT):
			heightLeft += SPEED



		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		ballrect = ballrect.move(speed)
		if ballrect.left < 0 or ballrect.right > width:
			speed[0] = -speed[0]
		if ballrect.top < 0 or ballrect.bottom > height:
			speed[1] = -speed[1]


	
		screen.fill(black)
		#drawSolidLine(screen, width, height)
		equalSpaceDashGen(screen, 40, (width/2, 0), (width/2, height))
		paddleMovement(screen, heightLeft, heightRight)
		playerScores(0, 0)
		screen.blit(ball, ballrect)
		pygame.display.flip()

main()