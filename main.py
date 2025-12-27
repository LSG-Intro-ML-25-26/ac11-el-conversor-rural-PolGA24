@namespace
class SpriteKind:
    Arbol = SpriteKind.create()
    Gallina = SpriteKind.create()
    Patata = SpriteKind.create()
    Cabra = SpriteKind.create()
    Huevo = SpriteKind.create()
    Caballo = SpriteKind.create()
# Variables globales

def on_on_overlap(player2, vendedor):
    vendedor.say("Gallina: 6kg (Pulsa A)", 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.Gallina, on_on_overlap)

def on_on_overlap2(player26, vendedor5):
    vendedor5.say("Huevo: 12kg (Pulsa A)", 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.Huevo, on_on_overlap2)

def on_down_pressed():
    animation.run_image_animation(nena,
        assets.animation("""
            nena-animation-down
            """),
        500,
        False)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

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

# Evento de choque

def on_on_overlap3(player24, arbol_tocado):
    global lenya_inventario
    # Confeti
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
    
sprites.on_overlap(SpriteKind.player, SpriteKind.Arbol, on_on_overlap3)

# Comprar con el boton A

def on_a_pressed():
    global lenya_inventario
    if nena.overlaps_with(gallina):
        coste_unitario = 6
        game.splash("GALLINERO")
        cantidad = game.ask_for_number("¿Cuántas gallinas quieres?", 1)
        if cantidad != int(cantidad):
            game.splash("¡Error! No vendemos medias gallinas.")

        if cantidad > 0:
            total_lenya = cantidad * coste_unitario
            if lenya_inventario >= total_lenya:
                if game.ask("Son " + ("" + str(total_lenya)) + "kg de leña. ¿Aceptas?"):
                    lenya_inventario += 0 - total_lenya
                    game.splash("¡Compra realizada!", "Gallinas: " + ("" + str(cantidad)))
            else:
                game.splash("No tienes suficiente leña.",
                    "Necesitas: " + ("" + str(total_lenya)))
    elif nena.overlaps_with(patata):
        ratio_conversion = 1.3333
        game.splash("HUERTO PATATAS")
        kilos_patata = game.ask_for_number("¿Kg de patatas?")
        if kilos_patata > 0:
            calculo_bruto = kilos_patata * ratio_conversion
            coste_final = int(calculo_bruto * 100) / 100
            if lenya_inventario >= coste_final:
                if game.ask("Coste: " + ("" + str(coste_final)) + " leña. ¿Trato?"):
                    lenya_inventario += 0 - coste_final
                    game.splash("¡Patatas conseguidas!")
            else:
                game.splash("Leña insuficiente.",
                    "Necesitas: " + ("" + str(coste_final)))
    elif nena.overlaps_with(cabra):
        coste_unitario = 5
        game.splash("CORRAL CABRAS")
        cantidad = game.ask_for_number("¿Cuántas cabras?", 1)
        if cantidad != int(cantidad):
            game.splash("¡Error! La cabra debe estar entera.")
        if cantidad > 0:
            total_lenya = cantidad * coste_unitario
            if lenya_inventario >= total_lenya:
                if game.ask("Son " + ("" + str(total_lenya)) + "kg de leña. ¿Aceptas?"):
                    lenya_inventario += 0 - total_lenya
                    game.splash("¡Meeeee! (Compra éxito)")
            else:
                game.splash("Falta leña.", "Coste: " + ("" + str(total_lenya)))
    elif nena.overlaps_with(huevo):
        coste_unitario = 0.25
        game.splash("HUEVOS FRESCOS")
        cantidad = game.ask_for_number("¿Docenas o unidades?", 12)
        if cantidad != int(cantidad):
            game.splash("¡Error! Huevos enteros por favor.")
        if cantidad > 0:
            total_lenya = cantidad * coste_unitario
            total_lenya = int(total_lenya * 100) / 100
            if lenya_inventario >= total_lenya:
                if game.ask("Coste: " + ("" + str(total_lenya)) + " leña. ¿Sí?"):
                    lenya_inventario += 0 - total_lenya
                    game.splash("¡Huevos comprados!")
            else:
                game.splash("Leña insuficiente.", "Necesitas: " + ("" + str(total_lenya)))
    elif nena.overlaps_with(caballo):
        coste_unitario = 12
        game.splash("ESTABLO")
        cantidad = game.ask_for_number("¿Cuántos caballos?", 1)
        if cantidad != int(cantidad):
            game.splash("¡Error! Nada de cabezas de caballo.")
        if cantidad > 0:
            total_lenya = cantidad * coste_unitario
            if lenya_inventario >= total_lenya:
                if game.ask("Gran coste: " + ("" + str(total_lenya)) + " leña. ¿Seguro?"):
                    lenya_inventario += 0 - total_lenya
                    game.splash("¡Iiiiih! Caballo tuyo.")
            else:
                game.splash("Muy caro para ti.", "Necesitas: " + ("" + str(total_lenya)))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap4(player25, vendedor4):
    vendedor4.say("Caballo: 12kg (Pulsa A)", 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.Caballo, on_on_overlap4)

def on_on_overlap5(player22, vendedor2):
    vendedor2.say("Patata: Ratio 1.33 (Pulsa A)", 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.Patata, on_on_overlap5)

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

def on_on_overlap6(player23, vendedor3):
    vendedor3.say("Cabra: 12kg (Pulsa A)", 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.Cabra, on_on_overlap6)

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