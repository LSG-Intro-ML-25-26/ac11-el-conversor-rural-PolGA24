@namespace
class SpriteKind:
    Arbol = SpriteKind.create()
    Gallina = SpriteKind.create()
    Patata = SpriteKind.create()
    Cabra = SpriteKind.create()
    Huevo = SpriteKind.create()
    Caballo = SpriteKind.create()
"""

Variables globales

"""

def on_on_overlap(player2, vendedor):
    vendedor.say("Gallina: 6kg (Pulsa A)", 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.Gallina, on_on_overlap)

def on_on_overlap2(player22, vendedor2):
    vendedor2.say("Patata: Ratio 1.33 (Pulsa A)", 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.Patata, on_on_overlap2)

def on_down_pressed():
    animation.run_image_animation(nena,
        assets.animation("""
            nena-animation-down
            """),
        500,
        False)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_on_overlap3(player23, vendedor3):
    vendedor3.say("Cabra: 12kg (Pulsa A)", 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.Cabra, on_on_overlap3)

# Evento de choque (Usando los tipos correctos)

def on_on_overlap4(player24, arbol_tocado):
    global lenya_inventario
    # Efectos visuales
    arbol_tocado.start_effect(effects.fountain, 500)
    music.ba_ding.play()
    # Sumar inventario
    lenya_inventario += 1
    player24.say("Leña: " + ("" + str(lenya_inventario)), 1000)
    # Destruir y programar el renacimiento
    sprites.destroy(arbol_tocado)
    
    def esperar_y_renacer():
        pause(2000)
        crear_arbol_aleatorio()
    control.run_in_parallel(esperar_y_renacer)
    
sprites.on_overlap(SpriteKind.player, SpriteKind.Arbol, on_on_overlap4)

def on_right_pressed():
    animation.run_image_animation(nena,
        assets.animation("""
            nena-animation-right
            """),
        500,
        False)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_left_pressed():
    animation.run_image_animation(nena,
        assets.animation("""
            nena-animation-left
            """),
        500,
        False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_overlap5(player25, vendedor4):
    vendedor4.say("Caballo: 12kg (Pulsa A)", 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.Caballo, on_on_overlap5)

def on_on_overlap6(player26, vendedor5):
    vendedor5.say("Huevo: 12kg (Pulsa A)", 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.Huevo, on_on_overlap6)

def on_up_pressed():
    animation.run_image_animation(nena,
        assets.animation("""
            nena-animation-up
            """),
        500,
        False)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def crear_mercado():
    global gallina, patata, cabra, huevo, caballo
    # 1. Vendedor GALLINA
    gallina = sprites.create(assets.image("""
        pollo
        """), SpriteKind.Gallina)
    gallina.set_position(113, 73)
    gallina.set_flag(SpriteFlag.GHOST, False)
    # 2. Vendedor PATATA
    patata = sprites.create(assets.image("""
        patata
        """), SpriteKind.Patata)
    patata.set_position(106, 96)
    patata.set_flag(SpriteFlag.GHOST, False)
    # 3. Vendedor CABRA
    cabra = sprites.create(assets.image("""
        cabra
        """), SpriteKind.Cabra)
    cabra.set_position(140, 60)
    cabra.set_flag(SpriteFlag.GHOST, False)
    # 4. Vendedor HUEVOS
    huevo = sprites.create(assets.image("""
        egg
        """), SpriteKind.Huevo)
    huevo.set_position(140, 80)
    huevo.set_flag(SpriteFlag.GHOST, False)
    # 5. Vendedor CABALLO
    caballo = sprites.create(assets.image("""
        caballo
        """), SpriteKind.Caballo)
    caballo.set_position(140, 100)
    caballo.set_flag(SpriteFlag.GHOST, False)
def crear_arbol_aleatorio():
    global arbol
    arbol = sprites.create(assets.image("""
            treeSmallPine
            """),
        SpriteKind.Arbol)
    arbol.set_position(randint(10, 60), randint(40, 110))
arbol: Sprite = None
caballo: Sprite = None
huevo: Sprite = None
cabra: Sprite = None
patata: Sprite = None
gallina: Sprite = None
lenya_inventario = 0
nena: Sprite = None
eleccion = 0
scene.set_background_image(assets.image("""
    fondo
    """))
nena = sprites.create(assets.image("""
        vendedor-front
        """),
    SpriteKind.player)
controller.move_sprite(nena)
crear_mercado()
for index in range(6):
    # Crear el primer árbol al iniciar
    crear_arbol_aleatorio()