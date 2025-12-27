namespace SpriteKind {
    export const Arbol = SpriteKind.create()
    export const Gallina = SpriteKind.create()
    export const Patata = SpriteKind.create()
    export const Cabra = SpriteKind.create()
    export const Huevo = SpriteKind.create()
    export const Caballo = SpriteKind.create()
}

//  Variables globales
sprites.onOverlap(SpriteKind.Player, SpriteKind.Gallina, function on_on_overlap(player2: Sprite, vendedor: Sprite) {
    vendedor.say("Gallina: 6kg (Pulsa A)", 500)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Huevo, function on_on_overlap2(player26: Sprite, vendedor5: Sprite) {
    vendedor5.say("Huevo: 12kg (Pulsa A)", 500)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    animation.runImageAnimation(nena, assets.animation`
            nena-animation-down
            `, 500, false)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    animation.runImageAnimation(nena, assets.animation`
            nena-animation-right
            `, 500, false)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    animation.runImageAnimation(nena, assets.animation`
            nena-animation-left
            `, 500, false)
})
//  Evento de choque
sprites.onOverlap(SpriteKind.Player, SpriteKind.Arbol, function on_on_overlap3(player24: Sprite, arbol_tocado: Sprite) {
    
    //  Confeti
    arbol_tocado.startEffect(effects.fountain, 500)
    music.baDing.play()
    //  Sumar inventario
    lenya_inventario += 1
    player24.say("Leña: " + ("" + ("" + lenya_inventario)), 1000)
    //  Destruir y programar el renacimiento
    sprites.destroy(arbol_tocado)
    control.runInParallel(function esperar_y_renacer() {
        pause(2000)
        crear_arbol_aleatorio()
    })
})
//  Comprar con el boton A
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    let coste_unitario: number;
    let cantidad: number;
    let total_lenya: number;
    let ratio_conversion: number;
    let kilos_patata: number;
    let calculo_bruto: number;
    let coste_final: number;
    
    if (nena.overlapsWith(gallina)) {
        coste_unitario = 6
        game.splash("GALLINERO")
        cantidad = game.askForNumber("¿Cuántas gallinas quieres?", 1)
        if (cantidad != Math.trunc(cantidad)) {
            game.splash("¡Error! No vendemos medias gallinas.")
        }
        
        if (cantidad > 0) {
            total_lenya = cantidad * coste_unitario
            if (lenya_inventario >= total_lenya) {
                if (game.ask("Son " + ("" + ("" + total_lenya)) + "kg de leña. ¿Aceptas?")) {
                    lenya_inventario += 0 - total_lenya
                    game.splash("¡Compra realizada!", "Gallinas: " + ("" + ("" + cantidad)))
                }
                
            } else {
                game.splash("No tienes suficiente leña.", "Necesitas: " + ("" + ("" + total_lenya)))
            }
            
        }
        
    } else if (nena.overlapsWith(patata)) {
        ratio_conversion = 1.3333
        game.splash("HUERTO PATATAS")
        kilos_patata = game.askForNumber("¿Kg de patatas?")
        if (kilos_patata > 0) {
            calculo_bruto = kilos_patata * ratio_conversion
            coste_final = Math.trunc(calculo_bruto * 100) / 100
            if (lenya_inventario >= coste_final) {
                if (game.ask("Coste: " + ("" + ("" + coste_final)) + " leña. ¿Trato?")) {
                    lenya_inventario += 0 - coste_final
                    game.splash("¡Patatas conseguidas!")
                }
                
            } else {
                game.splash("Leña insuficiente.", "Necesitas: " + ("" + ("" + coste_final)))
            }
            
        }
        
    } else if (nena.overlapsWith(cabra)) {
        coste_unitario = 5
        game.splash("CORRAL CABRAS")
        cantidad = game.askForNumber("¿Cuántas cabras?", 1)
        if (cantidad != Math.trunc(cantidad)) {
            game.splash("¡Error! La cabra debe estar entera.")
        }
        
        if (cantidad > 0) {
            total_lenya = cantidad * coste_unitario
            if (lenya_inventario >= total_lenya) {
                if (game.ask("Son " + ("" + ("" + total_lenya)) + "kg de leña. ¿Aceptas?")) {
                    lenya_inventario += 0 - total_lenya
                    game.splash("¡Meeeee! (Compra éxito)")
                }
                
            } else {
                game.splash("Falta leña.", "Coste: " + ("" + ("" + total_lenya)))
            }
            
        }
        
    } else if (nena.overlapsWith(huevo)) {
        coste_unitario = 0.25
        game.splash("HUEVOS FRESCOS")
        cantidad = game.askForNumber("¿Docenas o unidades?", 12)
        if (cantidad != Math.trunc(cantidad)) {
            game.splash("¡Error! Huevos enteros por favor.")
        }
        
        if (cantidad > 0) {
            total_lenya = cantidad * coste_unitario
            total_lenya = Math.trunc(total_lenya * 100) / 100
            if (lenya_inventario >= total_lenya) {
                if (game.ask("Coste: " + ("" + ("" + total_lenya)) + " leña. ¿Sí?")) {
                    lenya_inventario += 0 - total_lenya
                    game.splash("¡Huevos comprados!")
                }
                
            } else {
                game.splash("Leña insuficiente.", "Necesitas: " + ("" + ("" + total_lenya)))
            }
            
        }
        
    } else if (nena.overlapsWith(caballo)) {
        coste_unitario = 12
        game.splash("ESTABLO")
        cantidad = game.askForNumber("¿Cuántos caballos?", 1)
        if (cantidad != Math.trunc(cantidad)) {
            game.splash("¡Error! Nada de cabezas de caballo.")
        }
        
        if (cantidad > 0) {
            total_lenya = cantidad * coste_unitario
            if (lenya_inventario >= total_lenya) {
                if (game.ask("Gran coste: " + ("" + ("" + total_lenya)) + " leña. ¿Seguro?")) {
                    lenya_inventario += 0 - total_lenya
                    game.splash("¡Iiiiih! Caballo tuyo.")
                }
                
            } else {
                game.splash("Muy caro para ti.", "Necesitas: " + ("" + ("" + total_lenya)))
            }
            
        }
        
    }
    
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Caballo, function on_on_overlap4(player25: Sprite, vendedor4: Sprite) {
    vendedor4.say("Caballo: 12kg (Pulsa A)", 500)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Patata, function on_on_overlap5(player22: Sprite, vendedor2: Sprite) {
    vendedor2.say("Patata: Ratio 1.33 (Pulsa A)", 500)
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    animation.runImageAnimation(nena, assets.animation`
            nena-animation-up
            `, 500, false)
})
function crear_mercado() {
    
    //  1. Vendedor GALLINA
    gallina = sprites.create(assets.image`
        pollo
        `, SpriteKind.Gallina)
    gallina.setPosition(113, 73)
    gallina.setFlag(SpriteFlag.Ghost, false)
    //  2. Vendedor PATATA
    patata = sprites.create(assets.image`
        patata
        `, SpriteKind.Patata)
    patata.setPosition(106, 96)
    patata.setFlag(SpriteFlag.Ghost, false)
    //  3. Vendedor CABRA
    cabra = sprites.create(assets.image`
        cabra
        `, SpriteKind.Cabra)
    cabra.setPosition(140, 60)
    cabra.setFlag(SpriteFlag.Ghost, false)
    //  4. Vendedor HUEVOS
    huevo = sprites.create(assets.image`
        egg
        `, SpriteKind.Huevo)
    huevo.setPosition(140, 80)
    huevo.setFlag(SpriteFlag.Ghost, false)
    //  5. Vendedor CABALLO
    caballo = sprites.create(assets.image`
        caballo
        `, SpriteKind.Caballo)
    caballo.setPosition(140, 100)
    caballo.setFlag(SpriteFlag.Ghost, false)
}

sprites.onOverlap(SpriteKind.Player, SpriteKind.Cabra, function on_on_overlap6(player23: Sprite, vendedor3: Sprite) {
    vendedor3.say("Cabra: 12kg (Pulsa A)", 500)
})
function crear_arbol_aleatorio() {
    
    arbol = sprites.create(assets.image`
            treeSmallPine
            `, SpriteKind.Arbol)
    arbol.setPosition(randint(10, 60), randint(40, 110))
}

let arbol : Sprite = null
let caballo : Sprite = null
let huevo : Sprite = null
let cabra : Sprite = null
let patata : Sprite = null
let gallina : Sprite = null
let lenya_inventario = 0
let nena : Sprite = null
let eleccion = 0
scene.setBackgroundImage(assets.image`
    fondo
    `)
nena = sprites.create(assets.image`
        vendedor-front
        `, SpriteKind.Player)
controller.moveSprite(nena)
crear_mercado()
for (let index = 0; index < 6; index++) {
    //  Crear el primer árbol al iniciar
    crear_arbol_aleatorio()
}
