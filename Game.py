""" Game.py is a pong game that is fully customizable.  The global constants are easily accessable and can be fine tuned to fit one's needs. 

Created by Ramamurthy Sundar on December 30, 2014.
"""

import sys, pygame, time

pygame.init()
myFont = pygame.font.SysFont("impact", 150)

# ARGUMENTS
BALL_SPEED = 5
screen_size = width, height = 1100, 600
PADDLE_WIDTH = 8
PADDLE_HEIGHT = 100
DISTANCE_SCREEN = 8

NUMBER_OF_SEGMENTS = 40
black = 0, 0, 0
white = 255, 255, 255
speed = [BALL_SPEED, BALL_SPEED]
screen = pygame.display.set_mode(screen_size)

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
	screen.blit(rightLabel, (width/2+77, 8))

def main():

	leftScore = 0
	rightScore = 0

	ball = pygame.image.load("ball.png")
	ballrect = ball.get_rect()
	INITIAL_POSITION = height/2
	heightLeft = INITIAL_POSITION
	heightRight = INITIAL_POSITION
	SPEED = 3

	while 1:

		# moves the paddles with key controls
		key = pygame.key.get_pressed()
		if key[pygame.K_UP] and heightRight>0:
			heightRight -=  SPEED
		if key[pygame.K_DOWN] and heightRight < (height-PADDLE_HEIGHT):
			heightRight += SPEED
		if key[pygame.K_w] and heightLeft>0:
			heightLeft -=  SPEED
		if key[pygame.K_s] and heightLeft < (height-PADDLE_HEIGHT):
			heightLeft += SPEED

		# reflects the ball off of the left and right paddles 
		if (0 < ballrect.right - (width - (PADDLE_WIDTH + DISTANCE_SCREEN)) < BALL_SPEED) \
			and (ballrect.bottom > heightRight) and (ballrect.top < heightRight+PADDLE_HEIGHT):
			speed[0] = -speed[0]

		if (-BALL_SPEED < ballrect.left - (PADDLE_WIDTH + DISTANCE_SCREEN) < 0) \
			and (ballrect.bottom > heightLeft) and (ballrect.top < heightLeft+PADDLE_HEIGHT):
			speed[0] = -speed[0]

		#quits if you want to quit
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		ballrect = ballrect.move(speed)

		# increases the persons score who wins by 1
		if ballrect.right < 0:
			rightScore += 1
		elif ballrect.left > width:
			leftScore += 1

		#resets the ball to the center if it goes off screen
		if ballrect.right < 0 or ballrect.left > width:
			ballrect.centerx = width/2
			ballrect.centery = height/2

		if ballrect.top < 0 or ballrect.bottom > height:
			speed[1] = -speed[1]

		screen.fill(black)
		equalSpaceDashGen(screen, NUMBER_OF_SEGMENTS, (width/2, 0), (width/2, height))
		paddleMovement(screen, heightLeft, heightRight)
		playerScores(leftScore, rightScore)
		screen.blit(ball, ballrect)
		pygame.display.flip()

if __name__ == "__main__":
	main()