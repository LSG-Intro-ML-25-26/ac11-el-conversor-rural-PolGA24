# El Conversor Rural - Alcubilla de Avellaneda

## Descripción del Proyecto
Este videojuego simula el sistema de trueque tradicional del pueblo "Alcubilla de Avellaneda". El jugador asume el rol de un vecino que debe aprovechar la "Suerte de Monte" para recolectar leña y canjearla por productos agrícolas y ganaderos en el mercado local.

El objetivo es gestionar el inventario de leña eficientemente y realizar intercambios matemáticos correctos.

## Controles
* **Flechas de Dirección:** Mover al personaje ("Nena") por el mapa.
* **Botón A:** Interactuar con los vendedores y confirmar compras.
* **Choque con Árbol:** Talar y recolectar leña automáticamente.

## Mecánicas y Lógica (Snake Case & Modularidad)

El código sigue una estructura modular estricta para facilitar la lectura y el mantenimiento:

1.  **Recolección (`crear_arbol_aleatorio`):** Los árboles aparecen aleatoriamente en la zona izquierda. Al talarlos, se suman al contador global `lenya_inventario` y reaparecen tras 2 segundos.
2.  **Sistema de Mercado (`crear_mercado`):** 5 vendedores (sprites) con propiedades físicas sólidas (`GHOST = False`) esperan en la zona derecha.
3.  **Lógica de Trueque (`on_a_pressed`):** Al pulsar A, el programa detecta con qué vendedor se interactúa (`overlaps_with`) y ejecuta la fórmula matemática correspondiente.

---

## Evidencias del Funcionamiento

### 1. El Mapa y la Tala
El jugador comienza en el bosque. Al interactuar con los pinos, estos desaparecen con una animación y suman leña al inventario.

<img width="1882" height="686" alt="Captura de pantalla 2025-12-27 145658" src="https://github.com/user-attachments/assets/65838684-f03c-491f-98b7-7a30bcb305f2" />

### 2. Interacción con el Mercado
Al acercarse a un vendedor, este informa del precio mediante un globo de texto (`say`). Al pulsar A, se despliega el menú de `ask_for_number`.

<img width="1892" height="692" alt="Captura de pantalla 2025-12-27 145802" src="https://github.com/user-attachments/assets/a7144887-b80e-4b08-84af-e6894da08c63" />

### 3. Cálculos y Redondeo (Patatas)
El sistema permite comprar patatas con decimales (ej. 1.5 kg) y el programa calcula el coste redondeado a 2 decimales usando matemáticas (`int(x*100)/100`).

<img width="1896" height="696" alt="Captura de pantalla 2025-12-27 145914" src="https://github.com/user-attachments/assets/01f52ba4-2c92-4591-bd38-abad53d949d3" />

### 4. Control de Errores (Anti-Trampas)
Si el usuario intenta comprar "media gallina" (decimales en animales) o introduce números negativos, el sistema detecta el error y bloquea la transacción.

<img width="1892" height="675" alt="Captura de pantalla 2025-12-27 150017" src="https://github.com/user-attachments/assets/5e6d7fa1-6442-48cf-8ec7-2f6970241cd9" />
<img width="1886" height="670" alt="Captura de pantalla 2025-12-27 150054" src="https://github.com/user-attachments/assets/64e283cb-e054-492f-b1cd-c2de463e55b0" />

