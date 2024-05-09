import pygame, random
from sudden_death import sudendeath


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
fuente=pygame.font.SysFont("ariel.ttf",32)

puntos1_text=fuente.render("Puntos P1:"+str(puntos_p1),True,(0,0,0),(255,255,255))
puntos1_rect= puntos1_text.get_rect()
puntos1_rect. topleft = (64,64)

puntos2_text=fuente.render("Puntos P1:"+str(puntos_p2),True,(255,255,255),(0,0,0))
puntos2_rect= puntos2_text.get_rect()
puntos2_rect. topright = (witdh-64,64)

#Tiempo
time_text= fuente.render("Time:" +str(tiempo)+"seg",True,(255,255,255),(0,0,0))
time_rect= time_text.get_rect()
time_rect. center=(witdh/2,64)

#Eleccion de direccion al iniciar
dx_inicio=random.choice(aleatorio)
dy_inicio=random.choice(aleatorio)


def Reiniciar():
    global puntos_p1,puntos_p2,tiempo,running2
     
    paused = True

    while paused:

        for evento in pygame.event.get():
                
            if evento.type == pygame.KEYDOWN:
                    
                puntos_p1=0
                puntos_p2=0
                player1_rect.topleft=(0,height/2)
                player2_rect.topright=(witdh,height/2)
                ball_rect.center =(witdh/2,height/2)
                tiempo =120

                paused = False
                running2= False

def Move():

    ball_velocity=2

    aleatorio=[-1,1]
    dx=random.choice(aleatorio)
    dy=random.choice(aleatorio)

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



running = True

while running:

    
    frame_count +=1

    if frame_count == FPS:
        tiempo -=1
        frame_count=0

        if (tiempo == 90) or (tiempo == 60) or (tiempo == 30) or (tiempo == 15):
         
             ball_velocity +=1

    time_text= fuente.render("Time:" +str(tiempo)+" seg",True,(255,255,255),(0,0,0))


    
    if tiempo == 0:
         
            
        if puntos_p1 > puntos_p2:
                 
                win1= pygame.image.load("win1.jpg")
                win1=pygame.transform.scale(win1,(witdh,height))
                display_surface.blit(win1,(0,0))
                pygame.display.update()
                Reiniciar()

                
        if puntos_p2 > puntos_p1:
                 
                win2= pygame.image.load("win2.jpg")
                win2=pygame.transform.scale(win2,(witdh,height))
                display_surface.blit(win2,(0,0))
                pygame.display.update()
                Reiniciar()

        if puntos_p2 == puntos_p1:
             
             sd=pygame.image.load("finalfight.jpg")
             sd=pygame.transform.scale(sd,(witdh,height))
             display_surface.blit(sd,(0,0))
             pygame.display.update()
             pygame.time.delay(2000)

             running2 = True

             while running2:
             
                for i in elmo:
                    fondo=pygame.image.load(i)
                    fondo=pygame.transform.scale(fondo,(witdh,height))
                    display_surface.blit(fondo,(0,0))
                    display_surface.blit(player1,player1_rect)
                    display_surface.blit(player2,player2_rect)
                    display_surface.blit(ball_image,ball_rect)
                    pygame.time.delay(20)
                    pygame.display.update()

                if running2 == True:
                    

                    ball_rect.x += dx * 40
                    ball_rect.y += dy *40

                    #Rebote

                    if ball_rect.left<=0 or ball_rect.right>= witdh:
                        dx = -1 * dx

                        if ball_rect.left<=0:
                            puntos_p2 +=1
                            puntos2_text=fuente.render("Puntos P2:"+str(puntos_p2),True,(255,255,255),(0,0,0))
                            ball_rect.center =(witdh/2,height/2)
                            ball_rect.x += dx * ball_velocity
                            dy=random.choice(aleatorio)
                            ball_rect.y += dy * ball_velocity
                            

                            
                        if ball_rect.right>= witdh:
                            puntos_p1 +=1
                            puntos1_text=fuente.render("Puntos P1:"+str(puntos_p1),True,(0,0,0),(255,255,255))
                            ball_rect.center =(witdh/2,height/2)
                            ball_rect.x += dx * ball_velocity
                            dy=random.choice(aleatorio)
                            ball_rect.y += dy * ball_velocity
                            

                        if puntos_p1 > puntos_p2:
                 
                            win1= pygame.image.load("win1.jpg")
                            win1=pygame.transform.scale(win1,(witdh,height))
                            display_surface.blit(win1,(0,0))
                            pygame.display.update()
                            Reiniciar()

                
                        if puntos_p2 > puntos_p1:
                                
                                win2= pygame.image.load("win2.jpg")
                                win2=pygame.transform.scale(win2,(witdh,height))
                                display_surface.blit(win2,(0,0))
                                pygame.display.update()
                                Reiniciar()


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
                            player2_rect.y-=100

                    if keys[pygame.K_DOWN] and player2_rect.bottom<height:
                            player2_rect.y+=100
                    
                    #Mover el pelicano

                    if keys[pygame.K_w] and player1_rect.top>64: 
                            player1_rect.y-=100

                    if keys[pygame.K_s] and player1_rect.bottom<height:
                            player1_rect.y+=100


                    for event in pygame.event.get():
                        #Cerrar juego
                        if event.type == pygame.QUIT:
                            running2 = False

                    pygame.display.update()


             
                        

         
    print(f" La velocidad es:{ball_velocity}")

    """print(f"dy: {dy}")
    print(f"dx: {dx}")"""
    
    ball_rect.x += dx * ball_velocity
    ball_rect.y += dy * ball_velocity

     #Rebote

    if ball_rect.left<=0 or ball_rect.right>= witdh:
        dx = -1 * dx

        if ball_rect.left<=0:
            puntos_p2 +=1
            puntos2_text=fuente.render("Puntos P2:"+str(puntos_p2),True,(255,255,255),(0,0,0))
            ball_rect.center =(witdh/2,height/2)
            ball_rect.x += dx * ball_velocity
            dy=random.choice(aleatorio)
            ball_rect.y += dy * ball_velocity

             
        if ball_rect.right>= witdh:
            puntos_p1 +=1
            puntos1_text=fuente.render("Puntos P1:"+str(puntos_p1),True,(0,0,0),(255,255,255))
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
    display_surface.blit(time_text,time_rect)

    
    clock.tick(FPS)
    pygame.display.update()


