import pygame
import random

import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Загружаем звуковые эффекты
shoot_sound = pygame.mixer.Sound("sounds/shut.wav")
explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/Shuter.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/Target.png")
explosion_img = pygame.image.load("img/explosion3.png")  # Загрузка изображения взрыва
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

score = 0
font = pygame.font.Font(None, 36)

target_speed_x = random.randint(-1, 1)
target_speed_y = random.randint(-1, 1)

# Отключаем видимость стандартного курсора мыши
pygame.mouse.set_visible(False)

# Загружаем изображение прицела и получаем его прямоугольник
crosshair_image = pygame.image.load("img/pricel.png").convert_alpha()
crosshair_rect = crosshair_image.get_rect()

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            shoot_sound.play(
                maxtime=1000)  # Воспроизвести звук выстрела, maxtime ограничивает воспроизведение 1000 мс
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                screen.blit(explosion_img, (target_x, target_y))  # Отображение взрыва при попадании
                explosion_sound.play(maxtime=2000)
                pygame.display.update()
                pygame.time.wait(2000)  # Задержка для отображения взрыва

                # Перемещение цели в новое местоположение
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Меняем направление движения цели
                target_speed_x = random.randint(-1, 1)
                target_speed_y = random.randint(-1, 1)

    # Движение цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Отскок от краев экрана
    if target_x < 0 or target_x > SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y < 0 or target_y > SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    screen.blit(target_img, (target_x, target_y))

    # Отображение счета
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Получаем текущее положение мыши
    mouse_pos = pygame.mouse.get_pos()

    # Позиционируем прицел на курсоре
    crosshair_rect.center = mouse_pos

    # Рисуем изображение прицела на его новом местоположении
    screen.blit(crosshair_image, crosshair_rect)

    pygame.display.update()

pygame.quit()