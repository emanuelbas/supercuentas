from clases import Cursor,Boton
import pygame

def about():
#Pantalla acerca de
    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Supercuentas")
    salir=False
    reloj1=pygame.time.Clock()
    fondo=pygame.image.load("imagenes/blackboard.jpeg")
    fuente1=pygame.font.Font("fuentes/EraserDust.ttf", 30)
    fuente2=pygame.font.Font("fuentes/EraserDust.ttf", 20)
    boton_volver = Boton(300,500,400,530,"Volver",30,(255,255,255),"fuentes/EraserDust.ttf")
    boton_titulo = Boton(130,20,211,158,"Acerca de Supercuentas!",45,(200,200,50),"fuentes/EraserDust.ttf")
    
    texto1= Boton(20,150,400,530,"Supercuentas! fue desarrollado por",20,(50,255,255),"fuentes/EraserDust.ttf")
    texto2= Boton(20,175,400,530,"Bravin Federico y Bastons Emanuel el anio 2013",20,(50,255,255),"fuentes/EraserDust.ttf")
    texto3= Boton(20,200,400,530,"Musica y sonidos: http://freesound.org/",20,(50,255,255),"fuentes/EraserDust.ttf")
    texto4= Boton(20,225,400,530,"los demas elementos multimedia son recopilacion de la web",20,(50,255,255),"fuentes/EraserDust.ttf")
    texto5= Boton(20,250,400,530,"",20,(50,255,255),"fuentes/EraserDust.ttf")



    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.es_presionado():
                    salir = True


        pantalla.fill((30,30,200))
        pantalla.blit(fondo,(0,0))
        texto1.update(pantalla)
        texto2.update(pantalla)
        texto3.update(pantalla)
        texto4.update(pantalla)
        texto5.update(pantalla)
        
        reloj1.tick(15)        

        boton_volver.update(pantalla)
        boton_titulo.update(pantalla)
        pygame.display.update()


