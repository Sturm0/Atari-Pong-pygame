# Atari-Pong-pygame
An atari pong clone made in python using pygame. 

jugador 1 (izquierda) utiliza "w" y "s" 
jugador 2 (derecha) las flechas arriba/abajo 
Esto es completamente configurable, dicha asignación de teclas se ecuentra aprox en la línea 200
Con la tecla "p" puede devolver la pelota al centro de la pantalla, sin que se reinicie ningún puntaje.

Error 1:
En Ubuntu 16.04 con python 3.5 y pygame versión 2.0.1 el programa crashea al reproducir un sonido, con un error "Fatal Python error: take_gil: NULL tstate". 
Desactivar el sonido debería ser suficiente para evitar que el error ocurra, desconozco el origen real del problema.

Error 2:
En Ubuntu mate 18.04 usar FULLSCREEN da problemas, en vez de mostrar el juego a pantalla completa muestra toda la pantalla en negro y no responde a alt+f4 para cerrarlo. Utilizar ctrl+alt+f1
para abrir la terminal y matar al proceso usando htop o el gestor de procesos de su preferencia. Con desactivar FULLSCREEN (eliminando dicha opción) es suficiente para evitar que se presente el error.

Sobre "Compilar.py":
"Compilar.py" deja una versión compilada de "Pong.py".
Al ejecutarse debería dejar dentro de una carpeta "pycache" el programa compilado en cuestión.
Únicamente puse esto por si alguien quiere tener una versión del juego que ocupe menos espacio y se ahorre parte del procesamiento inicial si lo va a ejecutar varias veces.
Al momento de hacer las pruebas el juego pesaba 7.06 KB sin compilar y 4.57 KB compilado. 

Sobre línea 101 (aprox):
Descripción de error:
Al ser el primer impacto el jugador 1 la pelota en vez de cambiar de trayectoria vuelve por la misma trayectoria.
Esto se debe a que por alguna razón se detecta la colisión dos veces y se activa 2 veces la función "darvuelta()". Dicho registro de dos veces seguida la colisión se debe a que por razones desconocidas el "x" e "y" no cambian pese
a haber pasado por la función líneal que debería cambiar su valor haciendo que ya no haya colisión alguna.

La solución provisional llevo a crear una función "estado" que cambiara luego de que ocurriera una colisión.

Otras notas sobre el programa:
A partir de la línea 14 hasta la 30 se puede acceder a diferentes configuraciones que podrían ser interesantes para el usuario (cuando fue redactado este documento en ese rango de líneas se encontraba,
pudo haber cambiado para cuando estes leyendo esto).