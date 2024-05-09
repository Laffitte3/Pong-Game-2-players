import pygame, random


pygame.init()

witdh=900
height=600

display_surface= pygame.display.set_mode((witdh,height))

FPS=60
clock= pygame.time.Clock()
puntos_p1=0
puntos_p2=0

tiempo=5
frame_count=0

def sudendeath():

        global puntos_p1,puntos_p2


        elmo=["frame-01.gif","frame-02.gif","frame-03.gif","frame-04.gif","frame-05.gif","frame-06.gif",
        "frame-07.gif","frame-08.gif","frame-09.gif","frame-10.gif","frame-11.gif","frame-12.gif",]


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


        running2=True

        while running2:

                if puntos_p1==0 and puntos_p2==0: 


                        for i in elmo:
                                fondo=pygame.image.load(i)
                                fondo=pygame.transform.scale(fondo,(witdh,height))
                                display_surface.blit(fondo,(0,0))
                                pygame.time.delay(10)
                                display_surface.blit(player1,player1_rect)
                                display_surface.blit(player2,player2_rect)
                                display_surface.blit(ball_image,ball_rect)

                        ball_rect.x += dx * ball_velocity
                        ball_rect.y += dy * ball_velocity

                        if player2_rect.colliderect(ball_rect):
                                dx= -1 *dx
                                dy=random.choice(aleatorio)

                        if player1_rect.colliderect(ball_rect):
                                dx= -1 * dx
                                dy=random.choice(aleatorio)

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
                                
                        
                        if puntos_p1 ==1:
                                win1= pygame.image.load("win1.jpg")
                                win1=pygame.transform.scale(win1,(witdh,height))
                                display_surface.blit(win1,(0,0))
                                pygame.display.update()
                                

                        if puntos_p2 == 1:
                        
                                win2= pygame.image.load("win2.jpg")
                                win2=pygame.transform.scale(win2,(witdh,height))
                                display_surface.blit(win2,(0,0))
                                pygame.display.update()
                                

                
        
        
                                ball_rect.x += dx * ball_velocity
                                ball_rect.y += dy * ball_velocity

                                #Rebote

                                if ball_rect.left<=0 or ball_rect.right>= witdh:
                                        dx = -1 * dx

                                        if ball_rect.left<=0:
                                                puntos_p2 +=1
                                                ball_rect.center =(witdh/2,height/2)
                                                ball_rect.x += dx * ball_velocity
                                                dy=random.choice(aleatorio)
                                                ball_rect.y += dy * ball_velocity

                                        
                                        if ball_rect.right>= witdh:
                                                puntos_p1 +=1
                                                ball_rect.center =(witdh/2,height/2)
                                                ball_rect.x += dx * ball_velocity
                                                dy=random.choice(aleatorio)
                                                ball_rect.y += dy * ball_velocity


                                if ball_rect.top<=64 or ball_rect.bottom>=height:
                                        dy = -1 * dy
                                
                                if player2_rect.colliderect(ball_rect):
                                        dx= -1 *dx
                                        dy=random.choice(aleatorio)

                                if player1_rect.colliderect(ball_rect):
                                        dx= -1 * dx
                                        dy=random.choice(aleatorio)
                                        
                                

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



                                
                                clock.tick(FPS)
                                pygame.display.update()


