import os

from controller.config_init_game_controller import *

#  (parametros)
altura = 650 # ALTURA DA WINDOW
largura = 900  # LARGURA DA WINDOW
w = 15 # LARGURA DA GRID
h = 15 # ALTURA DA GRID
m = 1 # MARGEM DOS BLOCOS DA GRID
M = 20 # LARGURA DOS BLOCOS DA DA GRID
H = 20 # ALTURA DOS BLOCOS DA DA GRID

config = ConfigInitGameController()
screen = config.screen(largura, altura)
grid1 = config.grid(15, 15)
grid2 = config.grid(15, 15)
WIDTH, HEIGHT, MARGIN = config.draw_grid(20, 20, 1)
clock = pygame.time.Clock()

def quit_game():
    pygame.display.quit()
# end method quit_game

def menu_game():
    im_menu = pygame.image.load(
        '/home/leobidoous/Documentos/UNIVERSIDADE/TECNOLOGIA E CONSTRUÇÃO DE SOFTWARE/TRAB_DISTRIBUÍDO/images/menu_batalha_naval.png')
    screen.blit(im_menu, [0, 0])
# end method menu_game

def menu_credits():
    im_credits = pygame.image.load(
        '/home/leobidoous/Documentos/UNIVERSIDADE/TECNOLOGIA E CONSTRUÇÃO DE SOFTWARE/TRAB_DISTRIBUÍDO/images/creditos_batalha_naval.png')
    screen.blit(im_credits, [0, 0])
    credits = False
    while not credits:
        for event in pygame.event.get():  # User did something
            try:
                if event.type == pygame.QUIT:  # If user clicked close
                    credits = True  # Flag that we are done so we exit this loop
                    quit_game()
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if x >= 0 and y >= 424 and x <= 182 and y <= 470:
                        return 0
            except:
                print("erro")
        clock.tick(60)  # Limit to 60 frames per second
        try:
            pygame.display.update()  # Go ahead and update the screen with what we've drawn.
        except:
            break
# end method menu_credits

def start_menu_game():
    # Variável para controlar o jogo
    done = False
    while not done:
        screen.fill(config.background_color('white'))
        menu_game()
        for event in pygame.event.get():  # User did something
            try:
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                    quit_game()
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if x >= 0 and y >= 48 and x <= 180 and y <= 90:
                        arg0 = wait_players()
                        start_game(arg0)
                    if x >= 0 and y >= 115 and x <= 180 and y <= 157:
                        screen.fill(config.background_color('white'))
                        menu_credits()
                    if x >= 0 and y >= 183 and x <= 180 and y <= 225:
                        quit_game()
                        return 0
            except socket.error as err:
                print("erro", err)
        clock.tick(60) # Limit to 60 frames per second
        try:
            pygame.display.update() # Go ahead and update the screen with what we've drawn.
        except:
            break
# end method start_menu_game

def wait_players():
    request = RequestConnectionsController()
    accept = AcceptConnectionsController()
    try:
        request.request()
        return 'Player 2'
    except:
        try:
            accept.listen()
            return 'Player 1'
        except socket.error as err:
            print(err)
# end method wait_players

def start_game(arg0):
    # Variável para controlar o jogo
    done = False
    while not done:
        screen.fill(config.background_color('white'))
        for event in pygame.event.get():  # User did something
            try:
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                    quit_game()
                    return 0
            except:
                print("erro")

        font = pygame.font.SysFont(None, 30)
        text = font.render(arg0, True, config.background_color('green'))
        pygame.draw.rect(screen, config.background_color('black'), [0, altura * 0.05, largura * (1 / 3), 27])
        screen.blit(text, [largura/2, altura/2])

        # Update screen ever 30 frames per second
        clock.tick(30)  # Limit to 30 frames per second
        try:
            pygame.display.update() # Go ahead and update the screen with what we've drawn.
        except:
            break
# end method start_game