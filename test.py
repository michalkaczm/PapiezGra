import pyglet
import util
from pyglet.window import Window, key
from pyglet import image
from pyglet import sprite
from pyglet import clock


win = Window(width=1280, height=720)

batch = pyglet.graphics.Batch()
gora, dol, lewo, prawo = False, False, False, False

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

    # def collision_detect(self):
    #     for i in range(len(game_objects)):
    #         for j in range(i + 1, len(game_objects)):
    #             obj_1 = game_objects[i]
    #             obj_2 = game_objects[j]
    #             if util.collides_with(obj_1, obj_2):
    #                 return True
    #                 """Chyba się zapierdole ni chuja nic nie mogę wymyśleć"""

gracz =

pilka =









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