namespace SpriteKind {
    export const Arbol = SpriteKind.create()
    export const Comerciante = SpriteKind.create()
}

//  Variables globales
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    animation.runImageAnimation(nena, assets.animation`
            nena-animation-down
            `, 500, false)
})
//  Evento de choque (Usando los tipos correctos)
sprites.onOverlap(SpriteKind.Player, SpriteKind.Arbol, function on_on_overlap(player2: Sprite, arbol_tocado: Sprite) {
    
    //  Efectos visuales
    arbol_tocado.startEffect(effects.fountain, 500)
    music.baDing.play()
    //  Sumar inventario
    lenya_inventario += 1
    player2.say("Leña: " + ("" + ("" + lenya_inventario)), 1000)
    //  Destruir y programar el renacimiento
    sprites.destroy(arbol_tocado)
    control.runInParallel(function esperar_y_renacer() {
        pause(2000)
        crear_arbol_aleatorio()
    })
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
controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    animation.runImageAnimation(nena, assets.animation`
            nena-animation-up
            `, 500, false)
})
function crear_arbol_aleatorio() {
    
    arbol = sprites.create(assets.image`
            treeSmallPine
            `, SpriteKind.Arbol)
    arbol.setPosition(randint(10, 60), randint(40, 110))
}

let arbol : Sprite = null
let lenya_inventario = 0
let nena : Sprite = null
scene.setBackgroundImage(assets.image`
    fondo
    `)
nena = sprites.create(assets.image`
    nena-front
    `, SpriteKind.Player)
controller.moveSprite(nena)
for (let arbol2 = 0; arbol2 < 6; arbol2++) {
    //  Crear el primer árbol al iniciar
    crear_arbol_aleatorio()
}
