import pygame
import socket
import time
import sys

def setup():
    global menu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))
    welcomemsg = f"Welcome to CryptChat {version}"
    text = font.render(welcomemsg, True, (255, 255, 255))
    text1 = font.render("[][][][][][][][][][]", True, (255, 255, 255))
    text2 = font.render("Continue", True, (0, 0, 0))
    screen.blit(text, (WINDOW_WIDTH // 2 - 170, WINDOW_HEIGTH // 2 - 300))
    screen.blit(text1, (WINDOW_WIDTH // 2 - 170, WINDOW_HEIGTH // 2 - 100))
    pygame.draw.rect(screen, (255, 255, 255), (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGTH // 2 + 250, 200, 50), border_radius = 15)
    screen.blit(text2, (WINDOW_WIDTH // 2 - 55, WINDOW_HEIGTH // 2 + 265))
    pygame.display.flip()
    mouse_buttons = pygame.mouse.get_pressed(num_buttons=3)
    if mouse_buttons[0]:
        menu = "askname"
        return main()

def askname():
    screen.fill((0, 0, 0))
    pygame.display.flip()

def chat():
    pass

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if menu == "setup":
            setup()
        elif menu == "askname":
            askname()
        elif menu == "chats":
            chat()

def loadprcbar():
    global menu
    loadprc = 1
    for i in range(99):
        pygame.draw.rect(screen, (255, 255, 255), (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGTH // 2 + 100, loadprc * 2, 10), border_radius = 15)
        pygame.display.flip()
        loadprc += 1
        time.sleep(0.01)
    time.sleep(1)
    menu = "setup"
    main()


def load():
    global screen, loadprc, font, version, WINDOW_HEIGTH, WINDOW_WIDTH
    loadprc = 1
    pygame.init()
    pygame.display.init()
    pygame.font.init()

    version = "26.0.0"

    WINDOW_WIDTH = 1200
    WINDOW_HEIGTH = 725
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))

    icon = pygame.transform.scale(pygame.image.load("Assets/logo.png"), (250, 250))
    pygame.display.set_icon(icon)
    pygame.display.set_caption(f"CryptChat {version}")
    screen.fill((0, 0, 0))
    screen.blit(icon, ((WINDOW_WIDTH // 2 - 125), (WINDOW_HEIGTH / 2 - 200)))
    pygame.display.flip()

    font = pygame.font.SysFont("Arial", 25, bold=True)

    image_typipbar = pygame.image.load("Assets/Images/typipbar.png")
    button_ok = pygame.image.load("Assets/Buttons/ok.png")
    button_send = pygame.image.load("Assets/Buttons/send.png")
    loadprcbar()

load()
