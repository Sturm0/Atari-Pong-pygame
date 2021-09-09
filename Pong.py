import pygame, sys
from pygame.locals import *
from time import sleep
from random import randint,uniform,choice
from os import system, name

#Configuraciones
puntaje_objetivo = 12 #Determina con cuantos puntos se gana
resolución = (656,492)

pygame.init()
sonido_act = True #Sonido activado
if sonido_act == True:
	sonido = pygame.mixer.Sound("pongblipf-5.wav")#En Ubuntu 16.04 con python 3.5 y pygame versión 2.0.1 el programa crashea al reproducir un sonido, más información en la sección de problemas de github
	sonido.set_volume(0.5)
miFuente = pygame.font.Font('pong-score.ttf',64)
ventana = pygame.display.set_mode(resolución,flags=pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.SCALED) #Configuración de ventana, SCALED solo sirve para pygame 2 o superior desactivar si se esta usando una versión anterior. FULLSCREEN según pruebas da problemas en ciertos casos
puntJugador1 = 0
puntJugador2 = 0
mostrPuntj1 = miFuente.render("0",0,(255,255,255))
mostrPuntj2 = miFuente.render("0",0,(255,255,255))
velocidad = 4 #velocidad a la que pueden mover los jugadores las paletas
velocidad_p = 4 #determina la velocidad a la cual se mueve la pelota

#Variables abstractas
estado = True #Fue creado para solucionar un error de origen desconocido, es usada en la línea 101
ult_col = None #Última colisión

#Creación de los jugadores y sus respectivos puntajes
class Player():
	def __init__(self,posiciónX,posiciónY):
		self.rectangulo = pygame.Rect(posiciónX,posiciónY,8,8*3) #desde acá se cambia el tamaño de los jugadores (los dos últimos valores)

jugador1 = Player(70,resolución[1]/2) 
jugador2 = Player(resolución[0]-70-8,resolución[1]/2)
puntajes = [0,0]

#Creación de rectangulos
rectangulo1 = pygame.Rect(0,0,resolución[0],1)
rectangulo2 = pygame.Rect(0,0,1,resolución[0])
rectangulo3 = pygame.Rect(resolución[0]-1,0,1,resolución[0])
rectangulo4 = pygame.Rect(0,resolución[1]-1,resolución[0],1)
pelota = pygame.Rect(resolución[0]/2,resolución[1]/2,8,8)

#Esta sección pone las líneas que aparecen en el medio de la ventana
lineas_medio = []
valor_a = (resolución[0]/2)-2
valor_b = 0

while valor_b < resolución[1]:
	lineas_medio.append(pygame.Rect(valor_a,valor_b,4,8))
	valor_b += 16

rectangulos = (jugador1.rectangulo,jugador2.rectangulo,rectangulo1,rectangulo2,rectangulo3,rectangulo4) #lista de colisión
clausulas = [False]*6

#Acá se determina la pendiente inicial de la función lineal
m1 = round(uniform(-0.67,0.67),5)
m2 = 1
div = m1/m2

while abs(m1) < 0.14: #si es 0 la trayectoria de la pelota nunca va a cambiar y si es muy poca el juego va a ser aburrido
	m1 = round(uniform(-0.67,0.67),5)

x = round(resolución[0]/2)
elección = choice((False,True))

def darvuelta(div,acum=0):
	if acum == 0:
		if div > 0:
			div = -div
		else:
			div = abs(div)
	return div

#determina la trayectoria al tocar cada superficie, es utilizada en el while principal
def trayectoria(índice):
		global x,y,nuev_x ,div,estado ,ult_col

		clausulas[índice] = True
		pelota.top = (div*(x - nuev_x))+y
		pelota.left = x

		if pelota.collidelist(rectangulos) == -1:
			
			if índice == 0: #Es para que la pelota rebote a la derecha cuando toca al jugador 1 y no a la izquierda
				x += velocidad_p
			elif (índice == 2 or índice == 5) and ult_col == 0:
				x += velocidad_p
			else:
				x -= velocidad_p
			
		elif pelota.collidelist(rectangulos) == índice and estado == True: #Estado fue creado para solucionar un error de origen real desconocido, consultar las notas sobre el programa
			div = darvuelta(div,0)
			if sonido_act == True:
				sonido.play()
			y = pelota.top
			nuev_x = x

			if índice == 0:
				x += velocidad_p
			elif (índice == 2 or índice == 5) and ult_col == 0:
				x += velocidad_p
			else:
				x -= velocidad_p
			estado = False

		elif pelota.collidelist(rectangulos) == índice:
			if índice == 0:
				x += velocidad_p
			elif (índice == 2 or índice == 5) and ult_col == 0:
				x += velocidad_p
			else:
				x -= velocidad_p
		else:
			ult_col = índice
			estado = True
			clausulas[índice] = False

#se utiliza en el ciclo while principal
def comprobación(número): 
	if pelota.collidelist(rectangulos) == número or clausulas[número] == True:
		return True
	else:
		return False

#Función para manejar la colisión con las superficies detrás de los jugadores
def caso_especial(jugador,lado):
	global puntajes, puntaje_objetivo,mostrPuntj1,mostrPuntj2,pelota,nuev_x,y,x,div,elección
	puntajes[jugador] +=1
	if puntajes[jugador] == puntaje_objetivo:
		pygame.quit()
		print('El jugador %s ganó la partida'%(jugador+1),lado)
		input('\nPresione alguna tecla para cerrar esta ventana')
		sys.exit()
	mostrPuntj1 = miFuente.render(str(puntajes[0]),0,(255,255,255))
	mostrPuntj2 = miFuente.render(str(puntajes[1]),0,(255,255,255))
	pelota.left = resolución[0]/2
	pelota.top = resolución[1]/2
	nuev_x = resolución[0]/2
	y = resolución[1]/2
	x = round(resolución[0]/2)
	div = round(uniform(-0.67,0.67),5)
	while abs(div) < 0.14: #si es 0 la trayectoria de la pelota nunca va a cambiar y si es muy poca el juego va a ser aburrido
		div = round(uniform(-0.67,0.67),5)
	elección = choice((False,True))

nuev_x = resolución[0]/2 #Nuevo eje de coordenadas
y = resolución[1]/2
while True:
	ventana.fill((0,0,0))
	posY = randint(0,resolución[1])
	
	if pelota.collidelist(rectangulos) <= -1 and not True in clausulas:
		pelota.top = ((div)*(x - resolución[0]/2))+resolución[1]/2
		pelota.left = x
		if elección == True:
			x += velocidad_p
		else:
			x -= velocidad_p
	elif comprobación(0):
		trayectoria(0)

	elif comprobación(1):
		trayectoria(1)
	
	elif comprobación(2):
		trayectoria(2)

	elif pelota.collidelist(rectangulos) == 3: #3 y 4 son los rectangulos que representan los lados que están opuestos a los jugadores
		caso_especial(1,'(derecha)')

	elif pelota.collidelist(rectangulos) == 4:
		caso_especial(0,'(izquierda)')

	elif comprobación(5):
		trayectoria(5)
	
	#Acá se configura la asignación de teclas
	keys = pygame.key.get_pressed()
	if keys[K_w]:
		jugador1.rectangulo.top -= velocidad
	if keys[K_s]:
		jugador1.rectangulo.top += velocidad
	if keys[K_UP]:
		jugador2.rectangulo.top -= velocidad
	if keys[K_DOWN]:
		jugador2.rectangulo.top += velocidad

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		if event.type == KEYDOWN:
			if event.key == K_p:
				pelota.left = resolución[0]/2
				pelota.top = resolución[1]/2
				nuev_x = resolución[0]/2
				y = resolución[1]/2
				x = round(resolución[0]/2)
				div = round(uniform(-0.67,0.67),5)
				elección = choice((False,True))

	#Acá se hace todo el muestreo
	for each in lineas_medio:
		pygame.draw.rect(ventana,(255,255,255),each)

	pygame.draw.rect(ventana,(255,255,255),jugador1.rectangulo)
	pygame.draw.rect(ventana,(255,255,255),jugador2.rectangulo)
	pygame.draw.rect(ventana,(255,255,255),pelota)
	ventana.blit(mostrPuntj1,(166,33))
	ventana.blit(mostrPuntj2,(resolución[0]-166-32,33))

	sleep(1/60) #Determina los FPS, la velocidad del juego esta ligada a los mismos.
	pygame.display.update()
