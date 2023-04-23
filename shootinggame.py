from pygame import*
from random import*

font.init()
font = font.Font(None, 36)
score = 0

class Setup(sprite.Sprite):
    def __init__(self, imagename, width, height, x,y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(imagename), (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self): 
        w.blit(self.image,(self.rect.x,self.rect.y))


class Bullet(Setup):
    def update(self):
        self.rect.y -= 7
        if self.rect.y < 0:
            self.kill()


class Player(Setup):
    def moving(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= 10
        if keys[K_RIGHT]:
            self.rect.x += 10
        if keys[K_UP]:
            self.rect.y -= 10
        if keys[K_DOWN]:
            self.rect.y += 10
    def fire(self):
        bullet = Bullet("bullet.png",20,40, self.rect.x, self.rect.y)
        bullets.add(bullet)

class Enemymove(Setup):
    def update(self):
        self.rect.y += 7







screenw = 700
screenh = 700
w = display.set_mode((screenw,screenh))
display.set_caption("shooting")
player = Player("rocket.png",50,100,screenw/2,(screenh-100))
bullets = sprite.Group()
monsters = sprite.Group()
back = transform.scale(image.load("galaxy.jpg"),(screenh,screenh))


wait = time.get_ticks() + 800
wait1 = time.get_ticks() + 200


run = True
time2 = True
score = 0
while run:
    if time2:
        w.blit(back,(0,0))
        text = font.render("Score: " + str(score), 1, (0,0,0))
        w.blit(text,(0,0))
        player.moving()
        player.reset()
        curwait = time.get_ticks()
        if curwait>wait:
            monster = Enemymove("rock.png",60,80,randint(0,640),5)
            monsters.add(monster)
            wait = time.get_ticks() + 800
        bullets.update()
        bullets.draw(w)
        monsters.update()
        monsters.draw(w)
        curshootingwait = time.get_ticks()
        for e in event.get():
            if e.type == KEYDOWN:
                if e.key == K_SPACE and curshootingwait>wait1:
                    player.fire()
                    wait1 = time.get_ticks() + 200
            if e.type == QUIT:
                run = False
    if sprite.groupcollide(monsters, bullets, True, True):
        score +=1
    if score == 50:
        time2 = False
        win = Setup("win.jpg",700,700, 0, 0)
        win.reset()
    if sprite.spritecollide(player, monsters, True):
        time2 = False
        lose = Setup("lose.png",700,700, 0, 0)
        lose.reset()

    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_e:

                w.fill((0,0,0))
                player = Player("rocket.png",50,100,screenw/2,(screenh-100))
                bullets = sprite.Group()
                monsters = sprite.Group()

                wait = time.get_ticks() + 800
                wait1 = time.get_ticks() + 200
                time2 = True


    display.update()
    time.delay(50)