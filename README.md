# Atari-Pong-pygame
An atari pong clone made in python using pygame. I tried to make it as close to the original as possible.

## English:
Player 1 (left) controls: 'w','s'

Player 2 (right) controls: 'up arrow','down arrow'

This is completely configurable, said key assignment is located approx on line 200.
With the "p" key you can return the ball to the center of the screen, without any score being reset.

## Español:
jugador 1 (izquierda) utiliza "w" y "s" 

jugador 2 (derecha) las flechas arriba/abajo 

Esto es completamente configurable, dicha asignación de teclas se ecuentra aproximadamente en la línea 200.

Con la tecla "p" se puede devolver la pelota al centro de la pantalla, sin que se reinicie ningún puntaje.
El juego proporciona una gran variedad de configuraciones desde aproximadamente la línea 14 hasta la 30.

## Sobre "Compilar.py":
"Compilar.py" deja una versión compilada de "Pong.py".
Al ejecutarse debería dejar dentro de una carpeta "pycache" el programa compilado en cuestión.
Únicamente puse esto por si alguien quiere tener una versión del juego que ocupe menos espacio y se ahorre parte del procesamiento inicial si lo va a ejecutar varias veces.
Al momento de hacer las pruebas el juego pesaba 7.22 KB sin compilar y 4.67 KB compilado. 

## Sobre línea 101 (aprox):
Descripción de error:
Al ser el primer impacto el jugador 1 la pelota en vez de cambiar de trayectoria vuelve por la misma trayectoria.
Esto se debe a que por alguna razón se detecta la colisión dos veces y se activa 2 veces la función "darvuelta()". Dicho registro de dos veces seguida la colisión se debe a que por razones desconocidas el "x" e "y" no cambian pese
a haber pasado por la función líneal que debería cambiar su valor haciendo que ya no haya colisión alguna.

La solución provisional llevo a crear una función "estado" que cambiara luego de que ocurriera una colisión.

Otras notas sobre el programa:
A partir de la línea 14 hasta la 30 se puede acceder a diferentes configuraciones que podrían ser interesantes para el usuario (cuando fue redactado este documento en ese rango de líneas se encontraba,
pudo haber cambiado para cuando estes leyendo esto).
