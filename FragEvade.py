from random import randint
import pygame
# define screen size
WIDTH = 1200
HEIGHT = 500

#Gr avity and speeds
GRAVITY = 0.06
SP = 1
FG_SP = 1.3
FR_SPEED = 2

# player n baddies
iii = randint(75,500)
player = Actor('heroine.png',(100,400))
FRAG = Actor('frf',(1300,iii)) #1100,300 lines it up exactly in the middle on the right most
FRAG1 = Actor('frfr',(1300,300)) #1100,300 lines it up exactly in the middle on the right most
zero = Actor('00',(1300,300))
zero1 = Actor('000',(1300,300))
zero2 = Actor('0000',(1300,300))
zero3 = Actor('00000',(1300,300))
one = Actor('11',(1300,300))
one1 = Actor('111',(1300,300))
one2 = Actor('1111',(1300,300))
one3 = Actor('11111',(1300,300))

llcount = 0
ll1 = Actor('ddd.png',(1300,300))
ll2 = Actor('dd.png',(1300,300))
ll3 = Actor('d.png',(1300,300))
ll4 = Actor('r.png',(1300,300))

ll = False
lld = False
b0  = False
b01 = False
b02 = False
b03 = False
b1  = False
b11 = False
b12 = False
b13 = False

frag_count = 1
frag2 = False

#background stuff1
BG_X_BEG = 0
BG2_X_BEG = 1850
BGF_X_BEG = 0
BGF2_X_BEG = 1828

PWRM = 1
PWR_PL = 0
BAD_M = 1
BADD = 0


bg_ = pygame.image.load("images/background.png").convert()
bg1_ = pygame.image.load("images/background1.png").convert()


bgf = pygame.image.load("images/fff.png").convert()
pygame.Surface.set_colorkey(bgf, [255,255,255])
bgf.set_alpha(255)
bgf1 = pygame.image.load("images/ff.png").convert()
pygame.Surface.set_colorkey(bgf1, [255,255,255])
bgf1.set_alpha(255)


# define initial and flap velocities
player.y_velocity = 0
player.flap_velocity = -2
player.score = 0
player.x_velocity = 0


ll1.angle = -15
ll2.angle = -6
ll3.angle = 6
ll4.angle = 15
#sounds
#beep = tone.create('A3', 5)

playing = True

def update():

    global playing, BG, BG2_X_BEG, BG_X_BEG, BGF2_X_BEG, BGF_X_BEG, SP, FG_SP, FR_SPEED, beep, frag_count, frag2
    global b0,b01,b02,b03,b1,b11,b12,b13,PWRM,PWR_PL,BAD_M,BADD, ll, lld, llcount


    if playing:
        #BG UPDATE
        if frag_count > 1:
            frag2 = True
        BG_X_BEG -= SP
        BG2_X_BEG -= SP
        BGF_X_BEG -= FG_SP
        BGF2_X_BEG -= FG_SP

        SP += 0.0001
        FG_SP += 0.0015

        if BG_X_BEG < 1850* -1:
            BG_X_BEG = 1850
        if BG2_X_BEG < -1850:
            BG2_X_BEG = 1850
        if BGF_X_BEG < -1828:
            BGF_X_BEG = 1828
        if BGF2_X_BEG < -1828:
            BGF2_X_BEG = 1828

        ## score for living
        player.score += (0.001* SP)


        if b0 == False:
            if (round(player.score,0) % 5 == 0):
                b0 = True
                zero.x = randint(600,1100)
        if b0  == True:
            zero.x -= (SP*0.8)
            if zero.x < 0:
                zero.x = 1300
                b0 = False
            if player.colliderect(zero):
                player.score += ((250+FR_SPEED)*PWRM)+PWR_PL
                zero.x = 1300
                b0 = False

        if b1 == False:
            if (round(player.score,0) % 5 == 1):
                b1 = True
                one.x = randint(800,1100)  #      if b01 == False:
                one.y = randint(100,400)
        if b1  == True:
            one.x -= (SP*0.8)
            if one.x < 0:
                one.x = 1300
                b1 = False
            if player.colliderect(one):
                player.score += 250+((2*FR_SPEED)*PWRM)+PWR_PL
                one.x = 1300
                b1 = False


        if b01 == False:
            if (round(player.score,0) % 16 == 0):
                b01 = True
                zero1.x = randint(800,1100)
                zero1.y = randint(100,300)
        if b01  == True:
            zero1.x -= (SP*0.8)+1
            zero1.y -= .5
            if zero1.x < 0:
                zero1.x = 1300
                b01 = False
            if player.colliderect(zero1):
                player.score += 500+((5*FR_SPEED)*PWRM)+PWR_PL
                zero1.x = 1300
                b01 = False
        if b11 == False:
            if (round(player.score,0) % 16 == 1):
                b1 = True
                one1.x = randint(800,1100)  #      if b01 == False:
                one1.y = randint(100,350)
        if b11  == True:
            one1.x -= (SP*0.8)+1
            if one1.y > 100:
                one1.y -=1
            if one1.t < 100:
                one1.y += 2
            if one1.x < 0:
                one1.x = 1300
                b11 = False
            if player.colliderect(one1):
                player.score += 500+((10*FR_SPEED)*PWRM)+PWR_PL
                one1.x = 1300
                b11 = False

        if keyboard.space or keyboard.K_w:# and player.y_velocity >= 0:
            player.y_velocity += (0.25)*player.flap_velocity
            if player.angle <= 0:
                player.angle = 5
            player.angle += 1
        if keyboard.K_s:# and player.y_velocity < 0:
            player.y_velocity += -(0.25 *player.flap_velocity)
            if player.angle > 0:
                player.angle = -5
            player.angle -= 1
        # acceleration is rate of change of velocity
        player.y_velocity += GRAVITY
        # velocity is rate of change of position
        player.y += player.y_velocity



        vel_factor = .2
        # changes for x
        if keyboard.K_d and player.x_velocity <= 0:
            player.x_velocity = vel_factor
 #           beep
            player.score += 5
        if keyboard.K_d and player.x_velocity > 0:
            player.x_velocity += vel_factor
            player.angle -= 0.5
#            beep
        if keyboard.K_a:
            if player.x>=0:
                if player.x_velocity == 0:
                   player.x_velocity = -vel_factor
                player.x_velocity+= -vel_factor
                player.angle +=0.5

        player.x += player.x_velocity


        ## player meets the edfe
        if player.x >= WIDTH:
           player.x = WIDTH-2
           player.x_velocity = -.02

        if player.x <= 0:
            player.x = 0
            player.x_velocity = .02

        if player.y <= 0:
            player.y = 0
            player.y_velocity = 0.2

        FRAG.x -= FR_SPEED
        if FRAG.x < -50:
            FF = randint(150,500)
            FRAG.x = 1300+FF
            player.score += FG_SP*10
            GG = randint(100,400)
            FRAG.y = GG
            II = randint(1,10)
            FR_SPEED += SP*(II*.1)
            frag_count += 1

      #  create new FRAGs
        if(frag2 == True):
            FRAG1.x -= FR_SPEED*2
#            d = randint(-3,3)
            FRAG1.angle -= .2
            if FRAG1.x < -50:
                FF1 = randint(150,500)
                FRAG1.x = 1300+FF1
                player.score += FG_SP*25
                GG1 = randint(100,400)
                FRAG1.y = GG1
                II1 = randint(1,5)
                FR_SPEED += SP*(II1*.1)
                frag_count += 1

        if player.colliderect(FRAG):
            player.score -= (.275*BAD_M)+BADD
            player.x
        if player.colliderect(FRAG1):
            player.score -= (.3*FR_SPEED*BAD_M)+BADD


        if ll == False:
            if (frag_count %25 == 0):
                lly = randint(200,400)
                ll1.y = lly
                ll2.y = lly
                ll3.y = lly
                ll4.y = lly

                llx = randint(1200,1300)
                ll1.x = llx + 0
                ll2.x = llx + 100
                ll3.x = llx + 200
                ll4.x = llx + 300

                ll1.angle = -30
                ll2.angle = -8
                ll3.angle = 10
                ll4.angle = 30

                llcount = 0
                lld = False
                ll = True


        if ll == True:
            if player.colliderect(ll1) or player.colliderect(ll2) or player.colliderect(ll3) or player.colliderect(ll4):
                PWRM = 2
                PWR_PL = 666
                BAD_M = 0.3
                BADD = -4

            if lld == True:
                ll1.angle += 01.1
                ll2.angle += 01.1
                ll3.angle += 01.1
                ll4.angle += 01.1
                llcount -= 1
            if lld == False:
                ll1.angle -= 01.1
                ll2.angle -= 01.1
                ll3.angle -= 01.1
                ll4.angle -= 01.1
                llcount += 1
            if llcount >= 90:
                lld = True
            if llcount <=0:
                lld = False

            ll1.x -= 4
            ll2.x -= 1
            ll3.x -= 3
            ll4.x -= 5
            PWRM,PWR_PL,BAD_M,BADD,


        # ...or touches the ground
        if player.y > (HEIGHT - 20):
            playing = False

def draw():

    if playing:
        screen.clear()
        screen.blit(bg_, (BG_X_BEG,0))
        screen.blit(bg1_, (BG2_X_BEG,0))
        screen.blit(bgf, (BGF_X_BEG,0))
        screen.blit(bgf1, (BGF2_X_BEG,0))

        # draw score
        rscore = round(player.score, 1)
        numbad = frag_count

        screen.draw.text('Score:',(5,10),fontsize=30, color="red")
        screen.draw.text(str(rscore), (20, 40), fontsize=40, color="white")
        screen.draw.text(str(numbad), (900,20), fontsize=50, color="white")

        # draw player
        player.draw()
        FRAG.draw()
        FRAG1.draw()
        zero.draw()
        one.draw()
        zero1.draw()
        one1.draw()
        ll1.draw()
        ll2.draw()
        ll3.draw()
        ll4.draw()

    else:
        screen.draw.text('Game Over!', (420, 200), fontsize=80, color="white")