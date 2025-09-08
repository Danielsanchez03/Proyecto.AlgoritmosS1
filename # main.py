#proyecto Blackjack con saldo.
#importamos librerias necesarias
import random
#creamos la baraja = valores y palos
Lista_palos = ["Corazones" , "Diamantes" , "Treboles" , "Picas"]
Lista_valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#definimos los componentes de nuestra baraja con un "bucle for" para valor y palo
Baraja_blackjack = [[valor, palo] for valor in Lista_valores for palo in Lista_palos]

#definimos como se obtendra el saldo inicial
#definimos nuestras variables que seran dia, mes y año de nacimiento
dia = int(input("ingresa dia de nacimiento"))
mes = int(input("ingresa mes de nacimiento"))
año = int(input("ingresa año de nacimiento"))
#sumamos nuestras variables
suma_fecha = dia + mes + año
#hacemos un multiplicador random de 10, 20 o 30
multiplicador = random.choice([10 , 20 , 30])
#calculamos el saldo final operando la suma por el multiplicador random
saldo = suma_fecha * multiplicador

#mostramos el saldo despues de la operación y el multiplicador obtenido
print("felicidades obtubiste tu multiplicador es de:  " , multiplicador)
print("Tu saldo es de:   " , saldo)

#definimos la función para pedir una carta
def pedir():
    return random.choice(Baraja_blackjack)

#definimos la función para calcular el puntaje de la mano. suma el valor numérico de cada carta (posición 0 de la lista [valor,palo])
def calcular_puntaje(mano):
    return sum([carta[0]for carta in mano])

#-----------Inicia el juego--------------
#Hacemos el ciclo principal del juego y se repite mientras el saldo sea positivo
while saldo > 0:
    print("Tu saldo actual es de:  " , saldo)
    apuesta = int(input("Cuanto quieres apostar?"))
    if apuesta > saldo:
        print("No puedes apostar mas de tu saldo.")
    else:
        break

#repartimos cartas iniciales (dos para el jugador y dos para el dealer)
mano_jugador = [pedir(), pedir()]
mano_dealer = [pedir(), pedir()]

#mostramos las cartas del jugador y la carta visible del dealer
print("tus cartas son:  " , mano_jugador)
print("tu puntaje actual es:  " , calcular_puntaje(mano_jugador))
print("la carta visible del dealer es: " , mano_dealer[0])

#Inicia el turno del jugador (pedir carta, plantarse)
while calcular_puntaje(mano_jugador) < 21:
    opcion = input("Quieres otra carta si/no: ").lower()
    if opcion == "si":
        mano_jugador.append(pedir())
        print("tus cartas son" , mano_jugador)
        print("tu puntaje es: " , calcular_puntaje(mano_jugador))
    else:
        break

    #si el jugador se pasa de 21, pierde automaticamente
    if calcular_puntaje(mano_jugador) > 21:
        print("Perdiste la partida")
        saldo -= apuesta
        continue

#turno del dealer (pedir cartas hasta 17 o mas)
while calcular_puntaje(mano_dealer) > 17:
    mano_dealer.append(pedir()) 

#Mostramos las cartas del dealer

print("cartas del dealer" , mano_dealer)
print("Puntaje del dealer" , calcular_puntaje(mano_dealer))

#calculamos puntajes finales
puntaje_jugador =( calcular_puntaje(mano_jugador))
puntaje_dealer = (calcular_puntaje(mano_dealer))

#Damos resultados finales

if puntaje_dealer > 21 or puntaje_dealer < puntaje_jugador:
    print("Ganaste la ronda")
    apuesta += saldo

elif puntaje_jugador == puntaje_dealer:
    print("Empate, No ganas ni pierdes  ")

else:
    print("Perdiste la ronda ")
    apuesta -= saldo

#Preguntamos si quiere seguir jugando
jugar = int(input("Quieres seguir jugando?  (si/no)  "))
if jugar == "si":
    