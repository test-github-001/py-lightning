import sys # импорт модуля sys, для правильного выхода из игры

from random import random, randint
from math import sin, pi

import pygame as PG # Импортируем pygame в переменную PG
PG.init() # инициализируем pygame (без этого не работают шрифты и некоторый функционал)

# размеры игрового окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FPS = 60 # частота обновления экрана
CLOCK = PG.time.Clock() # создаем счетчик обновления экрана

SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # создаем игровое окно (заданной в константах ширины и высоты)
# ОПЦИОНАЛЬНО
# PG.mouse.set_visible(False) # отключаем отображение курсора мыши
# ICON = PG.image.load('./src/images/icon.png').convert_alpha() # загружаем иконку для окна игры
# PG.display.set_icon(ICON) # устанавливаем игровому окну иконку
# PG.display.set_caption('Lightning') # устанавливаем игровому окну заголовок

# НАСТРОЙКИ ДЛЯ МОЛНИЙ
lightning_duration_min = 0.1 * FPS
lightning_duration_max = 0.2 * FPS

lightning_delay_min = 0.5 * FPS
lightning_delay_max = 2.0 * FPS

lightning_duration = randint( int(lightning_duration_min), int(lightning_duration_max) )
lightning_delay = randint( int(lightning_delay_min), int(lightning_delay_max) )
lxs = randint(50, SCREEN_WIDTH - 50)
lxe = randint(50, SCREEN_WIDTH - 50)

is_lightning = False

# lightning_colors
lc1 = (255, 255, 255)
lc2 = (255, 255,   0)
lc3 = (  0, 255, 255)
lightning_colors_list = [lc1, lc2, lc3, lc1, lc3, lc1]
def get_lightning_color():
    return lightning_colors_list[ randint(0, len(lightning_colors_list) - 1) ]

def get_distance(x1, y1, x2, y2):
    dy = x1 - x2
    dx = y1 - y2
    return (dx * dx + dy * dy)**0.5

def drawLightning(xs, ys, xe, ye):
    color = get_lightning_color()
    distance = get_distance(xs, ys, xe, ye);
    xx, yy = xs, ys
    x0, y0 = xs, ys
    stepsCount = 1 + int( random() * distance / 3 )
    for i in range(stepsCount):
        n = stepsCount - i
        pathLength = get_distance(xx, yy, x0, y0)
        offset = sin(pathLength / distance * pi) * 5
        xx += (xe - xx) / n + random() * offset * 2 - offset
        yy += (ye - yy) / n + random() * offset * 2 - offset
        PG.draw.line(SCREEN, color, (xs, ys), (xx, yy), 2)
        xs, ys = xx, yy


# ИГРОВОЙ ЦИКЛ
is_on_loop = True # цикл запущен
while is_on_loop:
    CLOCK.tick(FPS) # ждем следующий кадр (время следующего обновления экрана)

    SCREEN.fill( (0,0,0) )

    PG.draw.line(SCREEN, (255, 0, 0), (10, 10), (50, 50), 3) # ЛИНИЯ (экран, цвет, начало, конец, толщина)
    PG.draw.rect(SCREEN, (0, 255, 0), (100, 10, 50, 20)) # ЛИНИЯ (экран, цвет, координаты, (не обязательно - толщина границы))
    PG.draw.polygon(SCREEN, (0, 255, 0), [[10, 100], [10, 200], [110, 150]], 5) # ПОЛИГОН (экран, цвет, координаты, (не обязательно - толщина границы))
    PG.draw.circle(SCREEN, (255, 255, 0), (300, 300), 25, 5) # ОКРУЖНОСТЬ (экран, цвет, координаты центра, радиус, (не обязательно - толщина границы))
    PG.draw.ellipse(SCREEN, (255, 255, 0), (100, 250, 200, 100), 5) # ЭЛЛИПС (экран, цвет, координаты, радиус, (не обязательно - толщина границы))
    PG.draw.arc(SCREEN, (0, 0, 255), (100, 400, 100, 100), pi, 2*pi, 3) # ДУГА (экран, цвет, координаты, начало дуги, конец дуги, (не обязательно - толщина границы))
    
    
    if lightning_delay > 0:
        lightning_delay -= 1
    else:
        if lightning_duration > 0:
            lightning_duration -= 1
            drawLightning(lxs, 0, lxe, SCREEN_HEIGHT)
        else:
            lightning_duration = randint( int(lightning_duration_min), int(lightning_duration_max) )
            lightning_delay = randint( int(lightning_delay_min), int(lightning_delay_max) )
            lxs = randint(10, SCREEN_WIDTH - 10)
            lxe = randint(10, SCREEN_WIDTH - 10)

    PG.display.flip() # обновляем экран

    # получаем все события
    for event in PG.event.get():
        # останавливаем игровой цикл если было закрыто окно или нажата клавиша ESCAPE
        if event.type == PG.QUIT: # проверка закрытия игрового окна
            is_on_loop = False # останавливаем главный цикл игры
        if event.type == PG.KEYDOWN and event.key == PG.K_ESCAPE: # если нажата кнопка ESCAPE (ESC)
            is_on_loop = False # останавливаем главный цикл игры

# завершение выполнения программы
PG.quit() # выходим из Pygame
sys.exit() # выключаем программу

