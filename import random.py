import random

# ----- CREAR BARAJA -----
palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
baraja = [[valor, palo] for valor in valores for palo in palos]

# ----- FUNCIÓN PARA REPARTIR CARTA -----
def pedir_carta():
    return random.choice(baraja)

# ----- FUNCIÓN PARA CALCULAR PUNTAJE -----
def calcular_puntaje(mano):
    return sum([carta[0] for carta in mano])

# ----- SALDO INICIAL -----
dia = int(input("Ingresa día de nacimiento: "))
mes = int(input("Ingresa mes de nacimiento: "))
año = int(input("Ingresa año de nacimiento: "))

suma_fecha = dia + mes + año
multiplicador = random.choice([10, 20, 30])
saldo = suma_fecha * multiplicador

print("\n🎉 Felicidades! Tu multiplicador es:", multiplicador)
print("💰 Tu saldo inicial es:", saldo)

# ----- JUEGO BLACKJACK -----
while saldo > 0:
    print("\n💵 Tu saldo actual es:", saldo)
    apuesta = int(input("¿Cuánto deseas apostar? "))

    if apuesta > saldo:
        print("❌ No puedes apostar más de tu saldo!")
        continue

    # Repartir cartas
    mano_jugador = [pedir_carta(), pedir_carta()]
    mano_banca = [pedir_carta(), pedir_carta()]

    print("\nTus cartas:", mano_jugador, " -> Puntaje:", calcular_puntaje(mano_jugador))
    print("Carta visible de la banca:", mano_banca[0])

    # Turno del jugador
    while True:
        opcion = input("\n¿Quieres otra carta? (s/n): ").lower()
        if opcion == "s":
            mano_jugador.append(pedir_carta())
            puntaje_jugador = calcular_puntaje(mano_jugador)
            print("Tus cartas:", mano_jugador, " -> Puntaje:", puntaje_jugador)
            if puntaje_jugador > 21:
                print("💥 Te pasaste de 21! Pierdes la apuesta.")
                saldo -= apuesta
                break
        else:
            break

    # Turno de la banca (si el jugador no se pasó)
    if calcular_puntaje(mano_jugador) <= 21:
        while calcular_puntaje(mano_banca) < 17:
            mano_banca.append(pedir_carta())

        print("\nCartas de la banca:", mano_banca, " -> Puntaje:", calcular_puntaje(mano_banca))

        # Comparar resultados
        puntaje_jugador = calcular_puntaje(mano_jugador)
        puntaje_banca = calcular_puntaje(mano_banca)

        if puntaje_banca > 21 or puntaje_jugador > puntaje_banca:
            print("🎉 Ganaste la ronda! Ganas:", apuesta)
            saldo += apuesta
        elif puntaje_jugador < puntaje_banca:
            print("😢 Perdiste la ronda! Pierdes:", apuesta)
            saldo -= apuesta
        else:
            print("🤝 Empate! Recuperas tu apuesta.")

    # Ver si el jugador sigue
    if saldo <= 0:
        print("\n💀 Te quedaste sin saldo. Juego terminado.")
        break

    seguir = input("\n¿Quieres jugar otra ronda? (s/n): ").lower()
    if seguir != "s":
        print("\n👋 Gracias por jugar. Te vas con:", saldo)
        break
