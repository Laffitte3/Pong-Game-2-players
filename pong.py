import pygame, random

pygame.init()

witdh=900
height=600

display_surface= pygame.display.set_mode((witdh,height))

FPS=120
clock= pygame.time.Clock()
puntos_p1=0
puntos_p2=0


#Acciones de la bola
ball_velocity=2

aleatorio=[-1,1]
dx=random.choice(aleatorio)
dy=random.choice(aleatorio)

#direccion de la bola

#Pelota
ball_image= pygame.image.load("clown.png")
ball_image=pygame.transform.scale(ball_image,(32,32))
ball_rect=ball_image.get_rect()
ball_rect.center =(witdh/2,height/2)


#Pelicano
player1=pygame.image.load("pelicano.png")
player1_rect= player1.get_rect()
player1_rect.topleft=(0,height/2)

#Gallina
player2=pygame.image.load("gallina.png")
player2_rect= player2.get_rect()
player2_rect.topright=(witdh,height/2)

#puntos
fuente=pygame.font.SysFont("ariel.ttf",32)

puntos1_text=fuente.render("Puntos P1:"+str(puntos_p1),True,(0,0,0),(255,255,255))
puntos1_rect= puntos1_text.get_rect()
puntos1_rect. topleft = (64,64)

puntos2_text=fuente.render("Puntos P1:"+str(puntos_p2),True,(255,255,255),(0,0,0))
puntos2_rect= puntos2_text.get_rect()
puntos2_rect. topright = (witdh-64,64)

#Eleccion de direccion al iniciar
dx_inicio=random.choice(aleatorio)
dy_inicio=random.choice(aleatorio)


running = True

while running:
    
    print(f"dy: {dy}")
    print(f"dx: {dx}")
    
    ball_rect.x += dx * ball_velocity
    ball_rect.y += dy * ball_velocity

     #Rebote

    if ball_rect.left<=0 or ball_rect.right>= witdh:
        dx = -1 * dx

        if ball_rect.left<=0:
            puntos_p2 +=1
            puntos2_text=fuente.render("Puntos P2:"+str(puntos_p2),True,(255,255,255),(0,0,0))

             
        if ball_rect.right>= witdh:
            puntos_p1 +=1
            puntos1_text=fuente.render("Puntos P1:"+str(puntos_p1),True,(0,0,0),(255,255,255))

  


    if ball_rect.top<=64 or ball_rect.bottom>=height:
        dy = -1 * dy
    
    if player2_rect.colliderect(ball_rect):
        dx= -1 *dx
        dy= -1 *dy

    if player1_rect.colliderect(ball_rect):
        dx= -1 * dx
        dy= -1 * dy
          
    

    keys=pygame.key.get_pressed()

    #Mover la gallina

    if keys[pygame.K_UP] and player2_rect.top>64: 
            player2_rect.y-=5

    if keys[pygame.K_DOWN] and player2_rect.bottom<height:
            player2_rect.y+=5

    
    #Mover el pelicano

    if keys[pygame.K_w] and player1_rect.top>64: 
            player1_rect.y-=5

    if keys[pygame.K_s] and player1_rect.bottom<height:
            player1_rect.y+=5



    for event in pygame.event.get():
        #Cerrar juego
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill((0,0,0))
    pygame.draw.line(display_surface,(255,255,255),(witdh/2,0),(witdh/2,height),20)
    display_surface.blit(ball_image,ball_rect)
    display_surface.blit(puntos1_text,puntos1_rect)
    display_surface.blit(puntos2_text,puntos2_rect)
    display_surface.blit(player1,player1_rect)
    display_surface.blit(player2,player2_rect)

    clock.tick(FPS)
    pygame.display.update()


