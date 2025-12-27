namespace SpriteKind {
    export const Arbol = SpriteKind.create()
    export const Gallina = SpriteKind.create()
    export const Patata = SpriteKind.create()
    export const Cabra = SpriteKind.create()
    export const Huevo = SpriteKind.create()
    export const Caballo = SpriteKind.create()
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
function crear_mercado() {
    
    //  1. Vendedor GALLINA
    gallina = sprites.create(assets.image`
        pollo
        `, SpriteKind.Gallina)
    gallina.setPosition(113, 73)
    gallina.setFlag(SpriteFlag.Ghost, true)
    //  2. Vendedor PATATA
    patata = sprites.create(assets.image`
        patata
        `, SpriteKind.Patata)
    patata.setPosition(106, 96)
    patata.setFlag(SpriteFlag.Ghost, true)
    //  3. Vendedor CABRA
    cabra = sprites.create(assets.image`
        cabra
        `, SpriteKind.Cabra)
    cabra.setPosition(140, 60)
    cabra.setFlag(SpriteFlag.Ghost, true)
    //  4. Vendedor HUEVOS
    huevo = sprites.create(assets.image`
        egg
        `, SpriteKind.Huevo)
    huevo.setPosition(140, 80)
    huevo.setFlag(SpriteFlag.Ghost, true)
    //  5. Vendedor CABALLO
    caballo = sprites.create(assets.image`
        caballo
        `, SpriteKind.Caballo)
    caballo.setPosition(140, 100)
    caballo.setFlag(SpriteFlag.Ghost, true)
}

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
