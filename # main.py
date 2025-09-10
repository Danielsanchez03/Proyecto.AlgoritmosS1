# proyecto Blackjack con saldo.
import random

# creamos la baraja = valores y palos
Lista_palos = ["Corazones", "Diamantes", "Treboles", "Picas"]
Lista_valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# definimos los componentes de nuestra baraja con un "bucle for" para valor y palo
Baraja_blackjack = [[valor, palo] for valor in Lista_valores for palo in Lista_palos]

# definimos como se obtendra el saldo inicial
# definimos nuestras variables que seran dia, mes y año de nacimiento
while True:
    try:
        dia = int(input("ingresa dia de nacimiento: ").strip())
        mes = int(input("ingresa mes de nacimiento: ").strip())
        año = int(input("ingresa año de nacimiento: ").strip())
        break
    except ValueError:
        print("Por favor ingresa números válidos para día, mes y año.")

# sumamos nuestras variables
suma_fecha = dia + mes + año
# hacemos un multiplicador random de 10, 20 o 30
multiplicador = random.choice([10, 20, 30])
# calculamos el saldo final operando la suma por el multiplicador random
saldo = suma_fecha * multiplicador

# mostramos el saldo despues de la operación y el multiplicador obtenido
print("felicidades obtuviste tu multiplicador es de:", multiplicador)
print("Tu saldo es de:", saldo)

# definimos la función para pedir una carta
def pedir():
    return random.choice(Baraja_blackjack)

# definimos la función para calcular el puntaje de la mano.
# suma el valor numérico de cada carta (posición 0 de la lista [valor,palo])
def calcular_puntaje(mano):
    return sum([carta[0] for carta in mano])

# -----------Inicia el juego--------------
# Hacemos el ciclo principal del juego y se repite mientras el saldo sea positivo
while saldo > 0:
    print("\nTu saldo actual es de:", saldo)

    # Pedir apuesta con validación
    while True:
        try:
            apuesta = int(input("Cuanto quieres apostar?: ").strip())
            if apuesta <= 0:
                print("La apuesta debe ser mayor que 0.")
                continue
            if apuesta > saldo:
                print("No puedes apostar mas de tu saldo.")
                continue
            break
        except ValueError:
            print("Ingresa un número entero para la apuesta.")

    # repartimos cartas iniciales (dos para el jugador y dos para el dealer)
    mano_jugador = [pedir(), pedir()]
    mano_dealer = [pedir(), pedir()]

    # mostramos las cartas del jugador y la carta visible del dealer
    print("tus cartas son:", mano_jugador)
    print("tu puntaje actual es:", calcular_puntaje(mano_jugador))
    print("la carta visible del dealer es:", mano_dealer[0])

    # Inicia el turno del jugador (pedir carta/plantarse)
    while calcular_puntaje(mano_jugador) < 21:
        opcion = input("Quieres otra carta? si/no: ").strip().lower()
        if opcion == "si":
            mano_jugador.append(pedir())
            print("tus cartas son:", mano_jugador)
            print("tu puntaje es:", calcular_puntaje(mano_jugador))
            # si se pasa, salimos del bucle para procesar la pérdida
            if calcular_puntaje(mano_jugador) > 21:
                break
        else:
            break

    # si el jugador se pasa de 21, pierde automáticamente
    if calcular_puntaje(mano_jugador) > 21:
        print("Perdiste la ronda (te pasaste).")
        saldo -= apuesta
    else:
        # turno del dealer (pedir cartas hasta 17 o más)
        while calcular_puntaje(mano_dealer) < 17:
            mano_dealer.append(pedir())

        # mostramos las cartas del dealer
        print("cartas del dealer:", mano_dealer)
        print("Puntaje del dealer:", calcular_puntaje(mano_dealer))

        # calculamos puntajes finales
        puntaje_jugador = calcular_puntaje(mano_jugador)
        puntaje_dealer = calcular_puntaje(mano_dealer)

        # damos resultados finales y actualizamos saldo correctamente
        if puntaje_dealer > 21 or puntaje_jugador > puntaje_dealer:
            print("Ganaste la ronda")
            saldo += apuesta
        elif puntaje_jugador == puntaje_dealer:
            print("Empate, No ganas ni pierdes")
            # saldo no cambia
        else:
            print("Perdiste la ronda")
            saldo -= apuesta

    # verificar si quedó saldo
    if saldo <= 0:
        print("Te quedaste sin saldo")
        break

    # preguntar si quiere seguir jugando (si/no)
    while True:
        seguir = input("Quieres seguir jugando? (si/no): ").strip().lower()
        if seguir in ("si", "no"):
            break
        print("Responde 'si' o 'no'.")

    if seguir == "no":
        print("Gracias por jugar. Tu saldo final es de:", saldo)
        break
    # si seguir == "si" el while principal vuelve y se pide apuesta de nuevo
