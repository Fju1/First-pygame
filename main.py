import pygame
pygame.init()

okno = pygame.display.set_mode((400, 300))               #vytvori okno o zadane velikosti
pygame.display.set_caption("test pygame")                #prida oknu nazev

x = 100
y = 100
sirka = 20
vyska = 35
velocity = 3

run = True
while run:
    pygame.time.delay(100)                     #delay programu

    for event in pygame.event.get():           #ziska input
        if event.type == pygame.QUIT:           
            run = False

    keys = pygame.key.get_pressed()            #ziska input, naslende posouva obdelnik

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        y += velocity
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        x += velocity

    okno.fill((0,0,0))                        #aktualizuje uvodni okno, aby byl videt jen aktualni obdelnik

    pygame.draw.rect(okno, (0,255,0), (x,y,sirka,vyska))   #nakresli obdelnik
    pygame.display.update()                                #aktualiyuje okno

pygame.quit()                                   #ukonci program