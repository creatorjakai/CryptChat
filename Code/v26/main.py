import pygame
import socket
import time
import sys

def setup():
    global menu
    screen.fill((0, 0, 0))
    welcomemsg = f"Welcome to CryptChat {version}"
    text = font.render(welcomemsg, True, (255, 255, 255))
    text1 = font.render("[][][][][][][][][][]", True, (255, 255, 255))
    text2 = font.render("Continue", True, (0, 0, 0))
    screen.blit(text, (WINDOW_WIDTH // 2 - 170, WINDOW_HEIGTH // 2 - 300))
    screen.blit(text1, (WINDOW_WIDTH // 2 - 170, WINDOW_HEIGTH // 2 - 100))
    button_rect = pygame.draw.rect(screen, (255, 255, 255), (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGTH // 2 + 250, 200, 50), border_radius = 15)
    screen.blit(text2, (WINDOW_WIDTH // 2 - 55, WINDOW_HEIGTH // 2 + 265))
    pygame.display.flip()
    mouse_buttons = pygame.mouse.get_pressed(num_buttons=3)
    mouse_pos = pygame.mouse.get_pos()
    if mouse_buttons[0] and button_rect.collidepoint(mouse_pos):
        time.sleep(0.05)
        menu = "askname"
        return main()

def askname():
    global menu, username, user_name
    text = font.render("What is your name?", True, (255, 255, 255))
    text2 = font.render("Continue", True, (0, 0, 0))
    screen.fill((0, 0, 0))
    screen.blit(text, (WINDOW_WIDTH // 2 - 120, WINDOW_HEIGTH // 2 - 300))
    input_rect = pygame.Rect(WINDOW_WIDTH // 2 - 200, WINDOW_HEIGTH // 2, 400, 50)
    pygame.draw.rect(screen, (255, 255, 255), input_rect, border_radius=15)
    button_rect = pygame.Rect(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGTH // 2 + 250, 200, 50)
    pygame.draw.rect(screen, (255, 255, 255), button_rect, border_radius=15)
    screen.blit(text2, (WINDOW_WIDTH // 2 - 55, WINDOW_HEIGTH // 2 + 265))
    username = "".join(user_name)
    text1 = font.render(username, True, (0, 0, 0))
    text_rect = text1.get_rect(midleft=(input_rect.x + 10, input_rect.centery))
    screen.blit(text1, text_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if user_name:
                    user_name.pop()
            elif event.key == pygame.K_RETURN:
                if username:
                    menu = "chat"
                    return main()
            else:
                user_name.append(event.unicode)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and button_rect.collidepoint(event.pos):
                if username:
                    time.sleep(0.05)
                    menu = "chat"
                    return main()

def connect():
    global menu, serverip, server_ip
    text = font.render("What is the server ip?", True, (255, 255, 255))
    text2 = font.render("Connect", True, (0, 0, 0))
    screen.fill((0, 0, 0))
    screen.blit(text, (WINDOW_WIDTH // 2 - 120, WINDOW_HEIGTH // 2 - 300))
    input_rect = pygame.Rect(WINDOW_WIDTH // 2 - 200, WINDOW_HEIGTH // 2, 400, 50)
    pygame.draw.rect(screen, (255, 255, 255), input_rect, border_radius=15)
    button_rect = pygame.Rect(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGTH // 2 + 250, 200, 50)
    pygame.draw.rect(screen, (255, 255, 255), button_rect, border_radius=15)
    screen.blit(text2, (WINDOW_WIDTH // 2 - 55, WINDOW_HEIGTH // 2 + 265))
    serverip = "".join(server_ip)
    text1 = font.render(serverip, True, (0, 0, 0))
    text_rect = text1.get_rect(midleft=(input_rect.x + 10, input_rect.centery))
    screen.blit(text1, text_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if server_ip:
                    server_ip.pop()
            elif event.key == pygame.K_RETURN:
                if serverip:
                    menu = "connecttoserver"
                    return main()
            else:
                server_ip.append(event.unicode)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and button_rect.collidepoint(event.pos):
                if serverip:
                    time.sleep(0.05)
                    menu = "connecttoserver"
                    return main()

def connecttoserver():
    pass

def chat():
    global menu
    screen.fill((0, 0, 0))
    text = font.render("Chats", True, (255, 255, 255))
    screen.blit(text, (50, 5))
    pygame.draw.circle(screen, (120, 120, 120), (20, 20), 15)
    button_calls = pygame.draw.circle(screen, (120, 120, 120), (20, 60), 15)
    button_channels = pygame.draw.circle(screen, (120, 120, 120), (20, 100), 15)
    button_communities = pygame.draw.circle(screen, (120, 120, 120), (20, 140), 15)
    button_media = pygame.draw.circle(screen, (120, 120, 120), (20, 665), 15)
    button_account = pygame.draw.circle(screen, (120, 120, 120), (20, 705), 15)
    pygame.draw.line(screen, (120, 120, 120), (43, 0), (43, 725), width=3)
    pygame.draw.line(screen, (120, 120, 120), (350, 0), (350, 725), width=3)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_calls.collidepoint(event.pos) and menu != "calls":
                menu = "calls"
            elif button_channels.collidepoint(event.pos) and menu != "channels":
                menu = "channels"
            elif button_communities.collidepoint(event.pos) and menu != "communities":
                menu = "communities"
            elif button_media.collidepoint(event.pos) and menu != "media":
                menu = "media"
            elif button_account.collidepoint(event.pos) and menu != "account":
                menu = "account"

def calls():
    global menu
    screen.fill((0, 0, 0))
    text = font.render("Calls", True, (255, 255, 255))
    screen.blit(text, (50, 5))
    button_chat = pygame.draw.circle(screen, (120, 120, 120), (20, 20), 15)
    pygame.draw.circle(screen, (120, 120, 120), (20, 60), 15)
    button_channels = pygame.draw.circle(screen, (120, 120, 120), (20, 100), 15)
    button_communities = pygame.draw.circle(screen, (120, 120, 120), (20, 140), 15)
    button_media = pygame.draw.circle(screen, (120, 120, 120), (20, 665), 15)
    button_account = pygame.draw.circle(screen, (120, 120, 120), (20, 705), 15)
    pygame.draw.line(screen, (120, 120, 120), (43, 0), (43, 725), width=3)
    pygame.draw.line(screen, (120, 120, 120), (350, 0), (350, 725), width=3)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_chat.collidepoint(event.pos) and menu != "chat":
                menu = "chat"
            elif button_channels.collidepoint(event.pos) and menu != "channels":
                menu = "channels"
            elif button_communities.collidepoint(event.pos) and menu != "communities":
                menu = "communities"
            elif button_media.collidepoint(event.pos) and menu != "media":
                menu = "media"
            elif button_account.collidepoint(event.pos) and menu != "account":
                menu = "account"

def channels():
    global menu
    screen.fill((0, 0, 0))
    text = font.render("Channels", True, (255, 255, 255))
    screen.blit(text, (50, 5))
    button_chat = pygame.draw.circle(screen, (120, 120, 120), (20, 20), 15)
    button_calls = pygame.draw.circle(screen, (120, 120, 120), (20, 60), 15)
    pygame.draw.circle(screen, (120, 120, 120), (20, 100), 15)
    button_communities = pygame.draw.circle(screen, (120, 120, 120), (20, 140), 15)
    button_media = pygame.draw.circle(screen, (120, 120, 120), (20, 665), 15)
    button_account = pygame.draw.circle(screen, (120, 120, 120), (20, 705), 15)
    pygame.draw.line(screen, (120, 120, 120), (43, 0), (43, 725), width=3)
    pygame.draw.line(screen, (120, 120, 120), (350, 0), (350, 725), width=3)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_calls.collidepoint(event.pos) and menu != "calls":
                menu = "calls"
            elif button_chat.collidepoint(event.pos) and menu != "chat":
                menu = "chat"
            elif button_communities.collidepoint(event.pos) and menu != "communities":
                menu = "communities"
            elif button_media.collidepoint(event.pos) and menu != "media":
                menu = "media"
            elif button_account.collidepoint(event.pos) and menu != "account":
                menu = "account" 

def communities():
    global menu
    screen.fill((0, 0, 0))
    text = font.render("Communities", True, (255, 255, 255))
    screen.blit(text, (50, 5))
    button_chat = pygame.draw.circle(screen, (120, 120, 120), (20, 20), 15)
    button_calls = pygame.draw.circle(screen, (120, 120, 120), (20, 60), 15)
    button_channels = pygame.draw.circle(screen, (120, 120, 120), (20, 100), 15)
    pygame.draw.circle(screen, (120, 120, 120), (20, 140), 15)
    button_media = pygame.draw.circle(screen, (120, 120, 120), (20, 665), 15)
    button_account = pygame.draw.circle(screen, (120, 120, 120), (20, 705), 15)
    pygame.draw.line(screen, (120, 120, 120), (43, 0), (43, 725), width=3)
    pygame.draw.line(screen, (120, 120, 120), (350, 0), (350, 725), width=3)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_calls.collidepoint(event.pos) and menu != "calls":
                menu = "calls"
            elif button_channels.collidepoint(event.pos) and menu != "channels":
                menu = "channels"
            elif button_chat.collidepoint(event.pos) and menu != "chat":
                menu = "chat"
            elif button_media.collidepoint(event.pos) and menu != "media":
                menu = "media"
            elif button_account.collidepoint(event.pos) and menu != "account":
                menu = "account"

def media():
    global menu
    screen.fill((0, 0, 0))
    text = font.render("Media", True, (255, 255, 255))
    screen.blit(text, (50, 5))
    button_chat = pygame.draw.circle(screen, (120, 120, 120), (20, 20), 15)
    button_calls = pygame.draw.circle(screen, (120, 120, 120), (20, 60), 15)
    button_channels = pygame.draw.circle(screen, (120, 120, 120), (20, 100), 15)
    button_communities = pygame.draw.circle(screen, (120, 120, 120), (20, 140), 15)
    pygame.draw.circle(screen, (120, 120, 120), (20, 665), 15)
    button_account = pygame.draw.circle(screen, (120, 120, 120), (20, 705), 15)
    pygame.draw.line(screen, (120, 120, 120), (43, 0), (43, 725), width=3)
    pygame.draw.line(screen, (120, 120, 120), (350, 0), (350, 725), width=3)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_calls.collidepoint(event.pos) and menu != "calls":
                menu = "calls"
            elif button_channels.collidepoint(event.pos) and menu != "channels":
                menu = "channels"
            elif button_chat.collidepoint(event.pos) and menu != "chat":
                menu = "chat"
            elif button_communities.collidepoint(event.pos) and menu != "communities":
                menu = "communities"
            elif button_account.collidepoint(event.pos) and menu != "account":
                menu = "account"

def account():
    global menu
    screen.fill((0, 0, 0))
    text = font.render("Account", True, (255, 255, 255))
    screen.blit(text, (50, 5))
    button_chat = pygame.draw.circle(screen, (120, 120, 120), (20, 20), 15)
    button_calls = pygame.draw.circle(screen, (120, 120, 120), (20, 60), 15)
    button_channels = pygame.draw.circle(screen, (120, 120, 120), (20, 100), 15)
    button_communities = pygame.draw.circle(screen, (120, 120, 120), (20, 140), 15)
    button_media = pygame.draw.circle(screen, (120, 120, 120), (20, 665), 15)
    pygame.draw.circle(screen, (120, 120, 120), (20, 705), 15)
    pygame.draw.line(screen, (120, 120, 120), (43, 0), (43, 725), width=3)
    pygame.draw.line(screen, (120, 120, 120), (350, 0), (350, 725), width=3)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_calls.collidepoint(event.pos) and menu != "calls":
                menu = "calls"
            elif button_channels.collidepoint(event.pos) and menu != "channels":
                menu = "channels"
            elif button_chat.collidepoint(event.pos) and menu != "chat":
                menu = "chat"
            elif button_media.collidepoint(event.pos) and menu != "media":
                menu = "media"
            elif button_communities.collidepoint(event.pos) and menu != "communities":
                menu = "communities"

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
        elif menu == "connect":
            connect()
        elif menu == "connecttoserver":
            connecttoserver()
        elif menu == "chat":
            chat()
        elif menu == "calls":
            calls()
        elif menu == "channels":
            channels()
        elif menu == "communities":
            communities()
        elif menu == "media":
            media()
        elif menu == "account":
            account()

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
    global screen, loadprc, font, version, WINDOW_HEIGTH, WINDOW_WIDTH, user_name, username, clock, server_ip, serverip
    loadprc = 1
    pygame.init()
    pygame.display.init()
    pygame.font.init()

    version = "26.0.1"

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

    user_name = []
    username = ""

    server_ip = []
    serverip = ""

    clock = pygame.time.Clock()
    loadprcbar()

load()