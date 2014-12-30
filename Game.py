import sys, pygame, time
pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

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

while 1:
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
    screen.blit(ball, ballrect)
    pygame.display.flip()