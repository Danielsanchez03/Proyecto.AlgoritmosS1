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
saldo_final = suma_fecha * multiplicador

#mostramos el saldo despues de la operación y el multiplicador obtenido
print("felicidades obtubiste tu multiplicador es de:  " , multiplicador)
print("Tu saldo es de:   " , saldo_final)

#definimos la función para pedir una carta
def pedir():
    return random.choice(Baraja_blackjack)

#función para calcular el puntaje de la mano
def calcular_puntaje(mano):
    return sum([carta[0]for carta in mano])
