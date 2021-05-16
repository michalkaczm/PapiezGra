import pyglet
import util
from pyglet.window import Window, key
from pyglet import image
from pyglet import sprite
from pyglet import clock
import random

#Globalne

# win = Window(fullscreen = True)
win = Window(width=1280, height=720)

batch = pyglet.graphics.Batch()
max_pilka_spin = 20
gora, dol, lewo, prawo = False, False, False, False

# centruje punkt odniesienia (np. obrotu) obrazka img
def center_anchor(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

# kurwa nie wiadomo co robi, aktualnie unused

#Klasa obiekty fizyczne (kolizje)
class PhysicalObject(sprite.Sprite):
    rotation_speed = 0
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
    # odpowiada za rotacje pilki (jesli self.rotation i rotation_speed podane) i wywoluje check_bounds
    def update(self):
        rotation = self.rotation + self.rotation_speed  #
        self.rotation = rotation                        #do wywalenia w przyszlosci
        self.check_bounds()
        self.collision_detect()
    #dba o to by obiekt nie wylatywał poza ekran
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

    def collision_detect(self):
        for i in range(len(game_objects)):
            for j in range(i + 1, len(game_objects)):
                obj_1 = game_objects[i]
                obj_2 = game_objects[j]
                if util.collides_with(obj_1, obj_2):
                    return True
                    """Chyba się zapierdole ni chuja nic nie mogę wymyśleć"""

class Pilka(PhysicalObject):
    def __init__(self,  *args, **kwargs):
        super(Pilka, self).__init__(*args, **kwargs)
        # vvv podane wartosci dla obrotu (rotation)
        self.rotation = random.random() * 360.
        self.rotation_speed = (random.random() - 0.5) * max_pilka_spin

    def collision_detect(self):
        for i in range(len(game_objects)):
            for j in range(i + 1, len(game_objects)):
                obj_1 = game_objects[i]
                obj_2 = game_objects[j]
                if util.collides_with(obj_1, obj_2):
                    return True
                    #odbij się i wypierdol


class Gracz(PhysicalObject):
    def __init__(self,  *args, **kwargs):
        super(Gracz, self).__init__(*args, **kwargs)

# ładujemy obrazki
papiez_pilka = image.load("obrazki/pilka.png")
center_anchor(papiez_pilka)

papiez_player = image.load("obrazki/papiez.png")
center_anchor(papiez_player)

#   definiujemy piłkę
pilka = Pilka(papiez_pilka, x=win.width / 2, y=win.height / 2)

#   definiujemy papieża
gracz = Gracz(papiez_player, x=win.width/2, y=0)

game_objects = gracz, pilka # bounds, kosz, wielkie_dildo,

# nieudolnie próbujemy ogarnąć kolizje
# def handle_collision_with(self, other_object):
#     if other_object.__class__ == self.__class__:
#         print(1)

# ustawiamy skale obrazkow żeby papież nie był zbyt duży a piłka zbyt mała
gracz.scale = 0.5
pilka.scale = 0.25

# ogarniamy sterowanie klawiaturą
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
    elif prawo == True:
        gracz.x += 5

@win.event
def on_draw():
    win.clear()
    gracz.draw()
    pilka.draw()
    pilka.update()
    gracz.update()

# ustawiamy zegarek żeby rzeczy się działy w czasie (to jest do ruszania się)
clock.schedule_interval(moveT, 1 / 60)

# uruchamiamy aplikację
pyglet.app.run()

#TODO: Zrobić kolizje obiektów
#TODO: Dodać odbijanie piłki
#TODO: Dodać tło
#TODO: Dodać kosz (nie obiekt)
# kosz może być obiektem, tylko bez odbijania po wykryciu kolizji (punkt zamiast tego) /Bizon
#TODO: Dodać zdobywanie punktów za piłkę która wpada do kosza
#TODO: Dodać obiekt, który blokuje piłę od boku kosza
#TODO: Zablokować wpadanie piłki do kosza od dołu