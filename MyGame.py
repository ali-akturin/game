import pygame

pygame.init()
win = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("xo")

walkRight = [pygame.image.load('right0.png'),  #Движение вправо АНИМАЦИЯ
pygame.image.load('right1.png'), pygame.image.load('right2.png'),
pygame.image.load('right3.png'), pygame.image.load('right4.png'),
pygame.image.load('right5.png'), pygame.image.load('right6.png'),
pygame.image.load('right7.png'), pygame.image.load('right8.png'),
pygame.image.load('right9.png')]

walkLeft = [pygame.image.load('left0.png'), #Движение влево АНИМАЦИЯ
pygame.image.load('left1.png'), pygame.image.load('left2.png'),
pygame.image.load('left3.png'), pygame.image.load('left4.png'),
pygame.image.load('left4.png'), pygame.image.load('left6.png'),
pygame.image.load('left7.png'), pygame.image.load('left8.png'),
pygame.image.load('left9.png')]

playerStand = pygame.image.load('stay.png')
bg = pygame.image.load('bg.jpg') #фон

clock = pygame.time.Clock()

x= 50
y= 760
width = 130
height = 120
speed = 10

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
lastMove = "right"

class Snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 16 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class Enemy():
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed

    def Move(self):
        if self.x < 0:
            while self.x != 1400:
                self.x+=speed
        else:
            while self.x != -2:
                self.x-=speed

    def draw(self, win):
        pygame.draw.circle(win, self.color , (self.x, self.y) , 40)


enemy = Enemy(800, 800, (0,0,0), 5)
def drawWindow():
    global animCount
    win.blit(bg, (0, 0))
    enemy.draw(win)

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount +=1
    elif right:
        win.blit(walkRight[animCount // 5], (x,y))
        animCount +=1
    else:
        win.blit(playerStand, (x,y))

    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

run = True
bullets = []
while run:
    clock.tick(40)
    enemy.Move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 1440 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if lastMove == "right":
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
            bullets.append(Snaryad(round(x + width // 2), round(y + height // 2), 4, (255, 0, 0), facing))

    if keys[pygame.K_LEFT] and x > 30:
        x-=speed
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] and x < 1440 - width - 30:
        x+=speed
        left = False
        right = True
        lastMove = "right"
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    if keys[pygame.K_ESCAPE]:  #Выход
        quit()


    print(isJump)

    drawWindow()

pygame.quit()
