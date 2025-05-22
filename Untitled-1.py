from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,picture,w,h,x,y,speed = 5):
        super().__init__()
        self.image=transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y =y
        self.speed = speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

run = True
class Player(GameSprite):
    def update(self):
        self.reset()
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 600:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x >0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 600:
            self.rect.x += self.speed
        if len(sprite.spritecollide(self, group, False)) != 0:
            if keys[K_w] and self.rect.y > 0:
                self.rect.y += self.speed + 1
            if keys[K_s] and self.rect.y < 600:
                self.rect.y -= self.speed
            if keys[K_a] and self.rect.x >0:
                self.rect.x += self.speed
            if keys[K_d] and self.rect.x < 600:
                self.rect.x -= self.speed
player = Player('popo.png',100,100,100,100)
win = GameSprite('really.png',100,100,300,300)
enemy = GameSprite('ggg.jpg',100,100,250,250)
group = sprite.Group()
group.add(GameSprite('Без названия.jpg',50,50,100  + 50,100  + 50))
class Enemy(GameSprite):
    def update (self):
        self.reset()
        self.rect.x += self.speed
        if self.rect.x < self.x -10 or self.rect.x >self.x + 200:
            self.speed *= -1
class Bulletr(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 700:
            self.kill()
class Bulletl(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()
class Bulletu(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
class Bulletd(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.kill()            
wall_1 = GameSprite('popo.png',80,180,200,250)
window = display.set_mode((700, 500))
clock = time.Clock()
display.set_caption('Моя первая игра')
player = Player('popo.png',100,100,100,100,5)
win = GameSprite('really.png',100,100,400,400,5)
enemy = Enemy('ggg.jpg',100,100,250,250,3)
enemy1 = Enemy('ggg.jpg',100,100,350,350,-4)
enemy2 = Enemy('ggg.jpg',100,100,450,450,2)
group = sprite.Group()
enemys = sprite.Group()
bullets = sprite.Group()
enemys.add(enemy)
enemys.add(enemy1)
enemys.add(enemy2)
group.add(wall_1)

finish = 1
while run:
    clock.tick(120)
    if finish:
        window.fill((255,255,255))
        player.update()
        enemys.update()
        win.reset()
        group.draw(window)
        bullets.update()
        bullets.draw(window)
        if sprite.collide_rect(player,win):
            finish = False
            qwe =transform.scale(image.load('popo.png'),(700,700))
            window.blit(qwe, (0,0))
        if len(sprite.spritecollide(player, enemys, False)) != 0:
            finish = False
            qwe = transform.scale(image.load('popo.png'),(700,700))
            window.blit(qwe, (0,0))    
        sprite.groupcollide(bullets, group, True, False)
        sprite.groupcollide(bullets, enemys, True, True)
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN and e.key == K_RIGHT:
            bullets.add(Bulletr('popo.png',20,20,player.rect.x + 25,player.rect.y+25,15))
        if e.type == KEYDOWN and e.key == K_LEFT:
            bullets.add(Bulletl('popo.png',20,20,player.rect.x + 25,player.rect.y+25,15))
        if e.type == KEYDOWN and e.key == K_UP:
            bullets.add(Bulletu('popo.png',20,20,player.rect.x + 25,player.rect.y+25,15))
        if e.type == KEYDOWN and e.key == K_DOWN:
            bullets.add(Bulletd('popo.png',20,20,player.rect.x + 25,player.rect.y+25,15)   )
                  
    display.update()