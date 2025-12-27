@namespace
class SpriteKind:
    Arbol = SpriteKind.create()
    Comerciante = SpriteKind.create()
# Variables globales

def on_down_pressed():
    animation.run_image_animation(nena,
        assets.animation("""
            nena-animation-down
            """),
        500,
        False)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

# Evento de choque (Usando los tipos correctos)

def on_on_overlap(player2, arbol_tocado):
    global lenya_inventario
    # Efectos visuales
    arbol_tocado.start_effect(effects.fountain, 500)
    music.ba_ding.play()
    # Sumar inventario
    lenya_inventario += 1
    player2.say("Leña: " + ("" + str(lenya_inventario)), 1000)
    # Destruir y programar el renacimiento
    sprites.destroy(arbol_tocado)
    
    def esperar_y_renacer():
        pause(2000)
        crear_arbol_aleatorio()
    control.run_in_parallel(esperar_y_renacer)
    
sprites.on_overlap(SpriteKind.player, SpriteKind.Arbol, on_on_overlap)

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

def on_up_pressed():
    animation.run_image_animation(nena,
        assets.animation("""
            nena-animation-up
            """),
        500,
        False)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def crear_arbol_aleatorio():
    global arbol
    arbol = sprites.create(assets.image("""
            treeSmallPine
            """),
        SpriteKind.Arbol)
    arbol.set_position(randint(10, 70), randint(20, 100))
arbol: Sprite = None
lenya_inventario = 0
nena: Sprite = None
scene.set_background_image(assets.image("""
    fondo
    """))
nena = sprites.create(assets.image("""
    nena-front
    """), SpriteKind.player)
controller.move_sprite(nena)
# Crear el primer árbol al iniciar
crear_arbol_aleatorio()