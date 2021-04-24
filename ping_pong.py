from pygame import*

class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        # Вызываем конструктор класса (Sprite):
        super().__init__()

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height -150:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height -150:
            self.rect.y += self.speed


back = (0,0,0)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
r1 = Player('racket.png', 0, 200, 4, 50, 150)
r2 = Player('racket.png', 550, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font= font.Font('calibri.ttf', 70)
lose1 = font.render('PLAYER 2 WIN', True, (0,0,255))
lose2 = font.render('PLAYER 1 WIN', True, (0,0,255))

speed_x=3
speed_y=3 
game = True
clock = time.Clock()
FPS = 60
finish = False
score1 = 0
score2 = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game =False

    if finish != True:
        window.fill(back)
        r1.update_l()
        r2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(r1, ball) or sprite.collide_rect(r2, ball):
            speed_x *=-1 -0.02
            speed_y *=1 + 0.02


        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *=-1 - 0.02

        
        if ball.rect.x > 550:
            finish = True
            score1 +=1
            window.blit(lose2, (100,200))
    
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (100,200))

        r1.reset()
        r2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
    
