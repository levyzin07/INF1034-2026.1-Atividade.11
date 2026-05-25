import pygame

pygame.init()

# TELA
LARGURA = 1200
ALTURA = 700

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("3 Animações")

clock = pygame.time.Clock()

# ==========================
# SPRITESHEETS
# ==========================

sonic_sheet = pygame.image.load("sonic.png").convert_alpha()
miku_sheet = pygame.image.load("miku.png").convert_alpha()
spider_sheet = pygame.image.load("spiderman.png").convert_alpha()

# ==========================
# SONIC (ANIMAÇÃO CONSTANTE)
# ==========================

frames_sonic = []

for i in range(8):

    frame = sonic_sheet.subsurface(
        (0 + i*32,110,32,40)
    )

    frames_sonic.append(
        pygame.transform.scale(frame,(80,80))
    )

frame_sonic = 0
tempo_sonic = 0

# ==========================
# MIKU (SEGURANDO D)
# ==========================

frames_miku = []

for i in range(4):

    frame = miku_sheet.subsurface(
        (10+i*20,25,20,28)
    )

    frames_miku.append(
        pygame.transform.scale(frame,(80,100))
    )

frame_miku = 0
tempo_miku = 0

x_miku = 100
y_miku = 450

# ==========================
# SPIDERMAN (UMA VEZ)
# ==========================

animar_spider = False

frames_spider = []

for i in range(6):

    frame = spider_sheet.subsurface(
        (10+i*60,220,60,80)
    )

    frames_spider.append(
        pygame.transform.scale(frame,(120,120))
    )

frame_spider = 0

# ==========================
# LOOP
# ==========================

rodando = True

while rodando:

    clock.tick(60)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_SPACE:

                animar_spider = True
                frame_spider = 0

    teclas = pygame.key.get_pressed()

    tela.fill((30,30,30))

    # SONIC CONSTANTE
    tempo_sonic += 0.15

    if tempo_sonic >= len(frames_sonic):

        tempo_sonic = 0

    frame_sonic = int(tempo_sonic)

    tela.blit(
        frames_sonic[frame_sonic],
        (150,150)
    )

    # MIKU SEGURANDO D

    if teclas[pygame.K_d]:

        x_miku += 4

        tempo_miku += 0.2

        if tempo_miku >= len(frames_miku):

            tempo_miku = 0

    frame_miku = int(tempo_miku)

    tela.blit(
        frames_miku[frame_miku],
        (x_miku,y_miku)
    )

    # SPIDERMAN UMA VEZ

    if animar_spider:

        tela.blit(
            frames_spider[frame_spider],
            (800,350)
        )

        frame_spider += 0.2

        if frame_spider >= len(frames_spider):

            animar_spider = False

    pygame.display.update()

pygame.quit()