import pyglet, util
from pyglet.window import Window, key
from pyglet import image
from pyglet import sprite
from pyglet import clock
import random

#Globalne

win = Window(fullscreen = True)

batch = pyglet.graphics.Batch()
max_pilka_spin = 20
gora, dol, lewo, prawo = False, False, False, False

#Klasa obiekty fizyczne (kolizje)

def wrap(value, width):
    if value > width:
        value -= width
    if value < 0:
        value += width
    return value

class PhysicalObject(sprite.Sprite):
    rotation_speed = 0
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self):
        rotation = self.rotation + self.rotation_speed

        self.rotation = rotation
        self.check_bounds()

    def check_bounds(self):
        min_x = 0 + int(self.width/2)
        min_y = 0 + int(self.height/2)
        max_x = win.width - int(self.width/2)
        max_y = win.height - int(self.height/2)
        if self.x < min_x:
            self.x = min_x
        elif self.x > max_x:
            self.x = max_x
        if self.y < min_y:
            self.y = min_y
        elif self.y > max_y:
            self.y = max_y

#definiujemy piłkę

class Pilka(PhysicalObject):
    def __init__(self,  *args, **kwargs):
        super(Pilka, self).__init__(*args, **kwargs)
        self.rotation = random.random() * 360.
        self.rotation_speed = (random.random() - 0.5) * max_pilka_spin

class Gracz(PhysicalObject):
    def __init__(self,  *args, **kwargs):
        super(Gracz, self).__init__(*args, **kwargs)


papiez_pilka = image.load("obrazki/pilka.png")
papiez_pilka.anchor_x = int(papiez_pilka.width/2)
papiez_pilka.anchor_y = int(papiez_pilka.height/2)

papiez_player = image.load("obrazki/papiez.png")
papiez_player.anchor_x = int(papiez_player.width/2)
papiez_player.anchor_y = int(papiez_player.height/2)

pilka = Pilka(papiez_pilka, x=win.width / 2, y=win.height / 2)

#definiujemy papieża

gracz = Gracz(papiez_player, x=win.width/2, y=0)


def handle_collision_with(self, other_object):
    if other_object.__class__ == self.__class__:
        print(1)

gracz.scale = 0.5
pilka.scale = 0.25

@win.event
def on_key_press(symbol, modifier):
    global gora, dol, lewo, prawo
    if symbol == key.A:
        lewo = True
    elif symbol == key.D:
        prawo = True
    elif symbol == key.W:
        gora = True
    elif symbol == key.S:
        dol = True

@win.event
def on_key_release(symbol, modifiers):
    global gora, dol, lewo, prawo
    if symbol == key.W:
        gora = False
    elif symbol == key.A:
        lewo = False
    elif symbol == key.S:
        dol = False
    elif symbol == key.D:
        prawo = False

@win.event
def moveT(dt):
    if gora == True:
        gracz.y += 5
    elif dol == True:
        gracz.y -= 5
    if lewo == True:
        gracz.x -= 5
        gracz.rotation = 0
    elif prawo == True:
        gracz.x += 5
        gracz.rotation = 0

@win.event
def on_draw():
    win.clear()
    gracz.draw()
    pilka.draw()
    pilka.update()
    gracz.update()

clock.schedule_interval(moveT, 1 / 60)
pyglet.app.run()

#TODO: Zrobić kolizje obiektów
#TODO: Dodać odbijanie piłki
#TODO: Dodać tło
#TODO: Dodać kosz (nie obiekt)
#TODO: Dodać zdobywanie punktów za piłkę która wpada do kosza
#TODO: Dodać obiekt, który blokuje piłę od boku kosza
#TODO: Zablokować wpadanie piłki do kosza od dołu